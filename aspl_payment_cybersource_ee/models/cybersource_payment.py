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

from odoo.http import request
from odoo import api,fields,models, _
import logging
from datetime import datetime
import time
import hmac
import hashlib
import base64
import uuid
import  httpagentparser
_logger = logging.getLogger(__name__)


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('cybersource', 'CyberSouce')])
    cybersource_merchant_id = fields.Char(required_if_provider='cybersource', string="Merchant id")
    cybersource_key = fields.Char(required_if_provider='cybersource', string="Key")
    secret_key = fields.Char(string='SecretKey', required_if_provider='cybersource')
    profile_id = fields.Char(string='Profile ID', required_if_provider='cybersource')
    access_key = fields.Char(string='Access Key', required_if_provider='cybersource')

    def get_signature(self,data):
        secret = bytes(self.secret_key, 'utf-8')
        mystr = ', '.join("{!s}={!r}".format(key, val) for (key, val) in data.items()).replace(' ','')
        new_str = mystr.replace("'", '').encode('utf-8')
        hash = hmac.new(secret, new_str, hashlib.sha256)
        result = base64.b64encode(hash.digest())
        return  result

    def _get_feature_support(self):
        res = super(PaymentAcquirer, self)._get_feature_support()
        res['tokenize'].append('cybersource')
        return res

    def _get_cybersource_urls(self, environment):
        """ Authorize URLs """
        if environment == 'prod':
            return {'cybersource_form_url': 'https://testsecureacceptance.cybersource.com/pay'}
        else:
            return {'cybersource_form_url': 'https://testsecureacceptance.cybersource.com/pay'}

    cybersouce_values = {}
    @api.multi
    def cybersource_form_generate_values(self, values):
        self.ensure_one()
        cybersouce_values = {}
        if self.payment_flow == 'form':
            agent = request.httprequest.environ.get('HTTP_USER_AGENT')
            agent_details = httpagentparser.detect(agent)
            user_os = agent_details['os']['name']
            browser_name = agent_details['browser']['name']
            device = ''
            partner_id = self.env.user.partner_id
            if "Mobile"  in agent:
                device = 'Mobile'
            else:
                device = 'Web'
            sale_order_id = self.env['sale.order'].search([('name','=',(values.get('reference').split('-'))[0])])
            categ_data = ''
            vat = 'None'
            billing_partner_company = ''
            if sale_order_id:
                for line in sale_order_id.order_line:
                    categ_data += str(line.product_id.categ_id.name+',').replace(" ", "")
            if values.get('vat'):
                vat = values.get('vat')
            elif partner_id.vat:
                vat = partner_id.vat
            if values.get('billing_partner_commercial_company_name'):
                 billing_partner_company = values.get('billing_partner_commercial_company_name').replace(" ","")
            cybersouce_values.update({
                'access_key': self.access_key,
                'profile_id': self.profile_id,
                'transaction_uuid': str(uuid.uuid1()),
                'signed_field_names': "access_key,profile_id,transaction_uuid,signed_field_names,unsigned_field_names,signed_date_time,locale,transaction_type,reference_number,amount,currency,merchant_defined_data5,merchant_defined_data6,merchant_defined_data7,merchant_defined_data8,merchant_defined_data9,merchant_defined_data10",
                'unsigned_field_names': '',
                'signed_date_time': datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%SZ'),
                'locale': 'en',
                'transaction_type': 'sale',
                'reference_number': values.get('reference'),
                'amount': values.get('amount'),
                'currency': values.get('currency').name,
                'merchant_defined_data5': self.cybersource_merchant_id,
                'merchant_defined_data6': device,
                'merchant_defined_data7': vat,
                'merchant_defined_data8': billing_partner_company,
                'merchant_defined_data9': categ_data if categ_data else 'Invoicedata',
                'merchant_defined_data10': values.get('partner_email') if values.get('partner_email') else partner_id.email,
            })
            signature = self.get_signature(cybersouce_values)
            cybersouce_values.update({'signature': signature})
            print("---cybersouce_values---->>>>>>>",cybersouce_values)
        if self.payment_flow == 's2s':
            cybersouce_values = dict(values)
            cybersouce_values.update({
                'c_login': self.cybersource_merchant_id,
                'c_trans_key': self.cybersource_key,
                'c_amount': str(values['amount']),
                'c_show_form': 'PAYMENT_FORM',
                'c_type': 'AUTH_CAPTURE' if not self.capture_manually else 'AUTH_ONLY',
                'c_method': 'CC',
                'c_fp_sequence': '%s%s' % (self.id, int(time.time())),
                'c_version': '3.1',
                'c_relay_response': 'TRUE',
                'c_fp_timestamp': str(int(time.time())),
                'c_relay_url': 'shop/confirmation',
                'c_currency_code': values['currency'] and values['currency'].name or '',
                'address': values.get('partner_address'),
                'city': values.get('partner_city'),
                'country': values.get('partner_country') and values.get('partner_country').name or '',
                'email': values.get('partner_email'),
                'zip_code': values.get('partner_zip'),
                'first_name': values.get('partner_first_name'),
                'last_name': values.get('partner_last_name'),
                'phone': values.get('partner_phone'),
                'state': values.get('partner_state') and values['partner_state'].code or '',
                'billing_address': values.get('billing_partner_address'),
                'billing_city': values.get('billing_partner_city'),
                'billing_country': values.get('billing_partner_country') and values.get(
                    'billing_partner_country').name or '',
                'billing_email': values.get('billing_partner_email'),
                'billing_zip_code': values.get('billing_partner_zip'),
                'billing_first_name': values.get('billing_partner_first_name'),
                'billing_last_name': values.get('billing_partner_last_name'),
                'billing_phone': values.get('billing_partner_phone'),
                'billing_state': values.get('billing_partner_state') and values['billing_partner_state'].code or '',
            })
        return cybersouce_values

    @api.multi
    def cybersource_get_form_action_url(self):
        self.ensure_one()
        return self._get_cybersource_urls(self.environment)['cybersource_form_url']

class TxCybersource(models.Model):
    _inherit = 'payment.transaction'


    @api.model
    def _cybersource_form_get_tx_from_data(self, data):
        # transaction = self.browse(data if data else False)
        return data
    
    @api.multi
    def _cybersource_form_get_invalid_parameters(self, data):
        invalid_parameters = []
        return invalid_parameters

    @api.multi
    def _cybersource_form_validate(self, data):
        # transaction_ids = self.browse(data if data else False)
        for tran in data:
            tran._set_transaction_done()
        return True

    @api.multi
    def s2s_do_transaction(self, **kwargs):
        custom_method_name = '%s_s2s_do_transaction' % self.acquirer_id.provider
        for trans in self:
            transaction_status = {}
            transaction_status.update({
                'state': 'done',
                'date': fields.Datetime.now(),
                'state_message': request.session.get('reason'),
                'acquirer_reference': request.session.get('requestID') or '',
            })
            trans.write(transaction_status)
            trans._log_payment_transaction_sent()
            if hasattr(trans, custom_method_name):
                return getattr(trans, custom_method_name)(**kwargs)
    

