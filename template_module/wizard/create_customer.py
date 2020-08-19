# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

# import logging
# _logger = logging.getLogger(__name__)

class CreateCustomer(models.TransientModel):
	_name = 'create.customer'
	_description = 'Create a new visitor on customers'
	
	#EN ESTE METODO SE OBTIENE LOS REGISTROS CON EL CHECK ACTIVO, RECORRO LA VISTA Y CREO EN CLIENTES EL REGITRO SELECCIONADO
	def create_customer(self):
		active_ids = self._context.get('active_ids', []) or []
		for record in self.env['muki.rest'].browse(active_ids):
			# record.nombre = self.env['muki.rest'].search([('nombre', '=', self.nombre)])
			self.env["res.partner"].create({'name':record.nombre,'visitor':record.hvisit,'email':record.visitor_email})

		self.env["muki.rest"].search([()]).unlink()   

			
		
   
	