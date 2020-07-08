# -*- coding: utf-8 -*-

from . import library
import json
from odoo import models, fields, api


import logging
_logger = logging.getLogger(__name__)

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    def action_muki_connect(self):
        # init API
        api = library.RestAPI()
        api.authenticate()

        
        # test API
        logging.info(str(api.execute('/api')))
        logging.info(str(api.execute('/api/user')))

        # create customer
        
        # # check customer
        # data = {
        # 	'model': "res.partner",
        # 	'domain': json.dumps([['name', '=', "Prueba VSO"]]),
        # 	'limit': 1
        # }
        # response = api.execute('/api/custom/create/vso', data=data)
        # customer = next(iter(response), False)
        
        

        # data = {
        #     'model': "res.partner",
        #     'domain': json.dumps([['customer_type', '=', "person"]]),
        #     'fields': json.dumps(['name', 'email']),
        # }
        response = api.execute('/api/custom/create/vso')
        result = response['result']
        for entry in result:
            number = entry.get('name')
            total = entry.get('email')
            visit = entry.get('visitor')
        response = api.execute('/api/custom/visitor/vso')
        # self.env["res.partner"].create({'name':number,'email':total,'visitor':visit})
        logging.info(str(response))

        # userinf = api.execute('/api/custom/hsusertype')
        #         result = userinf['result']
            
        #         logging.warning("result:" + str(result))
        #         for entry1 in result:
        #             usuarios = entry1.get('users')

        """
        # sampel query
        data = {
            'model': "res.partner",
            'domain': json.dumps([['parent_id.name', '=', "Azure Interior"]]),
            'fields': json.dumps(['name', 'image_small']),
        }
        response = api.execute('/api/search_read', data=data)
        for entry in response:
            entry['image_small'] = entry.get('image_small')[:5] + "..."
        logging.info(str(response))

        # check customer
        data = {
            'model': "res.partner",
            'domain': json.dumps([['name', '=', "Sample Customer"]]),
            'limit': 1
        }
        response = api.execute('/api/search', data=data)
        customer = next(iter(response), False)

        # create customer
        if not customer:
            values = {
                'name': "Sample Customer",
            }
            data = {
                'model': "res.partner",
                'values': json.dumps(values),
            }
            response = api.execute('/api/create', type="POST", data=data)
            customer = next(iter(response))

        # create product
        values = {
            'name': "Sample Product",
        }
        data = {
            'model': "product.template",
            'values': json.dumps(values),
        }
        response = api.execute('/api/create', type="POST", data=data)
        product = next(iter(response))

        # create order
        values = {
            'partner_id': customer,
            'state': 'sale',
            'order_line': [(0, 0, {'product_id': product})],
        }
        data = {
            'model': "sale.order",
            'values': json.dumps(values),
        }
        response = api.execute('/api/create', type="POST", data=data)
        order = next(iter(response))
        """


