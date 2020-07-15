# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ClassCode (models.Model):
    _name= 'class.code'
    _description = 'Modulo para administrar Class Code'

    # _inherit = 'account.invoice'
   
    name = fields.Char (string = 'Name', required = True)
    code = fields.Char (string = 'Code', required = True)

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            record_name = '[' + record.code + '] ' + record.name
            result.append((record.id, record_name))
        return result

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if context.has_key('class_search'):
            domain = [('code', 'operator', value)]
            ids = self.search(domain)
        else:
            return super(ClassCode, self).name_search(cr, user, name, args=args, operator='ilike', context=context, limit=limit)
        return self.name_get(cr, uid, ids, context)