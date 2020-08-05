# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class CreateCustomer(models.TransientModel):
    _name = 'create.customer'
    _description = 'Create a new visitor on customers'
    
    visitor_name = fields.Char("Name")
    
    # def create_visitor(self):
    #     active_ids = self._context.get('active_ids', []) or []
    #     for record in self.env['muki.rest'].browse(active_ids):
    #         record.visitor_name = self.visitor_name
            
    #Funcion para obtener los registros seleccionados
    def _get_visitors(self):
        return self.env['muki.rest'].browse(self._context.get('active_ids'))

    # session_ids = fields.Many2many('muki.rest',
    #     string="Sessions", required=True, default=_default_sessions)
    # attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def create_visitor(self):
        customer = self.env['res.partner']
        customers = customer
        for visitor_vals in self._get_visitors():
            customers += customer.create(visitor_vals)
        customers.post()

        action_vals = {
            'name': _('customers'),
            'domain': [('id', 'in', customers.ids)],
            'view_type': 'form',
            'res_model': 'res.partner',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }
        return action_vals

    