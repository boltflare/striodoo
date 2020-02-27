# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime
from dateutil import tz


import logging
_logger = logging.getLogger(__name__)


class accountInvoiceInherit2(models.Model):
	_inherit = "account.invoice"


	class_code = fields.Many2one("class.code", "Class Code")
	customer_is_fund = fields.Boolean(string="Is Customer Fund?", compute="_customer_is_fund", default=False)
	#btn_credit_note = fields.Boolean(compute="_compute_btn_credit_note", string="Activar button credit note")
	fund_project_id = fields.Char(string="Project ID", compute="_compute_fund_project_id")

	@api.depends('partner_id')
	def _customer_is_fund(self):
		# self.customer_is_fund = True if self.partner_id.customer_type == 'fund' else False
		for invoice in self:
			customer_type = invoice.partner_id.customer_type
			invoice.customer_is_fund = True if customer_type == 'fund' else False


	@api.depends('customer_is_fund')
	def _compute_fund_project_id(self):
		try:
			for invoice in self:
				invoice.fund_project_id = invoice.partner_id.stri_project
		except Exception as __ERROR:
			pass

	"""
	@api.depends('type')
	def _compute_btn_credit_note(self):
		for invoice in self:
			from_zone = tz.gettz('UTC')
			to_zone = tz.gettz('America/Panama')
			utc = datetime.now(from_zone)
			date_current = utc.astimezone(to_zone)


			date_invoice = invoice.
	"""