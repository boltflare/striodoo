# -*- coding: utf-8 -*-
# 

{
	'name': 'HS Customs Develop',
	'version': '1.0',
	'summary':'Configuraciones generales',
	'category': 'Tool',
	'depends': ['base', 'sale', 'purchase', 'stock', 'account', 'point_of_sale', 'website_sale', 'hs_customer_class_code', 'hs_chart_field'],
	'description': """
		En este modulo se almacenan toda las configuraciones y desarrollos
		generales de HS Consulting para STRI
	""",

	'author': 'HS Consul S.A.',

	'data': [
		'views/account_invoice.xml',
		'views/sale_view.xml',
		'views/stock_view.xml',
		'views/point_of_sale.xml',
		'wizard/acc_acc_budget.xml',
		'wizard/res_partner_budget.xml',
	],
	'qweb': [
		'static/src/xml/pos_hide_tax.xml'
	],
		
	'installable': True,
	'auto_install': False,
}
