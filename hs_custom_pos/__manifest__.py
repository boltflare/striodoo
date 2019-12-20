# -*- coding: utf-8 -*-
# 

{
	'name': 'PoS - Config',
	'version': '1.0',
	'summary':'PoS Custom Config',
	'category': 'Tool',
	'depends': ['base', 'point_of_sale'],
	'description': """
		Is a Module to create and add class code for customers.
	""",

	'author': 'HS Consul S.A.',

	'data': [
		'views/res_partner.xml',
	],
		
	'installable': True,
	'auto_install': False,
}
