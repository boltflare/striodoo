# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


import logging
_logger = logging.getLogger(__name__)

class AcquirerInherit(models.Model):
	_inherit = "payment.acquirer"

	category = fields.Selection(selection=[
		('sale', 'Ecommerce'), ('invoice', 'Invoice')
	], string='Category', default='sale')