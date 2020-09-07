# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


import logging
_logger = logging.getLogger(__name__)


class SaleOrderInherit(models.Model):
	_inherit = "sale.order"


	strifund = fields.Many2one('res.partner', 'Fund')


	def search_partner_fund(self, filter):
		query_text = """SELECT id, name FROM res_partner 
		WHERE customer_type = 'fund' 
		AND (lower(name) LIKE '%{}%' OR lower(stri_project) LIKE '%{}%');
		""".format(str(filter).lower(), str(filter).lower())
		self.env.cr.execute(query_text)
		results = self.env.cr.fetchall()
		logging.info(results)
		return results
		# docids = [item[0] for results]
		#return self.env['res.partner'].sudo().search(docids)


	def update_storeroom_order(self):
		logging.info("Entro en update_storeroom_order")
		if self.strifund:
			logging.info("---Strifund Encontrado---")
			# sale_order = self.env['sale.order'].sudo().browse(order_id)
			filter_query = [('partner_id', '=', self.partner_id.id)]
			user = self.env['res.users'].sudo().search(filter_query, limit=1)
			logging.info(user)
			if user:
				self.user_id = user
			self.partner_id = self.strifund
			self.partner_invoice_id = self.strifund
			self.partner_shipping_id = self.strifund
			
		