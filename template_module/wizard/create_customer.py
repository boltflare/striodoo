# -*- coding: utf-8 -*-
# from . import library2
# import json
from odoo import models, fields, api, _

# import logging
# _logger = logging.getLogger(__name__)

class CreateCustomer(models.TransientModel):
    _name = 'create.customer'
    _description = 'Create a new visitor on customers'
    

    """ def update_state(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['sale.order'].browse(active_ids):
            record.state = self.state  """   

    #Funcion para obtener los registros seleccionados
    """ def _get_visitors(self):
        return self.env['muki.rest'].browse(self._context.get('active_ids')) """
    
    def create_customer(self):
        # context = dict(self._context or {})
        # active = self.env['muki.rest'].browse(context.get('active_ids'))
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['muki.rest'].browse(active_ids):
            record.nombre = self.nombre
            record.visitor_email = self.visitor_email
            record.hvisit = self.hvisit
            self.env["res.partner"].create({'name':record.nombre,'email':record.visitor_email, 'visitor':record.hvisit})

"""  def create_visitor(self):
        # active_ids = self._context.get('active_ids', []) or []
       
        api = library2.RestAPI()
        api.authenticate()
                
        # test API
        logging.info(str(api.execute('/api')))
        logging.info(str(api.execute('/api/user')))

                
        #EJEMPLO FUNCIONAL 
        response = api.execute('/api/custom/create/customer')
        logging.info(str(response))

        result = response['result']
        for entry in result:
            nomb = entry.get('nombre')
            correo = entry.get('visitor_email')
            visit = entry.get('hvisit')
            for record in self.env['muki.rest'].browse(self._context.get('active_ids')):
                record.create = self.env["res.partner"].create({'name':nomb,'email':correo, 'visitor':visit}) """
            
        # return self.env['muki.rest'].browse(self._context.get('active_ids'))
            
        
   
    