# -*- coding: utf-8 -*-
# 

{
	'name': 'Reportes para STRI',
	'version': '1.0',
	'summary':'Reportes variados',
	'category': 'Tool',
	'depends': ['base', 'account', 'account_reports'],
	'description': """
		Is a Module to create and add class code for customers.
	""",

	'author': 'HS Consul S.A.',

	'data': [
		'reports/items_funds.xml',
		'reports/stock_product.xml',
		'views/journal_report.xml'
	],
		
	'installable': True,
	'auto_install': False,
}
