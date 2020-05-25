# -*- coding: utf-8 -*-
from . import library
import json
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class InvoiceReport(models.Model):
	# _name= 'invoice.view'
	_inherit = 'account.invoice.report'

	test= fields.Char(compute='action_muki_connect')

	def action_muki_connect(self):
		api = library.RestAPI()
		api.authenticate()
		# logging.info(str(api.execute('/api')))
		account_line_info =api.execute('/api/read/account.invoice.report?ids=%5B375%5D&fields=%27number%27%2C%27id%27%2C%27account_line_id%27')
		for info in account_line_info:
			all_account_line_id = info.get('account_line_id')
		logging.info('ACCOUNT LINE ID:' + str(all_account_line_id[0]))
		
		chartfield_info =api.execute('/api/read/account.account?ids=%5B'+ str(all_account_line_id[0]) +'%5D&fields=%27id%27%2C%27stri_chartfield%27')
		for stri in chartfield_info:
			all_chartfield = stri.get('stri_chartfield')
		logging.info('CHARTFIELD:' + str(all_chartfield))