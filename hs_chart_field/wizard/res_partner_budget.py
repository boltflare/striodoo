# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions

class PartnerBudgetWizard(models.TransientModel):
	_name="partner.budget.wizard"
	_description="Partner Budget Wizard"

	budget_year = fields.Char(string="Budget Year", size=4)


	@api.multi
	def action_update_budget(self):
		try:
			doc_ids=self._context.get('active_ids')
			account = self.env["res.partner"].browse(doc_ids)
			account.write({'stri_budget' : self.budget_year})
		except Exception as __ERROR:
			_logger.error("Error on budget reference field: " + str(__ERROR))
			#raise exceptions.Warning("No se encontraron cuentas por cobrar para el \
			#	producto ingreado: " + str(__ERROR))