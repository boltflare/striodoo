# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fund Manager',
    'version': '12.0',
    'summary':'List and create Fund Manager',
    'category': 'Tools',
    'depends': ['base', 'account', 'hs_customer_class_code'],
    'description': """
        Is a Module to create a fund manager for view customers.
    """,

    'author': 'Hermec Consulting, S.A.',
    'maintainer':'Ceila Hernandez',

    'data': [
      'security/ir.model.access.csv',
      'views/fund_manager_view.xml',
    ],
    
    'installable': True,
    'auto_install': False,
}
