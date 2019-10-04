# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ResPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	# is_fund = fields.Boolean(string="Is Fund")

	customer_type =  fields.Selection(string='Customer Type',
		selection=[('regular', 'Regular'), ('fund', 'Fund')], 
		default="regular")

	fund_manager = fields.Many2one("fund.manager", "Fund Manager", required=True)
	principal_investigator = fields.Char(string = 'Principal Investigator', required = True)