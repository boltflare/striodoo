# -*- coding: utf-8 -*-
# import urllib3.request, urllib3.parse, urllib3.error, json
import certifi
import urllib3, json
import base64
import socket
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api, _
from odoo.exceptions import RedirectWarning

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

	#FUNCION PARA HACER REPLACE DE VALORES NONE
	def replace(self,data, search, replacement, parent=None, index=None):
		if data == search:
			parent[index] = replacement
		elif isinstance(data, (list, dict)):
			for index, item in enumerate(data) if isinstance(data, list) else data.items():
				self.replace(item, search, replacement, parent=data, index=index)

	#FUNCION PARA HACER VALIDACION DE LOS KEYS DENTRO DE ADDRESS
	def verify_keys(self,address):
		if {'line1', 'line2','country', 'city', 'zip'} <= address.keys():
			return True
		else:
			return False	

	#FUNCION PARA HACER REQUEST Y OBTENER JSON CON LOS RESULTADOS DE LA BUSQUEDA
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
		# logging.info("DICCIONARIO: " + str(datas))
		#VARIABLE PARA MOSTRAR EXCEPCION EN CASO DE NO OBTENER RESULTADO
		action = self.env.ref('template_module.muki_rest_action')
		try:
			datas = json.loads(datas.data.decode('utf-8'))
		except Exception:
			raise RedirectWarning("No se han encontrado resultados!", action.id, _('OK'))
		
		self.replace(datas, None, 'None')
		self.replace(datas, [], 'None')
		logging.info("CONTENIDO: " + str(datas.values()))

		for value in datas.values():
			for data in value:
				hvisit= data['user_id']
				nombre= data['visitor_name']
				fname= data['first_name']
				lname= data['last_name']
				visitor_email=data['email']
				hstatus=data['status']
				hcateg=data['visitor_category']
				address = data['funding']['address']
				# logging.info("ADDRESS: " + str(address))
				if address != 'None':
					if self.verify_keys(address):
						hstreet=address['line1']
						hstreet2=address['line2']
						hcity=address['city']
						hzip=address['zip']
						hcountry=address['country']
						# logging.info("DENTRO DEL IF: " + str(address))
				else:
					hstreet=""
					hstreet2=""
					hcity=""
					hzip=""
					hcountry=""
					# logging.info("DENTRO DEL ELSE: " + str(address))
		
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