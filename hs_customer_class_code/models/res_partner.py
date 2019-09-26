# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ResPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	is_fund = fields.Boolean(string="Is Fund")

	fund_manager = fields.Char("Fund Manager")
	principal_investigator = fields.Char("Principal Investigator")