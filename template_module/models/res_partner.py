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
			# 'domain': json.dumps([['visitor', '=', '1708']]),
			'values': json.dumps(values),
		}
		response = api.execute('/api/custom/update/customer', type="PUT", data=data)
		logging.info(str(response))
		
		# /api/write
		"""  #EJEMPLO FUNCIONAL 
		response = api.execute('/api/custom/update/customer')
		result = response['result']
		for entry in result:
			nombre = entry.get('name')
			correo = entry.get('email')
			visit = entry.get('visitor')
			self.env["muki.rest"].create({'visitor_name':nombre,'visitor_email':correo, 'visitor':visit})
			# self.env["res.partner"].create({'name':number,'hstatus':estado,'email':total,'visitor':visit})
			logging.info(str(response)) """
		

		#URL: https://demo12.mukit.at/api/write/res.partner?ids=%5B14%5D&values=%7B%27name%27%3A%20%27TEST%20UPDATE%27%7D