# -*- coding: utf-8 -*-
# import urllib3.request, urllib3.parse, urllib3.error, json
import certifi
import urllib3, json
import base64
import socket
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api, _

class MukiREST(models.Model):
	_name = "muki.rest"
	_description = "Visitor Search"

	user_id = fields.Many2one('res.users', string="Current User",
		default=lambda self: self.env.user)

	hstatus = fields.Selection([
		('Check-OUT', 'Check-OUT'),
		('Cancelled', 'Cancelled'),
		('Declined', 'Declined'),
		('Draft', 'Draft'),
		('Revision', 'Revision'),
		('Check-IN', 'Check-IN'),
		('Approved', 'Approved'),
		('Submit', 'Submit')],string = 'Status')
	nombre = fields.Char("Name")
	fname = fields.Char("First Name")
	lname = fields.Char("Last Name")
	visitor_email = fields.Char("Email")
	hvisit = fields.Char("Visitor ID")
	hstreet = fields.Char("Street")
	hstreet2 = fields.Char("Street2")
	hcity = fields.Char("City")
	hzip = fields.Char("Zip")
	hcountry = fields.Char("Country")
	hcateg = fields.Char("Visitor Category")

	def search_visitor(self):
		ip_address = '34.66.235.140'
		#CONVIRTIENDO A FORMATO ASCII EL IP
		ip_address_bytes = ip_address.encode('ascii')
		#CONVIRTIENDO A BASE64 EL IP
		ipBase = base64.b64encode(ip_address_bytes)
		http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		url = 'https://visitors.stri.si.edu/services/getVisits'
		
		values = dict()
		filtros_dic = {
			"visitor_id":self.hvisit,
			"status": self.hstatus,
			"visitor_name":self.nombre,
			"name":self.fname,
			"last_name":self.lname,
			"email":self.visitor_email}

		for key, value in filtros_dic.items():
			if (value != False):
				values[key] = value
		# values = {"visitor_id":self.hvisit,"status": self.hstatus,"visitor_name":self.nombre}
		logging.info("VALUES: " + str(values))
	
		headers={'Accept': 'application/json',
				'X-VSO-caller': ipBase}

		datas = http.request('POST', url, fields=values, headers=headers)

		datas = json.loads(datas.data.decode('utf-8'))
		logging.info("CONTENIDO: " + str(datas['visit']))

		for data in datas['visit']:
			hvisit= data['user_id']
			nombre= data['visitor_name']
			fname= data['first_name']
			lname= data['last_name']
			visitor_email=data['email']
			hstatus=data['status']
			hcateg=data['visitor_category']
			address = data['funding']['address']
			if address is None:
				hstreet=data['funding']['address']['line1']
				hstreet2=data['funding']['address']['line2']
				hcity=data['funding']['address']['city']
				hzip=data['funding']['address']['zip']
				hcountry=data['funding']['address']['country']
			else:
				hstreet=""
				hstreet2=""
				hcity=""
				hzip=""
				hcountry=""
			self.env['muki.rest'].create({
				'hvisit': hvisit,
				'nombre': nombre,
				'fname': fname,
				'lname': lname,
				'visitor_email': visitor_email,
				'hstatus': hstatus,
				'hcateg':hcateg,
				'hstreet':hstreet,
				'hstreet2':hstreet2,
				'hcity':hcity,
				'hzip':hzip,
				'hcountry':hcountry,
				})

		action = self.env.ref('template_module.muki_rest_action').read()[0]
		action['target'] = 'main'
		return action	
		# print(datas)

		"""for data in datas['visit']:
			self.env['muki.rest'].create({
				'hvisit': data['user_id'],
				'nombre': data['visitor_name'],
				'fname': data['first_name'],
				'lname': data['last_name'],
				'visitor_email': data['email'],
				'hstatus': data['status'],
				'hstreet':data['funding']['address']['line1'],
				'hstreet2':data['funding']['address']['line2'],
				'hcity':data['funding']['address']['city'],
				'hzip':data['funding']['address']['zip']
				# 'hstreet':data['line1'],
				# 'hstreet2':data['line2'],
				# 'hcity': data['city'],
				# 'hzip': data['zip']
			}) """