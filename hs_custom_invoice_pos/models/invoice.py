# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class InvoiceInherit2(models.Model):
	_inherit = 'account.invoice'

	hs_journal = fields.Char(compute='_compute_journal_id', string='Journal', store=True)

	@api.depends('journal_id') 
	def _compute_journal_id(self):
		for invoice in self:
			invoice.hs_journal = invoice.journal_id.name

class accountPaymentInherit(models.Model):
	_inherit = 'account.payment'

	diario  = fields.Char(string='Invoice Journal', related='partner_id.invoice_ids.journal_id.name')
	# diario = fields.Char(compute='_compute_journal_name', string='Invoice Journal', store=True)

""" 	@api.depends('invoice_ids.hs_journal') 
	def _compute_journal_name(self):
		for payment in self:
			payment.diario = payment.invoice_ids.hs_journal """