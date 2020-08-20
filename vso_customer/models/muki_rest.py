# -*- coding: utf-8 -*-

from . import library
import json
from odoo import models, fields, api


import logging
_logger = logging.getLogger(__name__)

class MukiREST(models.Model):
	_name = "muki.rest"
	_description = "Ejemplo Muki Rest"

	name = fields.Char("Customer")
	email = fields.Char("Email")
	visitor_num = fields.Char("Visitor ID")

def action_muki_connect(self):
		# init API
		api = library.RestAPI()
		api.authenticate()

		
		# test API
		logging.info(str(api.execute('/api')))
		logging.info(str(api.execute('/api/custom/search_create/vso')))

		# create customer
		if not customer:
			values = {
				'name': "Sample Customer",
			}
			data = {
				'model': "res.partner",
				'values': json.dumps(values),
			}
			response = api.execute('/api/custom/create/vso', type="POST", data=data)
			customer = next(iter(response))

# class template_module(models.Model):
#     _name = 'template_module.template_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100