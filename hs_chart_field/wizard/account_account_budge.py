# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ChartfieldBudgetWizard(models.TransientModel):
	_name="account.budget.wizard"
	_description="Account Budget Wizard"

	budget_year = fields.Char(string="Budget Year", size=4)


	@api.multi
	def action_update_budget(self):
		try:
			doc_ids=self._context.get('active_ids')
			account = self.env["account.account"].browse(doc_ids)
			account.write({'stri_budget' : self.budget_year})
		except Exception as __ERROR:
			raise exceptions.ValidationError("No se encontraron cuentas por cobrar para el \
				producto ingreado: " + str(__ERROR))