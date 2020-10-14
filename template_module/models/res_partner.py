
from odoo import api, fields, models
import etree

class resPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	visit_category = fields.Char(string='Visitor Category')
	
	@api.model
	def fields_view_get(self, view_id=None, view_type='form',
					toolbar=False, submenu=False):
		result = super(resPartnerInherit2, self).fields_view_get(
		view_id=view_id, view_type=view_type,
		toolbar=toolbar, submenu=submenu)

	# Disabling the import button for users who are not in import group
		if view_type == 'tree':
			doc = etree.XML(result['arch'])
			if not self.env.user.has_group('account.group_account_manager'):
			# When the user is not part of the import group
				for node in doc.xpath("//tree"):
					# Set the import to false
					node.set('import', 'false')
			result['arch'] = etree.tostring(doc)

		return result  

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