# -*- coding: utf-8 -*-
from . import library
import json
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class InvoiceReport(models.Model):
	# _name= 'invoice.view'
	_inherit = 'account.invoice.report'
	# _description = 'Account Invoice View'
	# init API
	# api = library.RestAPI()
	# api.authenticate()

	# test API
	# logging.info(str(api.execute('/api')))
	# logging.info(str(api.execute('/api/user')))

	def action_muki_connect(self):
		api = library.RestAPI()
		api.authenticate()
		logging.info(str(api.execute('/api')))
		logging.info(str(api.execute('/api/user')))

	# hs_fund = fields.Char(string='Fund Code', related='invoice_id.stri_fund', store=True)
	# hs_budget = fields.Char(string='Budget Reference', related='invoice_id.stri_budget', store=True)
	# hs_desig = fields.Char(string='Designated Code', related='invoice_id.stri_desig', store=True)
	# hs_dept = fields.Char(string='Department ID', related='invoice_id.stri_dept', store=True)
	# hs_account = fields.Char(string='Account', related='invoice_id.stri_account', store=True)
	# hs_class = fields.Char(string='Class Field', related='invoice_id.stri_class', store=True)
	# hs_program = fields.Char(string='Program Code', related='invoice_id.stri_program', store=True)

	# hs_project = fields.Char(string='Project ID', related='invoice_id.stri_project', store=True)
	# hs_activity = fields.Char(string='Activity Code', related='invoice_id.stri_activity', store=True)
	# hs_type = fields.Selection(string='Type', related='invoice_id.stri_type', store=True)
	
	# chartfield = fields.Char(string='Chartfield', compute='_compute_hs_chartfield')
	# chartfield = fields.Char(string='ChartField', related='invoice_id.stri_chartfield', store=True)
	# self._cr.execute('select * from res_partner')

	# for res in self.env.cr.fetchall():

	# print(res)
	# @api.depends('hs_fund', 'hs_budget', 'hs_desig', 'hs_dept', 'hs_account', 'hs_class', 'hs_program', 'hs_project', 'hs_activity', 'hs_type')
	# def _compute_hs_chartfield(self):
	# 	resp = str(self.hs_fund) if self.hs_fund else ""

	# 	resp = resp + "," + str(self.hs_budget) if self.hs_budget \
	# 		else resp + ","
		
	# 	resp = resp + "," + str(self.hs_desig) if self.hs_desig \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_dept) if self.hs_dept \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_account) if self.hs_account \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_class) if self.hs_class \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_program) if self.hs_program \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_project) if self.hs_project \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_activity) if self.hs_activity \
	# 		else resp + ","

	# 	resp = resp + "," + str(self.hs_type) if self.hs_type \
	# 		else resp + ","

	# 	self.chartfield = resp
			
	

	

	