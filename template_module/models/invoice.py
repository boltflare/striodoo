# -*- coding: utf-8 -*-
from odoo import api, fields, models
import etree

class resPartnerInherit2(models.Model):
	_inherit = 'account.invoice'


	@api.model
	def fields_view_get(self, view_id=None, view_type='form',
					toolbar=False, submenu=False):
		result = super(resPartnerInherit2, self).fields_view_get(
		view_id=view_id, view_type=view_type,
		toolbar=toolbar, submenu=submenu)

	# Disabling the import button for users who are not in import group
		if view_type == 'tree':
			doc = etree.XML(result['arch'])
			if not self.env.user.has_group('account.group_account_user'):
			# When the user is not part of the import group
				for node in doc.xpath("//tree"):
					# Set the import to false
					node.set('import', 'false')
			result['arch'] = etree.tostring(doc)

		return result  
