# -*- coding: utf-8 -*-
# 

{
	'name': 'Reportes para STRI',
	'version': '1.0',
	'summary':'Reportes variados',
	'category': 'Tool',
	'depends': ['base', 'account', 'account_reports', 'stock'],
	'description': """
		Is a Module to create and add class code for customers.
	""",

	'author': 'HS Consul S.A.',

	'data': [
		'reports/items_funds.xml',
		'reports/stock_product.xml',
	],
		
	'installable': True,
	'auto_install': False,
}
