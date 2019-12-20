# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class ReportItemFund(models.AbstractModel):
	_name = "report.hs_custom_reports.item_fund_template"
	_description = "reporte Item by Fund"
	

	def get_categ(self, recordset):
		pass

	
	"""
	@api.model
	def _get_report_values(self, docids, data=None):
		report_name = "hs_custom_reports.item_fund_template"
		report = self.env["ir.actions.report"]._get_report_from_name(report_name)
		docs = self.env[report.model].browse(docids)
		return {
			'doc_ids' : docids,
			'doc_model':report.model,
			'docs' : docs,
			'report_type': data.get('report_type') if data else '',
		}
	"""
	
	@api.model
	def _get_report_values(self, docids, data=None):
		report_name = "hs_custom_reports.item_fund_template"
		report = self.env["ir.actions.report"]._get_report_from_name(report_name)
		docs = self.env[report.model].browse(docids)
		document = [docids[0]] if len(docids) > 1 else docids
		lines = []
		for doc in docs:
			account = doc.property_account_income_id
			chartfield = account.stri_chartfield if len(account) > 0 else '' 
			lines.append({
				'name' : doc.name,
				'code' : doc.default_code,
				'categ' : doc.categ_id.display_name,
				'chartfield' : chartfield
			})
		return {
			'doc_ids' : docids,
			'doc_model':report.model,
			'docs' : self.env[report.model].browse(document),
			'lines' : lines,
			'report_type': data.get('report_type') if data else '',
		}
