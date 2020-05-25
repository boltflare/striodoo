# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceReport(models.Model):
	# _name= 'invoice.view'
	_inherit = 'account.invoice.report'
	# _description = 'Account Invoice View'

	# class_code = fields.Many2one("class.code", "Class Code")
	#property_account_income_id = fields.Many2one('account.account', string='Income Account', compute='_compute_hs_income', readonly=True, store=True)
	# hs_quantity = fields.Float(string='Quantity', related='invoice_id.quantity', store=True)
	
	hs_fund = fields.Char(string='Fund Code', related='product_id.stri_fund', store=True)
	hs_budget = fields.Char(string='Budget Reference', related='product_id.stri_budget', store=True)
	hs_desig = fields.Char(string='Designated Code', related='product_id.stri_desig', store=True)
	hs_dept = fields.Char(string='Department ID', related='product_id.stri_dept', store=True)
	hs_account = fields.Char(string='Account', related='product_id.stri_account', store=True)
	hs_class = fields.Char(string='Class Field', related='product_id.stri_class', store=True)
	hs_program = fields.Char(string='Program Code', related='product_id.stri_program', store=True)

	hs_project = fields.Char(string='Project ID', related='product_id.stri_project', store=True)
	hs_activity = fields.Char(string='Activity Code', related='product_id.stri_activity', store=True)
	hs_type = fields.Selection(string='Type', related='product_id.stri_type', store=True)
	
	chartfield = fields.Char(string='Chartfield', compute='_compute_hs_chartfield')
	# chartfield = fields.Char(string='ChartField', related='id.stri_chartfield', store=True)

	@api.depends('hs_fund', 'hs_budget', 'hs_desig', 'hs_dept', 'hs_account', 'hs_class', 'hs_program', 'hs_project', 'hs_activity', 'hs_type')
	def _compute_hs_chartfield(self):
		resp = str(self.hs_fund) if self.hs_fund else ""

		resp = resp + "," + str(self.hs_budget) if self.hs_budget \
			else resp + ","
		
		resp = resp + "," + str(self.hs_desig) if self.hs_desig \
			else resp + ","

		resp = resp + "," + str(self.hs_dept) if self.hs_dept \
			else resp + ","

		resp = resp + "," + str(self.hs_account) if self.hs_account \
			else resp + ","

		resp = resp + "," + str(self.hs_class) if self.hs_class \
			else resp + ","

		resp = resp + "," + str(self.hs_program) if self.hs_program \
			else resp + ","

		resp = resp + "," + str(self.hs_project) if self.hs_project \
			else resp + ","

		resp = resp + "," + str(self.hs_activity) if self.hs_activity \
			else resp + ","

		resp = resp + "," + str(self.hs_type) if self.hs_type \
			else resp + ","

		self.chartfield = resp
			
	

	

	