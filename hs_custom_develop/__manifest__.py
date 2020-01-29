# -*- coding: utf-8 -*-
# 

{
	'name': 'HS Customs Develop',
	'version': '1.0',
	'summary':'Configuraciones generales',
	'category': 'Tool',
	'depends': ['base', 'sale', 'purchase', 'stock', 'account'],
	'description': """
		En este modulo se almacenan toda las configuraciones y desarrollos
		generales de HS Consulting para STRI
	""",

	'author': 'HS Consul S.A.',

	'data': [
		'views/sale_view.xml',
		'views/stock_view.xml',
	],
		
	'installable': True,
	'auto_install': False,
}
