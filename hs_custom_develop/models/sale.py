# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)


class SaleInherit(models.Model):
	_inherit = "sale.order"


	required_invoice = fields.Boolean("Invoice Required", default=True)


	@api.onchange('order_line')
	def _on_change_order_line(self):
		for line in self.order_line:
			if line.product_id:
				product = line.product_id
				if self.required_invoice == True and product.type == "product":
					product.sudo().write({'invoice_policy': 'order'})