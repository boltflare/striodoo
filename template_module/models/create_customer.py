# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CreateCustomer(models.TransientModel):
    _name = 'create.customer'
    _description = 'Create a new visitor on customers'
    
    # state = fields.Selection([
    #     ('draft', 'Quotation'),
    #     ('sent', 'Quotation Sent'),
    #     ('sale', 'Sales Order'),
    #     ('done', 'Locked'),
    #     ('cancel', 'Cancelled'),
    # ], string = 'Status')
    
    def create_visitor(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['muki.rest'].browse(active_ids):
            record.state = self.state