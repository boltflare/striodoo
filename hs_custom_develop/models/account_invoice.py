# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


import logging
_logger = logging.getLogger(__name__)

class AccountInvoiceInherit3(models.Model):
	_inherit = 'account.invoice'

	charfield_project = fields.Char(string="Project ID", compute="compute_project_id")


	@api.depends('partner_id')
	def compute_project_id(self):
		for invoice in self:
			partner = invoice.partner_id
			if partner.customer_type == 'fund':
				invoice.charfield_project = partner.stri_project


	@api.multi
	def action_invoice_open(self):
		action_open = super(AccountInvoiceInherit3, self).action_invoice_open()
		for inv in self:

			if inv.type != 'out_invoice':
				continue

			if inv.partner_id.customer_type == 'regular':
				continue

			Payment = self.env['account.payment'].sudo().with_context(
				default_invoice_ids=[(4, inv.id, False)],
				default_amount = inv.amount_total,
				default_payment_date = fields.Date.today()
			)

			filter_config = 'hs_custom_develop.default_journal_strifund'
			config = self.env['ir.config_parameter'].get_param(filter_config)
			journal = self.env['account.journal'].sudo(True).browse(int(config))
			payment_method = self.env.ref('account.account_payment_method_manual_in')
			if not payment_method:
				raise exceptions.ValidationError('Account configuration '
				'module - Default journal Strifund is empty.') 

			payment = Payment.create({
				'payment_method_id': payment_method.id,
				'payment_type': 'inbound',
				'partner_type': 'customer',
				'partner_id': inv.partner_id.id,
				'journal_id': journal.id,
				'company_id': inv.company_id.id,
				'currency_id': inv.company_id.currency_id.id,
			})
			payment.action_validate_invoice_payment()
		return action_open