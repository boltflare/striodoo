# -*- coding: utf-8 -*-

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
		# con esto conseguiremos la IP del host que este ejecutando la peticion
		# hostname = socket.gethostname()
		# ip_address = socket.gethostbyname(hostname)
		ip_address = '190.140.165.45'
		# transformamos la ip a ascii para que la pueda leer el modulo base64
		ip_address_bytes = ip_address.encode('ascii')
		# se transforma en base 64
		ipBase = base64.b64encode(ip_address_bytes)
		# print(ipBase)
		# url del web service
		url = 'https://visitors.stri.si.edu/services/getVisits'
		# aqui se armaria el diccionario con los valores necesarios para los filtros
		values = {"status": "Check-OUT", "name": "Paula"}
		# values = {"visitor_id": "visitor","status": "hstatus" }

		# a continuacion, se utiliza urllib.parse.urlencode para transformar los valores a un formato valido del request
		data = urllib3.parse.urlencode(values).encode('utf-8')
		# declaramos los headers necesarios
		headers={'Accept': 'application/json',
				'X-VSO-caller': ipBase}

		# aramamos el request tipo post de la libreria
		req = urllib3.request.Request(url, data=data, headers=headers)
		logging.info("REQ:" + str(req))
		# print(req)

		# esta funcion deberia abrir la respuesta enviada en el request
		rsp = urllib3.request.urlopen(req)
		logging.info("CONTIENE:" + str(rsp))
		# print(rsp.read)
		# con esta linea leemos los datos de la respuesta
		content = rsp.read()
						   
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
		print(content)