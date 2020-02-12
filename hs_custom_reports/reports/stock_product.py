# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ReportItemFund(models.AbstractModel):
	_name = "report.hs_custom_reports.stock_product_template"
	_description = "product stock report"


	@api.multi
	def _get_report_values(self, docids, data=None):
		report_name = "hs_custom_reports.stock_product_template"
		report = self.env["ir.actions.report"]._get_report_from_name(report_name)
		docs = self.env[report.model].browse(docids)
		lines = []
		
		for doc in docs:
			if doc.filter == "none":
				products = self.env["product.product"].search([])
			elif doc.filter == "category":
				categ_id = docs.category_id
				products = self.env["product.product"].search([('categ_id', '=', categ_id)])
			elif doc.filter == "product":
				products = [docs.product_id]
			else:
				raise exceptions.Warning("Este reporte no esta disponible para este tipo de inventario")

			for item in products:
				lines.append({
					'name' : item.name,
					'quantity' : ''
				})
		
		return {
			'doc_ids' : docids,
			'doc_model':report.model,
			'docs' : self.env[report.model].browse(docids),
			'lines' : lines,
			'report_type': data.get('report_type') if data else '',
		}