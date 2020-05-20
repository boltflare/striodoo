# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceReport(models.Model):
	# _name= 'invoice.view'
	_inherit = 'account.invoice.report'
	# _description = 'Account Invoice View'

	# class_code = fields.Many2one("class.code", "Class Code")
	property_account_income_id = fields.Many2one('account.account', string='Income Account', compute='_compute_hs_income', readonly=True, store=True)
	# hs_quantity = fields.Float(string='Quantity', related='invoice_id.quantity', store=True)
	stri_chartfield = fields.Char('account.account', string='Char Field', readonly=True)
	# chartfield = fields.Char(string='ChartField', related='id.stri_chartfield', store=True)

	@api.depends('invoice_id', 'product_id')
	def _compute_hs_income(self):
		for item in self:
			line = self.env['account.invoice.line'].search([('invoice_id', '=', item.invoice_id.id),('product_id', '=', item.product_id.id)], limit=1)
			item.property_account_income_id = line.account_id
			
	# _depends = {
	# 	'account.account': [
	# 		'property_account_income_id', 'stri_chartfield', 
	# 	],
	# }
	# def _select(self):
	# 	select_str = """
	# 		SELECT sub.property_account_income_id, sub.stri_chartfield
	# 	"""
	# 	return select_str

	# def _sub_select(self):
	# 	select_str = """
	# 			SELECT aa.property_account_income_id,
	# 				aa.stri_chartfield
	# 	"""
	# 	return select_str

	

	