# -*- coding: utf-8 -*-
{
	'name': "Muki Rest",

	'summary': """APP for Integration with VSO and Update customer information""",

	'description': """
		APP for Integration with VSO and Update customer information
	""",

	'author': "HS Consult",
	'website': "http://www.yourcompany.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'tools',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['base', 'account'],

	'external_dependencies': {
		'python' : ['requests_oauthlib', 'pprint']
	},

	# always loaded
	'data': [
		'security/ir.model.access.csv',
		'views/muki_rest.xml',
		'views/res_partner.xml',
		'views/vso_button.xml',
		# 'views/create_customer_wizard.xml',
	],
	'qweb': [
        "static/src/xml/muki_vso.xml",
    ],
	# only loaded in demonstration mode
	'demo': [
		#'demo/demo.xml',
	],
}