# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ResPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	# is_fund = fields.Boolean(string="Is Fund")

	customer_type =  fields.Selection(string='Customer Type',
		selection=[('regular', 'Regular'), ('fund', 'Fund')], 
		default="regular")

	fund_manager = fields.Many2one("fund.manager", "Fund Manager")
	principal_investigator = fields.Many2one("principal.investigator", "Principal Investigator")

	regular_companies_id = fields.Many2one("regular.companies", "Company")


	@api.onchange('customer_type')
	def _on_change_customer_type(self):
		if self.customer_type == "regular":
			self.company_type = "person"
		else:
			self.company_type = "company"