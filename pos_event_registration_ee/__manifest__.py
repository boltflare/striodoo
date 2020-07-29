# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': "Pos Event Registration",
    'version': '0.0.2',
    'category': 'Point of Sale',
    'description': """
This module is used to register event on pos interface
""",
    'summary': 'This module is used to register event on pos interface',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'website': "http://www.acespritech.com",
    'currency': 'EUR',
    'price': 0.00,
    'depends': ['web', 'point_of_sale', 'base','event'],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/point_of_sale_view.xml',
        'views/product_view.xml',
        'views/event_view.xml',
        'views/pos_session_view.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
        ],
    "installable": True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
