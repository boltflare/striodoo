{
    'name': 'Details in POS Receipt',
    'summary': """Add Discount Price in details to POS Receipt""",
    'version': '1.0',
    'description': """Add Discount Price in details to POS Receipt""",
    'author': "HS Consulting S.A.",
	'website': "http://www.hconsul.com/odoo/",
	'maintainer': 'Ceila Hernández',
    'contributors': ['Luis Dominguez'],
    'category': 'Point of Sale',
    'depends': ['base', 'point_of_sale'],
    'license': 'OPL-1',
    'data': [
		'views/pos_template.xml',
    ],
    'qweb': ['static/src/xml/pos_receipt_view.xml'],
    # 'images': ['static/description/banner.jpg'],
    # 'demo': [],
    'installable': True,
    'auto_install': False,

}
