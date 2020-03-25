# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountInvoiceInherit(models.Model):
	_inherit = "account.invoice"
	people_soft_registered = fields.Boolean("PeopleSoft Registered", default=False)
	"""
	people_soft_categ = fields.Selection(string="People Soft Category", 
		selection=[
			('customer_bci',  'Customer Account BCI'),
			('customer_stri', 'Customer Account STRI'),
			('strifund',      'STRIFUND'),
		])
	"""


	"""
	@api.multi
	def action_invoice_open(self):

		for invoice in self:
			if invoice.partner_id.customer_type == 'fund':
				invoice.people_soft_categ = 'strifund'
			
			elif "stri" in str(invoice.journal_id).lower():
				invoice.people_soft_categ = "customer_stri"
			elif "bci" in str(invoice.journal_id).lower():
				invoice.people_soft_categ = "customer_bci"
			else:
				raise ValidationError(_("La factura no pudo ser categorizada "\
					"para el reporte de People Soft."))
		
		return super(AccountInvoiceInherit, self).action_invoice_open()
	"""
		