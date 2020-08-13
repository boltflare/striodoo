# -*- coding: utf-8 -*-
# import urllib3.request, urllib3.parse, urllib3.error, json
import urllib3, json
import certifi
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
	visitor = fields.Char("Visitor ID")


	def search_visitor(self):
		ip_address = '190.140.165.45'
		#CONVIRTIENDO A FORMATO ASCII EL IP
		ip_address_bytes = ip_address.encode('ascii')
		#CONVIRTIENDO A BASE64 EL IP
		ipBase = base64.b64encode(ip_address_bytes)

		http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		url = 'https://visitors.stri.si.edu/services/getVisits'

		values = {"status": "Check-OUT","name": "Paula"}
		logging.info("VALUES: " + str(values))
		
		headers={'Accept': 'application/json',
				'X-VSO-caller': ipBase}

		datas = http.request('POST', url, fields=values, headers=headers)
		logging.info("DATA: " + str(datas))

		datas = json.loads(datas.data.decode('utf-8'))
		logging.info("VALOR: " + str(datas.data))
	
		# data = urllib.parse.urlencode(values).encode('utf-8')
		# declaramos los headers necesarios
		for data in datas:
		   self.env['muki.rest'].create({
			   'visitor': data['visitor_id'],
			   'nombre': data['visitor_name'],
			   'fname': data['name'],
			   'lname': data['last_name'],
			   'visitor_email': data['email'],
			   'hstatus': data['status']
		   })
		   logging.info("CONTENIDO: " + str(datas))
		# print(datas)
