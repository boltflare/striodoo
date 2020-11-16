# -*- coding: utf-8 -*-
{
	'name': "click automatico btn invoice",

	'summary': """click automatico btn invoice""",

	'description': """
		
	""",

	'author': "HS Consult",
	'website': "http://www.yourcompany.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'tools',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['base','point_of_sale' ],

	# 'external_dependencies': {
	# 	'python' : ['requests_oauthlib', 'pprint']
	# },

	# always loaded
	'data': [
		
		'view/agregar_js_pos.xml',
	
	],
	# only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
}