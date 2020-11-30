# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)


class SaleInherit(models.Model):
	_inherit = "sale.order"


	required_invoice = fields.Boolean("Invoice Required", default=True)
