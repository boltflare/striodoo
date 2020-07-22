# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MukiREST(models.Model):
	_name = "muki.rest"
	_description = "Visitor Search"

	hstatus = fields.Char("Status")
	visitor_name = fields.Char("Name")
	visitor_email = fields.Char("Email")
	visitor = fields.Char("Visitor_id")

