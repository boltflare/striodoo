# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProductTemplateInherit2(models.Model):
	_inherit = 'product.template'

	visit_categ =  fields.Selection(string='Visitor Category',
		selection=[('A', 'A'), ('B', 'B'), ('C', 'C')], 
		help='Opción para poder clasificar los productos correspondientes a la categoria del visitante')


class ProductInherit1(models.Model):
	_inherit = 'product.product'
	

	visit_categ =  fields.Selection(string='Visitor Category',
		selection=[('A', 'A'), ('B', 'B'), ('C', 'C')], 
		help='Opción para poder clasificar los productos correspondientes a la categoria del visitante')
