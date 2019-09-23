# -*- coding: utf-8 -*-

from odoo import models, fields


class accountInvoiceInherit2(models.Model):
	_inherit = "account.invoice"


	class_code = fields.Many2one("class.code", "Class Code")