# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResPartnerInherit(models.Model):
	_inherit = 'res.partner'
	only_pos = fields.Boolean("Visible solo en PoS", 
		required=True, default=False)


	@api.model
	def create_from_ui(self, partner):
		partner_id = super(ResPartnerInherit, self).create_from_ui(partner)
		self.browse(partner_id).write({
			'only_pos' : True
		})
		return partner_id