# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class InvoiceInherit2(models.Model):
	_inherit = 'account.invoice'
	# _inherit = ['todo.task', 'mail.thread']

	# is_fund = fields.Boolean(string="Is Fund")
	#CAMPO PARA SOBRESCRIBIR EL CAMPO DE FECHA
	date_invoice = fields.Date(string='Invoice Date',
        readonly=True, states={'draft': [('readonly', False)]}, default = fields.Date.context_today, index=True,
        help="Keep empty to use the current date", copy=False)

	note =  fields.Char(string='Description')

	@api.multi
	def update_status_meal_card(self):
		lines = self.env['account.invoice.line'].search([('invoice_id', '=', self.id)])
		if lines:
			lines.write({'hs_state':self.state})
	
