# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Class Code',
    'version': '12.0',
    'summary':'List and create class code',
    'category': 'Accounting',
    'depends': ['base'],
    'description': """
        Is a Module to create and add class code for customers.
    """,

    'author': 'Hermec Solutions, S.A.',
    'maintainer':'Ceila Hernandez',

    'data': [
      'security/ir.model.access.csv',
      'views/class_code_view.xml',
    ],
    
    'installable': True,
    'auto_install': False,
}
