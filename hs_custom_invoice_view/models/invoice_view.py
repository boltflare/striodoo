# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceView(models.Model):
	_name= 'invoice.view'
	#_inherit = 'account.invoice'
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

	# class_code = fields.Many2one("class.code", "Class Code")
	number = fields.Char(string='Invoice #')
	quantity = fields.Float(string='Quantity')
	date = fields.Date(string='Invoice Date')
	product_id = fields.Char("Item Code") #debo cambiarlo que sea tipo char
	# item = fields.Char (related='item_type.item')
	item= fields.Many2one("product.template", "Item Type")
	partner_id = fields.Char(string='Customer')
	total = fields.Float(string='Total')
	note = fields.Char(string='Description')

	
	# item_food = fields.Boolean(string="Is item food?", compute="_item_type", default=False)

	# @api.depends('partner_id')
	# def _item_type(self):
	# 	# self.customer_is_fund = True if self.partner_id.customer_type == 'fund' else False
	# 	for invoice in self:
	# 		customer = invoice.partner_id.customer
	# 		invoice.item_food = True if customer == True else False
	
	# @api.depends('item_type')
	# def _item_type(self):
	# 	# self.customer_is_fund = True if self.partner_id.customer_type == 'fund' else False
	# 	for invoice in self:
	# 		customer_type = invoice.partner_id.customer_type
	# 		invoice.customer_is_fund = True if customer_type == 'fund' else False

	
