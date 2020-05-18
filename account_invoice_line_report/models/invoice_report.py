# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceReport(models.Model):
	# _name= 'invoice.view'
	_inherit = 'account.invoice.report'
	# _description = 'Account Invoice View'

	# class_code = fields.Many2one("class.code", "Class Code")
	property_account_income_id = fields.Many2one('account.account', string='Department', readonly=True)
	# hs_quantity = fields.Float(string='Quantity', related='invoice_id.quantity', store=True)
	stri_chartfield = fields.Char('account.account', string='Fund', readonly=True)


	
	
	# @api.depends('invoice_id.state')
	# def _get_default_state(self):
	# 	for invoice in self:
	# 		invoice.hs_state = invoice.invoice_id.state in ['open', 'paid']

	