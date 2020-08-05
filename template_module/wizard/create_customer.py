# -*- coding: utf-8 -*-
from . import library
# from . import library2
import json
from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

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

    def create_visitor(self):
        api = library.RestAPI()
        api.authenticate()
        
        # test API
        logging.info(str(api.execute('/api')))
        logging.info(str(api.execute('/api/user')))

        #EJEMPLO FUNCIONAL 
        response = api.execute('/api/custom/create/customer')
        result = response['result']
        for entry in result:
            # estado = entry.get('hstatus')
            nombre = entry.get('visitor_name')
            correo = entry.get('visitor_email')
            visit = entry.get('visitor')
            self.env["res.partner"].create({'name':nombre,'email':correo, 'visitor':visit})
            # self.env["res.partner"].create({'name':number,'hstatus':estado,'email':total,'visitor':visit})
            logging.info(str(response))

    """ @api.multi
    def create_visitor(self):

        /api/custom/create/customer

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
        return action_vals """

    