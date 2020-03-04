# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class PeopleSoftReport(models.AbstractModel):
	_name = "account.peaplesoft.report"
	_description = "People Soft Report"
	_inherit = "account.report"


	filter_date = {'date_from': '', 'date_to': '', 'filter': 'today'}
	filter_all_entries = False
	filter_unfold_all = False


	def _get_templates(self):
		templates = super(PeopleSoftReport, self)._get_templates()
		templates['line_template'] = 'hs_custom_reports.line_template_peoplesoft_report'
		return templates


	def _get_columns_name(self, options):
		return [{'name': ''},
				{'name': _("Ledger")},
				{'name': _("Account")},
				{'name': _("Entry Event")},
				{'name': _("Fund")},
				{'name': _("Dsgc")},
				{'name': _("Budget Ref")},
				{'name': _("Dept ID")},
				{'name': _("Amount"), 'class': 'number'},
				{'name': _("Reference")},
				{'name': _("Program")},
				{'name': _("Class")},
				{'name': _("Project")},
				{'name': _("Proj Unit")},
				{'name': _("Analysis")}]



	@api.model
	def _get_lines(self, options, line_id=None):
		lines = []
		invoices = self.env["account.invoice"].search([('number', '!=', False)])
		for invoice in invoices:
			lines.append({
				'id': invoice.id,
				'name': invoice.number,
				'unfoldable': False,
				'level': 3,
				'columns': [{'name' : v} for v in ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]],
			})
		return lines


	@api.model
	def _get_report_name(self):
		return _('People Soft')