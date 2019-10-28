# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class ProductCategoryInherit1(models.Model):
	_inherit = "product.category"


	current_user = fields.Many2one('res.users','Current User', 
		default=lambda self: self.env.user)

	user_ids = fields.Many2many("res.users", 
		"user_product_category_rel", "product_category_id", 
		"user_id", "User")

	account_journal_ids = fields.Many2many("account.journal",
		"journal_payment_product_categ_rel", "account_journal_id",
		"product_category_id", "AccountJournal")

	user_count = fields.Integer("# Users", 
		compute="_compute_user_count")
	
	account_journal_count = fields.Integer("# Payments", 
		compute="_compute_account_journal_count")


	# active_to_user = fields.Boolean(string="Activo",
	# 	compute="_compute_active_to_current_user")



	def _compute_user_count(self):
		"""[summary]
		"""
		for categ in self:
			if categ.user_ids:
				categ.user_count = len(categ.user_ids)



	def _compute_account_journal_count(self):
		"""[summary]
		"""
		for categ in self:
			if categ.account_journal_ids:
				categ.account_journal_count = len(categ.account_journal_ids)


	"""
	@api.depends("user_ids")
	def _compute_active_to_current_user(self):
		user = self.env.user
		for categ in self:
			if categ.user_ids:
				if user.id in categ.user_ids:
					categ.active_to_user = True
	"""
			





class ProductInherit2(models.Model):
	_inherit = "product.product"

	current_user = fields.Many2one('res.users','Current User', 
		default=lambda self: self.env.user)

	
	salesperson_ids = fields.Many2many("res.users", 
		"product_salesperson_rel", "product_id", 
		"salesperson_id", "Salesperson")


	@api.model
	def create(self, values):
		"""Override default Odoo create function and extend."""
		# Do your custom logic here
		_logger.info("Value of create is:  " + str(values))
		if "categ_id" in values:
			category = values["categ_id"]
			users = self.env["res.users"].search([("departments_ids", '=', category)])
			values["salesperson_ids"] = [(6, users)]
		return super(ProductInherit2, self).create(values)


	@api.multi
	def write(self, values):
		"""Override default Odoo write function and extend."""
		# Do your custom logic here

		_logger.info("Value of write is:  " + str(values))
		if "categ_id" in values:
			category = values["categ_id"]
			query = self.env["res.users"].search([("departments_ids", '=', category)])
			users = list(set(query))
			_logger.info("Value of user is:  " + str(users))
			values["salesperson_ids"] = [(6, _, users)]
		return super(ProductInherit2, self).write(values)