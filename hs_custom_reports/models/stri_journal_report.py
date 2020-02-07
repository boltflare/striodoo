# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api
from odoo.tools.translate import _
from odoo.tools.misc import formatLang

class InheritStriJournalReport(models.AbstractModel):
	_inherit = 'account.report'
	_name = 'account.stri.journal.report'
	_description = 'STRi Journal Report'


	filter_date = {'date_from': '', 'date_to': '', 'filter': 'this_month'}
	filter_comparison = {'date_from': '', 'date_to': '', 'filter': 'no_comparison', 'number_period': 1}

	def _get_columns_name(self, options):
		columns = [
			{},
			{'name': _('Fund Code')},
			{'name': _('Budget Reference'), 'class': 'number'},
			{'name': _('Designated Code')},
			{'name': _('Department ID')},
			{'name': _('Account')},
			{'name': _('Program Code')},
			{'name': _('Project ID')},
			{'name': _('Activity Code')},
			{'name': _('Type')},
			{'name': _('Amount')},
			{'name': _('Date'), 'class': 'date'}]

		return columns


	def _get_templates(self):
		templates = super(ReportPartnerLedger, self)._get_templates()
		templates['line_template'] = 'account_reports.line_template_journal_report'
		return templates


	def _set_context(self, options):
		ctx = super(InheritStriJournalReport, self)._set_context(options)
		ctx['strict_range'] = True
		return ctx


	def _group_by_invoice_id(self, options, line_id):
		invoices = {}
		pass


	@api.model
	def _get_lines(self, options, line_id=None):
		
		"""
		offset = int(options.get('lines_offset', 0))
		lines = []
		context = self.env.context
		company_id = context.get('company_id') or self.env.user.company_id
		if line_id:
			line_id = int(line_id.split('_')[1]) or None
		"""

		total_columns = ['', '', '', '', '', '', '', '', '', '', '']
		lines.append({
			'id': 'grouped_partners_total',
			'name': _('Total'),
			'level': 0,
			'class': 'o_account_reports_domain_total',
			'columns': [{'name': v} for v in total_columns],
			})
		return lines
		


	@api.model
	def _get_report_name(self):
		return _('Journal Report')