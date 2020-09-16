# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class InvoiceInherit2(models.Model):
	_inherit = 'account.invoice'

	hs_journal = fields.Char(compute='_compute_journal_id', string='Journal', store=True)

	@api.depends('journal_id') 
	def _compute_journal_id(self):
		for invoice in self:
			invoice.hs_journal = invoice.journal_id.name

	# pos_invoice = fields.Char(compute='_compute_state_invoice', string='POS Invoice', store=True)
	pos_invoice = fields.Boolean(string="Is_Pos_Invoice", compute="_get_state_invoice")

	@api.depends('journal_id') 
	def _get_state_invoice(self):
		for fac in self:
			fac.pos_invoice = True if self.journal_id.name == 'POS Sale Journal' else False

			# if self.bool_field:
		# self.bool_field = True

	""" @api.depends('origin') 
	def _compute_state_invoice(self):
		for invoice in self:
			invoice.pos_invoice = invoice.origin """



class accountPaymentInherit(models.Model):
	_inherit = 'account.payment'

	diario  = fields.Char(string='Invoice Journal', related='partner_id.invoice_ids.journal_id.name')
	# diario = fields.Char(compute='_compute_journal_name', string='Invoice Journal', store=True)

""" 	@api.depends('invoice_ids.hs_journal') 
	def _compute_journal_name(self):
		for payment in self:
			payment.diario = payment.invoice_ids.hs_journal """