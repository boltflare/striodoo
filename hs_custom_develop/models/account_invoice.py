# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class AccountInvoiceInherit3(models.Model):
	_inherit = 'account.invoice'

	charfield_project = fields.Char(string="Project ID", compute="compute_project_id")


	@api.depends('partner_id')
	def compute_project_id(self):
		for invoice in self:
			partner = invoice.partner_id
			if partner.customer_type == 'fund':
				invoice.charfield_project = partner.stri_project
