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
    def _get_visitors(self):
        return self.env['muki.rest'].browse(self._context.get('active_ids'))
    logging.info(str(_get_visitors))

    def create_visitor(self):
        api = library2.RestAPI()
        api.authenticate()
        
        # test API
        logging.info(str(api.execute('/api')))
        logging.info(str(api.execute('/api/user')))

        
        #EJEMPLO FUNCIONAL 
        response = api.execute('/api/custom/create/customer')
        result = response['result']
        for entry in result:
            nombre = entry.get('visitor_name')
            correo = entry.get('visitor_email')
            visit = entry.get('visitor')
            self.env["res.partner"].create({'name':nombre,'email':correo, 'visitor':visit})
            # self.env["res.partner"].create({'name':number,'hstatus':estado,'email':total,'visitor':visit})
            logging.info(str(response))

   
    