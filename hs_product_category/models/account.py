# -*- coding: utf-8 -*-

from odoo import api, fields, models, _



class AccountInvoiceInherit2(models.Model):
	_inherit = "account.invoice"


	current_user = fields.Many2one(comodel_name='res.users', string="Current User",
		store=False, default=lambda self: self.env.user)


	can_user_payment = fields.Boolean(string="Puede registar pagos", store=False,
		default= lambda self: self._can_user_payment)

	
	@api.depends('current_user')
	def _can_user_payment(self):
		count = 0
		departments = self.current_user.departments_ids
		for dept in departments:
			journals = self.env["account.journal"].search([("department_ids", "=", dept.id), ("type", "in", ["cash", "bank"])])
			if journals:
				count = count + 1
		
		if count > 0:
			return True
		else:
			return False





class AccountPaymentInherit1(models.Model):
	_inherit = "account.payment"

	current_user = fields.Many2one(comodel_name='res.users', string="Current User",
		store=False, default=lambda self: self.env.user)

	"""
	journal_count = fields.Integer(string="total payments allowed",
		compute="_compute_journal_count")


	def _compute_journal_count(self):
		try:
			count = 0
			user = self.env.user
			departments = self.env["product.category"].search([("user_ids", "=", user.id)])
			for department in departments:
					journals = self.env["account.journal"].search([("department_ids", "=", department.id)])
					for journal in journals:
						if journal.type in ("cash", "bank"):
							count = count + 1
			return count
		except Exception as __ERROR:
			return -1
	"""




class AccountJournalInherit1(models.Model):
	_inherit = "account.journal"


	current_user = fields.Many2one(comodel_name='res.users', string="Current User",
		store=False, default=lambda self: self.env.user)


	department_ids = fields.Many2many("product.category",
		"journal_payment_product_categ_rel", "product_category_id",
		"account_journal_id", "Product Category")


	
	@api.model
	def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
		if self._context.get('search_journal_id'):
			args.append((('department_ids', '=', self._context['search_journal_id'])))
		return super(AccountJournalInherit1, self)._search(args, offset=offset, 
																 limit=limit, 
																 order=order, 
																 count=count, 
																 access_rights_uid=access_rights_uid
															)