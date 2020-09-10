# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


import logging
_logger = logging.getLogger(__name__)


class TransactionInherit(models.Model):
	_inherit = "payment.transaction"