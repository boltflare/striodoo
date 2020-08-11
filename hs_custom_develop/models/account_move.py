# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


import logging
_logger = logging.getLogger(__name__)

class AccountMovelineInherit(models.Model):
	_inherit = 'account.move.line'


	@api.multi
	def remove_move_reconcile(self):
		user = self.env.user
		group_manager = self.env.ref('account.group_account_user')
		if user in group_manager.users:
			raise exceptions.ValidationError('No cuenta con los permisos \
				necesarios para realizar esta acción.')
		
		return super(AccountMovelineInherit, self).remove_move_reconcile()