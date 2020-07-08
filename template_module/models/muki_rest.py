# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MukiREST(models.Model):
	_name = "muki.rest"
	_description = "Ejemplo Muki Rest"

	name = fields.Char("Nombre")
	amount = fields.Char("Email")
	# visita = fields.Char("Visitor ID")



# class template_module(models.Model):
#     _name = 'template_module.template_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100