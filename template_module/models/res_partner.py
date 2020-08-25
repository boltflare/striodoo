from . import library
import json
from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class UpdateCustomer(models.Model):
	_inherit = 'res.partner'

	def action_update_customer(self):
		# init API
		api = library.RestAPI()
		api.authenticate()

		# test API
		logging.info(str(api.execute('/api')))
		logging.info(str(api.execute('/api/user')))

		# Update customer
		values = {
			
			'email': "alextrillo@outlook.com",
		}
		data = {
		 	'model': "res.partner",
			'values': json.dumps(values),
		 	'domain': json.dumps([['visitor', '=', '1708']]),
		}
		response = api.execute('/api/custom/update/customer', type="PUT", data=data)
		logging.info(str(response))
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