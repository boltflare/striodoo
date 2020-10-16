
from odoo import api, fields, models

class resPartnerInherit2(models.Model):
	_inherit = 'res.partner'

	visit_category = fields.Char(string='Visitor Category')
	