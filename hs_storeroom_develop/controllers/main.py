# -*- coding: utf-8 -*-
import json
import logging
from odoo import fields, http, tools, _
from odoo.http import request
from werkzeug.exceptions import Forbidden, NotFound
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import WebsiteSale, WebsiteSaleForm
# from odoo.addons.website_form.controllers.main import WebsiteForm

_logger = logging.getLogger(__name__)

class WebsiteSaleFormInherit(WebsiteSaleForm):

	@http.route('/website_form/shop.sale.order', type='http', auth="public", methods=['POST'], website=True)
	def website_form_saleorder(self, **kwargs):
		logging.info("Entro en website_form_saleorder")
		if kwargs.get('strifund'):
			order = request.website.sale_get_order()
			order.write({
				'strifund': int(kwargs.get('strifund'))
			})
		return super(WebsiteSaleFormInherit, self).website_form_saleorder(**kwargs)



class WebsiteSaleInherit(WebsiteSale):

	@http.route(['/shop/extra_info'], type='http', auth="public", website=True, sitemap=False)
	def extra_info(self, **post):
		logging.info("Entro en extra_info")
		super(WebsiteSaleInherit, self).extra_info(**post)
		
		# Check that this option is activated
		extra_step = request.website.viewref('website_sale.extra_info_option')
		if not extra_step.active:
			return request.redirect("/shop/payment")

		# check that cart is valid
		order = request.website.sale_get_order()
		redirection = self.checkout_redirection(order)
		if redirection:
			return redirection

		# if form posted
		if 'post_values' in post:
			values = {}
			for field_name, field_value in post.items():
				if field_name in request.env['sale.order']._fields and field_name.startswith('x_'):
					values[field_name] = field_value
			if values:
				order.write(values)
			return request.redirect("/shop/payment")

		values = {
			'website_sale_order': order,
			'post': post,
			'escape': lambda x: x.replace("'", r"\'"),
			'partner': order.partner_id.id,
			'order': order,
		}

		if 'search' in post:
			filter_search = post.get('search')
			sale_order = request.env['sale.order'].sudo().browse(order.id)
			fund_partners = sale_order.search_partner_fund(filter_search)
			values['funds'] = fund_partners 
			values['search'] = post.get('search')

		return request.render("website_sale.extra_info", values)
		

	@http.route('/shop/payment/validate', type='http', auth="public", website=True, sitemap=False)
	def payment_validate(self, transaction_id=None, sale_order_id=None, **post):
		logging.info("Entro en payment_validate")
		transaction = super(WebsiteSaleInherit, self).payment_validate(
			transaction_id=transaction_id, 
			sale_order_id=sale_order_id, 
			**post
		)
		sale_order_id = request.session.get('sale_last_order_id')
		if sale_order_id:
			order = request.env['sale.order'].sudo().browse(sale_order_id)
			order.update_storeroom_order()
		return transaction


	@http.route(['/shop/confirmation'], type='http', auth="public", website=True, sitemap=False)
	def payment_confirmation(self, **post):
		logging.info("Entro en payment_confirmation")
		transaction = super(WebsiteSaleInherit, self).payment_confirmation(**post)
		sale_order_id = request.session.get('sale_last_order_id')
		if sale_order_id:
			order = request.env['sale.order'].sudo().browse(sale_order_id)
			order.update_storeroom_order()
		return transaction