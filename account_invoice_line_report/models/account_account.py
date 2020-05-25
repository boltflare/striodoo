# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountInherit(models.Model):
	# _name= 'invoice.view'
	_inherit = 'account.account'

	# @api.multi
	# def get_chartfield(self):
	# 	lines = self.env['account.account'].search([('invoice_id', '=', self.id)])
	# 	if lines:
	# 		lines.write({'chartfield':self.stri_chartfield})