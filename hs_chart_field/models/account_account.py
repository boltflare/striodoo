# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class AccountAccountInherit(models.Model):
	_inherit = 'account.account'

	stri_fund = fields.Char("Fund Code")
	stri_budget = fields.Char("Budget Reference")
	stri_desig = fields.Char("Designated Code")
	stri_dept = fields.Char("Department ID")
	stri_account = fields.Char("Account")
	stri_class = fields.Char(string="Class Field", default="CLASSCODE")
	stri_program = fields.Char("Program Code")

	stri_project = fields.Char("Project ID")
	stri_activity = fields.Char(string="Activity Code", default="DEFAULT")
	stri_type = fields.Selection([("GLE", "GLE"), ("GLR", "GLR")], "Type")

	stri_chartfield = fields.Char(compute="_computed_chartfield", 
		string="Char Field")


	@api.depends('stri_fund', 'stri_budget', 'stri_desig', 'stri_dept',
		'stri_account', 'stri_class', 'stri_program', 'stri_project',
		'stri_activity', 'stri_type')
	def _computed_chartfield(self):
		resp = str(self.stri_fund) if str(self.stri_fund) != "False" else ""

		resp = resp + "," + str(self.stri_budget) if str(self.stri_budget) != "False" \
			else resp + ","
		
		resp = resp + "," + str(self.stri_desig) if str(self.stri_desig) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_dept) if str(self.stri_dept) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_account) if str(self.stri_account) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_class) if str(self.stri_class) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_program) if str(self.stri_program) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_project) if str(self.stri_project) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_activity) if str(self.stri_activity) != "False" \
			else resp + ","

		resp = resp + "," + str(self.stri_type) if str(self.stri_type) != "False" \
			else resp + ","

		self.stri_chartfield = resp
