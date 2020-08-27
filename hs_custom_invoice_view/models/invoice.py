# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class InvoiceInherit2(models.Model):
	_inherit = 'account.invoice'
	# _inherit = ['todo.task', 'mail.thread']

	# is_fund = fields.Boolean(string="Is Fund")
	
	note =  fields.Char(string='Description')
	hs_journal = fields.Char(compute='_compute_journal_id', string='Journal', store=True)

	@api.multi
	def update_status_meal_card(self):
		lines = self.env['account.invoice.line'].search([('invoice_id', '=', self.id)])
		if lines:
			lines.write({'hs_state':self.state})
	
	@api.depends('journal_id') 
	def _compute_journal_id(self):
		for invoice in self:
			invoice.hs_journal = invoice.journal_id.name

class accountPaymentInherit(models.Model):
	_inherit = 'account.payment'

	#    diario  = fields.Char(string='Invoice Journal', related='partner_id.invoice_ids.hs_journal')
	diario = fields.Char(compute='_compute_journal_name', string='Invoice Journal', store=True)

	@api.depends('invoice_ids.hs_journal') 
	def _compute_journal_id(self):
		for invoice in self:
			invoice.diario = invoice.invoice_ids.hs_journal
