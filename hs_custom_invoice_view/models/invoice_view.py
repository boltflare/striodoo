# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceView(models.Model):
	_name= 'invoice.view'
	# _inherit = 'account.invoice'
	# _description = 'Account Invoice View'

	# partner_id = fields.Many2one('res.partner', string='Partner', change_default=True,
    #     readonly=True, states={'draft': [('readonly', False)]},
    #     track_visibility='always', help="You can find a contact by its Name, TIN, Email or Internal Reference.")
	# number = fields.Char(related='move_id.name', store=True, readonly=True, copy=False)
	# quantity = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'),
    #     required=True, default=1)
	# date_invoice = fields.Date(string='Invoice Date',
    #     readonly=True, states={'draft': [('readonly', False)]}, index=True,
    #     help="Keep empty to use the current date", copy=False)
	#  amount_total = fields.Monetary(string='Total',
    #     store=True, readonly=True, compute='_compute_amount')
	# name = fields.Text(string='Description', required=True)
	
	number = fields.Char(string='Invoice #', required = True)
	quantity = fields.Float(string='Quantity', required = True)
	date = fields.Date(string='Invoice Date')
	product_id = fields.Char("Item Code") #debo cambiarlo que sea tipo char
	partner_id = fields.Char(string='Customer', required = True)
	total = fields.Float(string='Total')
	note = fields.Text(string='Description', required=True)


