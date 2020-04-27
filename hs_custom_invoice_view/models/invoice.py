# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class InvoiceInherit2(models.Model):
	_inherit = 'account.invoice'
    # _inherit = ['todo.task', 'mail.thread']

	# is_fund = fields.Boolean(string="Is Fund")

	note =  fields.Char(string='Description')

    

    
