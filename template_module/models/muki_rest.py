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
			
		# print(datas)

	#ESTOY AGREGANDO LA FUNCION PARA CREAR EL CUSTOMER AQUI
	def create_customer(self):
        # context = dict(self._context or {})
        # active = self.env['muki.rest'].browse(context.get('active_ids'))
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['muki.rest'].browse(active_ids):
            record.nombre = self.nombre
            record.visitor_email = self.visitor_email
            record.hvisit = self.hvisit
            self.env["res.partner"].create({'name':record.nombre,'email':record.visitor_email, 'visitor':record.hvisit})
