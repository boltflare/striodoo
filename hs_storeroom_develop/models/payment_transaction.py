# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


import logging
_logger = logging.getLogger(__name__)


class PaymentTransactionInherit(models.Model):
	_inherit = "payment.transaction"

	
	def update_sale_order(self, orders):
		for order in orders:
			if order.strifund:
				sale_order = self.env['sale.order'].sudo().browse(order.id)
				filter_query = [('partner_id', '=', sale_order.partner_id.id)]
				user = self.env['res.users'].sudo().search(filter_query, limit=1)
				if user:
					sale_order.user_id = user
					
				partner_invoice = order.partner_invoice_id
				partner_shipping = order.partner_shipping_id
				
				sale_order.partner_id = order.strifund
				sale_order.partner_invoice_id = partner_invoice
				sale_order.partner_shipping_id = partner_shipping


	def _transfer_form_validate(self, data):
		if self.sale_order_ids:
			self.update_sale_order(self.sale_order_ids)
		return super(PaymentTransactionInherit, self)._transfer_form_validate(data)
