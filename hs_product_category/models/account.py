# -*- coding: utf-8 -*-

from odoo import api, fields, models, _



class AccountInvoiceInherit2(models.Model):
	_inherit = "account.invoice"


	can_user_payment = fields.Boolean(string="Puede registrar Pagos",
		compute="_compute_can_user_payment")


	def _compute_can_user_payment(self):
		value = self.env["account.payment"]._can_user_payment()
		if value > 0:
			self.can_user_payment = True
		else:
			self.can_user_payment = False




class AccountPaymentInherit1(models.Model):
	_inherit = "account.payment"


	user = fields.Many2one('res.users','Current User', 
		default=lambda self: self.env.user)


	journal_count = fields.Integer(string="total payments allowed",
		compute="_compute_journal_count")


	def _compute_journal_count(self):
		self.journal_count = self._can_user_payment()


	def _can_user_payment(self):
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



class AccountJournalInherit1(models.Model):
	_inherit = "account.journal"


	department_ids = fields.Many2many("product.category",
		"journal_payment_product_categ_rel", "product_category_id",
		"account_journal_id", "Product Category")


	
	active_to_user = fields.Boolean("")


	
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