# -*- coding: utf-8 -*-
# 

{
	'name': 'Reportes para STRI',
	'version': '1.0',
	'summary':'Reportes variados',
	'category': 'Tool',
	'depends': ['base', 'account_reports', 'hs_chart_field'],
	'description': """
		Is a Module to create and add class code for customers.
	""",

	'author': 'HS Consul S.A.',

	'data': [
		'reports/items_funds.xml',
		'reports/people_soft_report.xml',
		'reports/people_soft_wizard.xml',
		'data/people_soft_data.xml',
		'views/account_journal.xml',
		'views/people_soft_report.xml',
	],
		
	'installable': True,
	'auto_install': False,
}
