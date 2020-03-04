# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class PeopleSoftReport(models.Model):
	_name = "account.peaplesoft.report"
	_description = "People Soft Report"
	_inherit = "account.report"


	filter_date = {'date_from': '', 'date_to': '', 'filter': 'today'}
	filter_all_entries = False
	filter_unfold_all = False


	def _get_templates(self):
		templates = super(PeopleSoftReport, self)._get_templates()
		templates['line_template'] = 'account_reports.line_template_peoplesoft_report'
		return templates


	def _get_columns_name(self, options):
		return [{'name': ''},
				{'name': _("Line")},
				{'name': _("Reference")},
				{'name': _("Amount"), 'class': 'number'}]


	@api.model
	def _get_lines(self, options, line_id=None):
		return []