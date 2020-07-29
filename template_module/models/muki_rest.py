# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class MukiREST(models.Model):
	_name = "muki.rest"
	_description = "Visitor Search"

	hstatus = fields.Selection([
		('Check-OUT', 'Check-OUT'),
		('Cancelled', 'Cancelled'),
		('Declined', 'Declined'),
		('Draft', 'Draft'),
		('Revision', 'Revision'),
		('Check-IN', 'Check-IN'),
		('Approved', 'Approved'),
		('Submit', 'Submit')],string = 'Status')
	visitor_name = fields.Char("Name")
	name = fields.Char("First Name")
	last_name = fields.Char("Last Name")
	visitor_email = fields.Char("Email")
	visitor = fields.Char("Visitor ID")

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
            record.visitor = self.visitor