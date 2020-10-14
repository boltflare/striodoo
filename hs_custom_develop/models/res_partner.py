# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)


class ResPartnerInherit(models.Model):
	_inherit = "res.partner"


	@api.multi
	def write(self, values):
		"""Sobreescribimos el metodo write para poner por default en
		el pais Panamá
		"""
		override = super(ResPartnerInherit, self).write(values)
		for partner in self:
			if not partner.country_id:
				country = self.env.ref('base.pa')
				partner.country_id = country
		return override