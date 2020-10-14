from . import library
import json
from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class resPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	visitor_categ = fields.Char(string='Visitor Category')
	

	""" # FUNCION PARA HACER UPDATE EN ODOO
	@api.multi
	def update_status_meal_card(self):
		lines = self.env['account.invoice.line'].search([('invoice_id', '=', self.id)])
		if lines:
			lines.write({'hs_state':self.state}) """
		
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