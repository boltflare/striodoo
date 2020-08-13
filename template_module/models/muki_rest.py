# -*- coding: utf-8 -*-
# import urllib3.request, urllib3.parse, urllib3.error, json
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
	visitor_name = fields.Char("Name")
	name = fields.Char("First Name")
	last_name = fields.Char("Last Name")
	visitor_email = fields.Char("Email")
	visitor = fields.Char("Visitor ID")


	def search_visitor(self):
		ip_address = '190.140.165.45'
		#CONVIRTIENDO A FORMATO ASCII EL IP
		ip_address_bytes = ip_address.encode('ascii')
		#CONVIRTIENDO A BASE64 EL IP
		ipBase = base64.b64encode(ip_address_bytes)


		http = urllib3.PoolManager()
		url = 'https://visitors.stri.si.edu/services/getVisits'

		values = {"status": "hstate","name": "name"}
		headers={'Accept': 'application/json',
				'X-VSO-caller': ipBase}


		datas = http.request('POST', url, fields=values, headers=headers)
		datas = json.loads(datas.data.decode('utf-8'))
		# data = urllib.parse.urlencode(values).encode('utf-8')
		# declaramos los headers necesarios

		print(datas)
						   
		# for entry1 in content:
		# 	visita = entry1.get('visitor_id')
		# 	nom = entry1.get('visitor_name')
		# 	fna = entry1.get('name')
		# 	lna = entry1.get('last_name')
		# 	mail = entry1.get('email')
		# 	estado = entry1.get('status')     
		# 	self.env["muki.rest"].create({'visitor':visita,'visitor_name':nom, 'name':fna, 'last_name':lna, 'visitor_email':mail, 'hstatus':estado })
		# 	logging.info(str(rsp))
			
		# imprimimos la respuesta, este content es el que se utilizaria para enviar la data a la vista segun se requiera
