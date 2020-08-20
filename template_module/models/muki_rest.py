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

	def search_visitor(self):
		ip_address = '35.222.101.46'
		#CONVIRTIENDO A FORMATO ASCII EL IP
		ip_address_bytes = ip_address.encode('ascii')
		#CONVIRTIENDO A BASE64 EL IP
		ipBase = base64.b64encode(ip_address_bytes)
		# ipBase = 'MTkwLjE0MC4xNjUuNDU='

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
		logging.info("CONTENIDO: " + str(datas))

		for data in datas['visit']:
			self.env['muki.rest'].create({
		 	   'hvisit': data['user_id'],
		 	   'nombre': data['visitor_name'],
		 	   'fname': data['first_name'],
		 	   'lname': data['last_name'],
		 	   'visitor_email': data['email'],
		 	   'hstatus': data['status']
			})

		action = self.env.ref('template_module.muki_rest_action').read()[0]
		action['target'] = 'main'
		return action	
		# print(datas)

