# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

import logging
_logger = logging.getLogger(__name__)


class accountInvoiceInherit2(models.Model):
	_inherit = "account.invoice"


	class_code = fields.Many2one("class.code", "Class Code")
	customer_is_fund = fields.Boolean(string="Is Customer Fund?", compute="_customer_is_fund", default=False)

	@api.depends('partner_id')
	def _customer_is_fund(self):
		# self.customer_is_fund = True if self.partner_id.customer_type == 'fund' else False
		for invoice in self:
			customer_type = invoice.partner_id.customer_type
			invoice.customer_is_fund = True if customer_type == 'fund' else False


	@api.onchange('invoice_line_ids')
	def _onchange_invoice_line(self):
		_logger.info("Metodo on Change llamado:  ")





class AccountInvoiceLine(models.Model):
	_inherit = "account.invoice.line"


	@api.multi
	def create(self, values):
		overwrite = super(AccountInvoiceLine, self).create(values)
		_logger.info("value of write is:  " + str(values))
		return overwrite

