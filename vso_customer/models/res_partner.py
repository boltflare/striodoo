# -*- coding: utf-8 -*-

from . import library
import json
from odoo import models, fields, api


import logging
_logger = logging.getLogger(__name__)

class ResPartnerInherit(models.Model):
	_inherit = "res.partner"

	def action_muki_connect(self):
		# init API
		api = library.RestAPI()
		api.authenticate()

		
		# test API
		logging.info(str(api.execute('/api')))
		logging.info(str(api.execute('/api/custom/create/vso')))

		#SEARCH AND CREATE CUSTOMER 
		""" values = {
			'name': "Prueba VSO",
			'visitor': "59",
			'email': "chernandez@hermecsolutions.com",
		}
		data = {
			'model': "account.invoice",
			'values': json.dumps(values),
			 #'domain': json.dumps([['type', '=', "out_invoice"], ['state', '!=', 'draft']]),
			 #'fields': json.dumps(['number', 'amount_total']),
		}
		response = api.execute('/api/custom/create/vso', data=data)
		for entry in response:
			name = entry.post('name')
			visitor_num = entry.post('visitor')
			email = entry.post('email')
			self.env["muki.rest"].create({'name':name,'visit':visitor_num,'email':email,})
		logging.info(str(response)) """


		# CREATE CUSTOMER
		customer = ''
		if not customer:
			values = {
				'name': "Prueba VSO",
				'visitor_id': "59",
				'email': "chernandez@hermecsolutions.com",
			}
			data = {
				'model': "res.partner",
				'values': json.dumps(values),
				#'domain': json.dumps([['customer_type', '=', "regular"]]),
				#'fields': json.dumps(['name', 'visitor_id', 'email']),
			}
			response = api.execute('/api/custom/create/vso', type="POST", data=data)
			customer = next(iter(response))
		
		# check customer
		# data = {
		# 	'model': "res.partner",
		# 	'domain': json.dumps([['visitor', '=', "23"]]),
		# 	'limit': 1
		# }
		# response = api.execute('/api/custom/search/vso', data=data)
		# customer = next(iter(response), False)
		
		
		# data = {
		# 	'model': "account.invoice",
		# 	'domain': json.dumps([['type', '=', "out_invoice"], ['state', '!=', 'draft']]),
		# 	'fields': json.dumps(['number', 'amount_total']),
		# }
		# response = api.execute('/api/search_read', data=data)
		# for entry in response:
		# 	number = entry.get('number')
		# 	total = entry.get('amount_total')
		# 	self.env["muki.rest"].create({'name':number,'amount':total})
		# logging.info(str(response))


		"""
		# sampel query
		data = {
			'model': "res.partner",
			'domain': json.dumps([['parent_id.name', '=', "Azure Interior"]]),
			'fields': json.dumps(['name', 'image_small']),
		}
		response = api.execute('/api/search_read', data=data)
		for entry in response:
			entry['image_small'] = entry.get('image_small')[:5] + "..."
		logging.info(str(response))

		# check customer
		data = {
			'model': "res.partner",
			'domain': json.dumps([['name', '=', "Sample Customer"]]),
			'limit': 1
		}
		response = api.execute('/api/search', data=data)
		customer = next(iter(response), False)

		# create customer
		if not customer:
			values = {
				'name': "Sample Customer",
			}
			data = {
				'model': "res.partner",
				'values': json.dumps(values),
			}
			response = api.execute('/api/create', type="POST", data=data)
			customer = next(iter(response))

		# create product
		values = {
			'name': "Sample Product",
		}
		data = {
			'model': "product.template",
			'values': json.dumps(values),
		}
		response = api.execute('/api/create', type="POST", data=data)
		product = next(iter(response))

		# create order
		values = {
			'partner_id': customer,
			'state': 'sale',
			'order_line': [(0, 0, {'product_id': product})],
		}
		data = {
			'model': "sale.order",
			'values': json.dumps(values),
		}
		response = api.execute('/api/create', type="POST", data=data)
		order = next(iter(response))
		"""


