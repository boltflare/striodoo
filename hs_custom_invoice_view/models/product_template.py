# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProductTemplateInherit2(models.Model):
	_inherit = 'product.template', 'product.product'

	# is_fund = fields.Boolean(string="Is Fund")

	item_type =  fields.Selection(string='Item Type',
		selection=[('meal', 'Meal Card'), ('visitor', 'Visitor Program')], 
	    required=True, help='Opción para poder clasificar los productos correspondientes al sistema de Meal Card'
             'Meal Card productos pertenecientes a Administración.\n'
             'Visitor Program productos relacionados a esta categoría.')
    

	# fund_manager = fields.Many2one("fund.manager", "Fund Manager")
	# principal_investigator = fields.Many2one("principal.investigator", "Principal Investigator")

	# regular_companies_id = fields.Many2one("regular.companies", "Company")

    # type = fields.Selection([
    #     ('consu', 'Consumable'),
    #     ('service', 'Service')], string='Product Type', default='consu', required=True,
    #     help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
    #          'A consumable product is a product for which stock is not managed.\n'
    #          'A service is a non-material product you provide.')