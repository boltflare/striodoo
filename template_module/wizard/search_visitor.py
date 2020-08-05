# -*- coding: utf-8 -*-
from odoo import api, fields, models


class searchVisitorWizard(models.TransientModel):
	_name = 'visitor.wizard'
	_description = 'Wizard for Search Visitor STRI'

	status = fields.Selection([
		('Check-OUT', 'Check-OUT'),
		('Cancelled', 'Cancelled'),
		('Declined', 'Declined'),
		('Draft', 'Draft'),
		('Revision', 'Revision'),
		('Check-IN', 'Check-IN'),
		('Approved', 'Approved'),
		('Submit', 'Submit')],string = 'Status')
	visit_name = fields.Char("Name")
	name = fields.Char("First Name")
	last_name = fields.Char("Last Name")
	visit_email = fields.Char("Email")
	visitor = fields.Char("Visitor ID")

	def search_visitor(self):
		active_ids = self._context.get('active_ids', []) or []