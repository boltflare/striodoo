# -*- coding: utf-8 -*-


from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)


class PeopleSoftReport(models.AbstractModel):
	_name = "account.peaplesoft.report"
	_description = "People Soft Report"
	_inherit = "account.report"


	filter_date = {'date_from': '', 'date_to': '', 'filter': 'today'}
	filter_all_entries = False
	filter_journals = True
	filter_analytic = False
	filter_unfold_all = False


	def _get_templates(self):
		templates = super(PeopleSoftReport, self)._get_templates()
		templates['line_template'] = 'hs_custom_reports.line_template_peoplesoft_report'
		return templates


	def _get_columns_name(self, options):
		return [{'name': ''},
				{'name': _("Ledger")},
				{'name': _("Account")},
				{'name': _("Entry Event")},
				{'name': _("Fund")},
				{'name': _("Dsgc")},
				{'name': _("Budget Ref")},
				{'name': _("Dept ID")},
				{'name': _("Amount"), 'class': 'number'},
				{'name': _("Currency")},
				{'name': _("Reference")},
				{'name': _("Program")},
				{'name': _("Class")},
				{'name': _("Project")},
				{'name': _("Proj Unit")},
				{'name': _("Activity")},
				{'name': _("Analysis")}]


	def _do_filter_by_journal(self, options):
		journals = options['journals']
		if journals == None:
			return '' 

		for journal in journals:
			if journal['id'] == 'divider':
				continue

			if journal['selected'] == True:
				return 'AND inv.journal_id = {}'.format(journal['id'])

		return ''



	def _get_with_statement(self, options):
		dt_from = options['date'].get('date_from')
		dt_to = options['date'].get('date_to')
		by_journal = self._do_filter_by_journal(options)
		sql = """
		WITH people_soft_data AS 
		(SELECT (SELECT CASE WHEN line.credit > 0.00 
		THEN CONCAT(a.stri_fund, ',', a.stri_budget, ',', a.stri_desig, ',', a.stri_dept, ',', a.stri_account, ',', a.stri_class, ',', a.stri_program, ',', a.stri_project, ',', a.stri_activity, ',', a.stri_type) 
		ELSE 
			(SELECT CASE WHEN p.customer_type = 'fund' 
			THEN CONCAT(p.stri_fund, ',', p.stri_budget, ',', p.stri_desig, ',', p.stri_dept, ',', p.stri_account, ',', p.stri_class, ',', p.stri_program, ',', p.stri_project, ',', p.stri_activity, ',', p.stri_type)
			ELSE 
				(SELECT CONCAT(a2.stri_fund, ',', a2.stri_budget, ',', a2.stri_desig, ',', a2.stri_dept, ',', a2.stri_account, ',', a2.stri_class, ',', a2.stri_program, ',', a2.stri_project, ',', a2.stri_activity, ',', a2.stri_type) as strifund
				FROM account_account as a2, account_journal as j
				WHERE a2.id = j.default_debit_account_id AND j.id = inv.journal_id LIMIT 1)
			END)
		END) AS chartfield,
		inv.number AS reference,
		move.date AS date,
		(SELECT SUM(CASE WHEN line.credit > 0.00 THEN line.credit * -1 else line.debit END)) as amount
		FROM account_account AS a, res_partner AS p, account_move AS move, account_move_line AS line, account_invoice AS inv
		WHERE line.account_id = a.id AND line.partner_id = p.id AND line.move_id = move.id AND move.id = inv.move_id {}
		GROUP BY chartfield, inv.number, move.date
		ORDER BY inv.number DESC)
		SELECT 'ACTUALS' Ledger, 
		split_part(chartfield, ',', 5) AS account,
		CONCAT('REIMB_', (SELECT CASE WHEN split_part(chartfield, ',', 5) = '6998' THEN '6998' ELSE '6999' END)) as entry_event,
		split_part(chartfield, ',', 1) AS fund,
		split_part(chartfield, ',', 3) AS dsgc,
		split_part(chartfield, ',', 3) AS budget_ref,
		split_part(chartfield, ',', 4) AS dept_id,
		amount,
		'USD' Currency,
		reference,
		split_part(chartfield, ',', 7) AS program,
		(SELECT CASE WHEN split_part(chartfield, ',', 6) != 'CLASSCODE' 
		THEN split_part(chartfield, ',', 6) 
		ELSE (SELECT cc.code FROM class_code AS cc, account_invoice AS ai WHERE ai.class_code = cc.id AND ai.number = reference limit 1)
		END) AS class,
		split_part(chartfield, ',', 8) AS project,
		(SELECT CASE WHEN split_part(chartfield, ',', 8) = '' THEN '' ELSE 'SI000' END) AS proj_unit,
		split_part(chartfield, ',', 9) AS activity,
		split_part(chartfield, ',', 10) AS Analysis
		FROM people_soft_data
		WHERE date BETWEEN '{}' AND '{}';
		""".format(by_journal, dt_from, dt_to)

		return sql


	def _do_query(self, options):
		with_sql = self._get_with_statement(options)
		self.env.cr.execute(with_sql)
		results = self.env.cr.fetchall()
		return results


	@api.model
	def _get_lines(self, options, line_id=None):
		_logger.info("El valor de options es: '" + str(options))
		_logger.info("El valor de line_id es: '" + str(line_id))
		lines = []
		#invoices = self.env["account.move.line"].search()
		invoices = self._do_query(options)
		count = 0
		for invoice in invoices:
			lines.append({
				'id': count,
				'name': count,
				'unfoldable': False,
				'level': 3,
				'columns': [{'name' : v} for v in invoice],
			})
			count+=1

		if len(invoices) == 0:
			lines.append({
				'id': '',
				'name': '',
				'unfoldable': False,
				'level': 3,
				'columns': [{'name' : v} for v in ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',]],
			})
		
		return lines


	@api.model
	def _get_report_name(self):
		return _('People Soft')