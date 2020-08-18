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
	visitor = fields.Integer("Visitor ID")

	def search_visitor(self):
		ip_address = '34.66.235.140'
		#CONVIRTIENDO A FORMATO ASCII EL IP
		ip_address_bytes = ip_address.encode('ascii')
		#CONVIRTIENDO A BASE64 EL IP
		ipBase = base64.b64encode(ip_address_bytes)
		# ipBase = 'MTkwLjE0MC4xNjUuNDU='

		http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		url = 'https://visitors.stri.si.edu/services/getVisits'

		#aqui hacer un for para recorrer el wizard y obtener los valores de los campos?
		values = {"status": "Check-OUT","name": "Paula","visitor_id": "295"}
		logging.info("VALUES: " + str(values))
	
		headers={'Accept': 'application/json',
				'X-VSO-caller': ipBase}

		datas = http.request('POST', url, fields=values, headers=headers)
		logging.info("DATA: " + str(datas.data))

		datas = json.loads(datas.data.decode('utf-8'))
		logging.info("QUE TENGO EN DATA: " + str(datas))
	
		for data in datas:
			v = data.get('user_id')
			n = data.get('visitor_name')
			f = data.get('first_name')
			l = data.get('last_name')
			c = data.get('email')
			s = data.get('status')
			self.env["muki.rest"].create({'visitor':v,'nombre':n,'fname':f,'lname':l,'visitor_email':c,'hstatus':s})
			
		""" for data in datas:
			self.env['muki.rest'].create({
		 	   'visitor': data['user_id'],
		 	   'nombre': data['visitor_name'],
		 	   'fname': data['first_name'],
		 	   'lname': data['last_name'],
		 	   'visitor_email': data['email'],
		 	   'hstatus': data['status']
			})
			logging.info("CONTENIDO: " + str(datas))
		print(datas) """

""" import requests
response = requests.get("http://httpbin.org/get")
print('Response from httpbin/get')
print(response.json())
print()
print('response.request.headers')
print(response.request.headers) """