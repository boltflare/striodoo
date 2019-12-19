# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class ReportItemFund(models.AbstractModel):
	_name = "report.hs_custom_reports.item_fund_template"
	_description = "reporte Item by Fund"

	
	@api.model
	def _get_report_values(self, docids, data=None):
		report_name = "hs_custom_reports.item_fund_template"
		report = self.env["ir.actions.report"]._get_report_from_name(report_name)
		docs = self.env["account.payment"].browse(docids)
		return {
			'doc_ids' : docids,
			'doc_model':report.model,
			'docs' : docs,
		}

