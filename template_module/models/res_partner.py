# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.osv import expression

class ResPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	visitor = fields.Char(string='Visitor ID')
	_sql_constraints = [
        ('visitor_uniq', 'unique(visitor)', "Visitor ID can only be assigned to one customer !"),
    ]