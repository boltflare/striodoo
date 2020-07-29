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


	""" @api.one
	def create_add_action(self):
		ActWindowSudo = self.env['ir.actions.act_window'].sudo()
		data_obj = self.env['ir.model.data']
		for action in self.browse(self._ids):
			src_obj = action.model_name.model
			model_data_id = data_obj._get_id('create_visitor_action')
			res_id = data_obj.browse( model_data_id).res_id
			button_name = _('Create (%s)') % action.name
			act_id = ActWindowSudo.create({
				 'name': button_name,
				 'type': 'ir.actions.act_window',
				 'res_model': 'create.customer',
				 'src_model': src_obj,
				 'view_type': 'form',
				'context': "{'visitor' : %d}" % (self.id),
				 'view_mode':'form,tree',
				 'view_id': res_id,
				 'target': 'new',
				 'binding_model_id': action.model_name.id,
				 'auto_refresh':1
			})
			action.write({
				'ref_ir_act_window': act_id.id,
			})
		return True """

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


