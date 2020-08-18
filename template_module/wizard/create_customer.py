# -*- coding: utf-8 -*-
from . import library2
# from . import library2
import json
from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

class CreateCustomer(models.TransientModel):
    _name = 'create.customer'
    _description = 'Create a new visitor on customers'
    
    visitor_name = fields.Char("Name")
    

    """ def update_state(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['sale.order'].browse(active_ids):
            record.state = self.state  """   

    #Funcion para obtener los registros seleccionados
    """ def _get_visitors(self):
        return self.env['muki.rest'].browse(self._context.get('active_ids'))
    logging.info(str(_get_visitors)) """

    def create_visitor(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['muki.rest'].browse(active_ids):
            record.api = library2.RestAPI()
            record.api.authenticate()
            
            # test API
            logging.info(str(api.execute('/api')))
            logging.info(str(api.execute('/api/user')))

            
            #EJEMPLO FUNCIONAL 
            record.response = api.execute('/api/custom/create/customer')
            record.result = record.response['result']
            for entry in record.result:
                nomb = entry.get('nombre')
                correo = entry.get('visitor_email')
                visit = entry.get('hvisit')
                self.env["res.partner"].create({'name':nomb,'email':correo, 'hvisit':visit})
                # self.env["res.partner"].create({'name':number,'hstatus':estado,'email':total,'visitor':visit})
                logging.info(str(record.response))

   
    