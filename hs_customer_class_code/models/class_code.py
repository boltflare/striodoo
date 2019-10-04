# -*- coding: utf-8 -*-

from odoo import models, fields

class ClassCode (models.Model):
    _name= 'class.code'

    # _inherit = 'account.invoice'
   
    name = fields.Char (string = 'Name', required = True)
    code = fields.Char (string = 'Code', required = True)
	
    # @api.multi
    # def name_get(self,cr,uid,ids,context=None):
    #     result = {}
    #     for code in self.browse(cr,uid,ids,context=context):
    #         result[code.id] = code.name + " " + code.code

    #     return result.items()	
