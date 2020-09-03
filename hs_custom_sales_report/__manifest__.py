# -*- coding: utf-8 -*-
# 

{
	'name': 'Reporte para Ventas',
	'version': '1.0',
	'summary':'Vista de para visualizar las ventas por accounting y pos',
	'category': 'Tool',
	'depends': ['base', 'account', 'point_of_sale'],
	'description': """
		En este modulo se creara una vista para visualizar las ventas de accounting y del pos para STRI
	""",

	'author': 'Hermec Consulting, S.A.',
    'maintainer':'Ceila Hernandez',

	'data': [
		'security/ir.model.access.csv',
		'views/invoice_inherit_view.xml',

	],
	
	'installable': True,
	'auto_install': False,
}
