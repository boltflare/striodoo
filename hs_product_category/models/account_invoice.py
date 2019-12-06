# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions

import logging
_logger = logging.getLogger(__name__)


class accountInvoiceInherit2(models.Model):
	_inherit = "account.invoice"


	@api.onchange('invoice_line_ids')
	def _onchange_invoice_line(self):
		try:
			for invoice_line in self.invoice_line_ids:
				product = invoice_line.product_id
				_logger.info(product.name)
				journals = self.env["account.journal"].search([('type', '=', 'sale')])
				journal = journals.filtered(lambda l: l.department_ids == product.categ_id)
				self.journal_id = journals
				_logger.info("El journal encontrado es: " + journal.name)
				break
		except Exception as error:
			raise exceptions.ValidationError("No se encontraron cuentas por cobrar para el \
				producto ingreado: " + str(error))





class AccountInvoiceLine(models.Model):
	_inherit = "account.invoice.line"


	@api.multi
	def create(self, values):
		overwrite = super(AccountInvoiceLine, self).create(values)
		_logger.info("value of write is:  " + str(values))
		return overwrite