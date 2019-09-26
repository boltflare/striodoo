# -*- coding: utf-8 -*-

from odoo import models, fields

class ClassCode (models.Model):
    _name= 'class.code'

    # _inherit = 'account.invoice'
   
    name = fields.Char (string = 'Name', required = True)
    code = fields.Char (string = 'Code', required = True)
	