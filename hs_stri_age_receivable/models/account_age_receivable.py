# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, exceptions, _

from odoo.tools import float_is_zero
from odoo.tools.misc import format_date
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)

class AgeReceivableInherit(models.AbstractModel):
	_inherit = "account.aged.receivable"


	def _get_columns_name(self, options):
		columns = super(AgeReceivableInherit, self)._get_columns_name(options)

		# Actualizamos el valor de la JRNL por No. Documento 
		columns[3] = {'name': _('Document')}

		# Eliminamos la columna JRNL, Pos: 1
		columns.pop(1)

		# Eliminamos la columna account, Pos 2 -> 1
		columns.pop(1)

		# Nada a pasado
		return columns


	# def _group_by_partner_id(self, options, line_id):
	# 	return super(AgeReceivableInherit, self)._group_by_partner_id(options, line_id)

	"""
	def _get_payment_name(self, line):
		recordset = self.env["account.payment"].search([('move_line_ids', '=', line.id)])
		for payment in recordset:
			return payment.name
		return line.name


	def _get_payment_ref(self, line):
		recordset = self.env["account.payment"].search([('move_line_ids', '=', line.id)])
		for payment in recordset:
			return payment.communication
		return line.name
	"""


	@api.model
	def _get_lines(self, options, line_id=None):
		lines = super(AgeReceivableInherit, self)._get_lines(options, line_id=line_id)
		for item in lines:
			logging.info(item.get('columns'))
			if item.get('level') == 2:
				# removemos la columna JRNL y la columna account
				columns = item.get('columns')
				columns.pop(0)
				columns.pop(0)
				item['columns'] = columns

			elif item.get('level') == 4:
				# removemos la columna JRNL y la columna account
				columns = item.get('columns')
				columns.pop(0)
				columns.pop(0)
				item['columns'] = columns
				"""
				is_payment_line = False 
				move_line = self.env['account.move.line'].browse(int(item['id']))
				if move_line.invoice_id:
					line_name = move_line.move_id.name
				elif move_line.statement_id:
					line_name = move_line.name
				else:
					line_name = self._get_payment_name(move_line)
					is_payment_line = True
	
				# removemos la columna account, la columna journal y
				# actualizamos la primera columna 
				columns = item.get('columns')
				columns[0] = {'name': line_name}
				columns.pop(1)
				columns.pop(2)

				if is_payment_line:
					payment_ref = self._get_payment_ref(move_line)
					columns[1] = {'name': payment_ref}

				item['columns'] = columns
				"""
		return lines
