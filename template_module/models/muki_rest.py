# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MukiREST(models.Model):
	_name = "muki.rest"
	_description = "Visitor Search"

	hstatus = fields.Char("Status")
	name = fields.Char("Name")
	housing = fields.Char("Housing")

