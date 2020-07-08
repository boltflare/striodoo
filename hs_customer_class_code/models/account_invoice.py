# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime
from dateutil import tz


import logging
_logger = logging.getLogger(__name__)


class accountInvoiceInherit2(models.Model):
    _inherit = "account.invoice"


    class_code = fields.Many2one("class.code", "Class Code")
    customer_is_fund = fields.Boolean(string="Is Customer Fund?", compute="_customer_is_fund", default=False)
    #btn_credit_note = fields.Boolean(compute="_compute_btn_credit_note", string="Activar button credit note")
    #CAMPO PARA SOBRESCRIBIR EL CAMPO DE FECHA
    date_invoice = fields.Date(string='Invoice Date',
        readonly=True, states={'draft': [('readonly', False)]}, default = fields.Date.context_today, index=True,
        help="Keep empty to use the current date", copy=False)


    @api.depends('partner_id')
    def _customer_is_fund(self):
        # self.customer_is_fund = True if self.partner_id.customer_type == 'fund' else False
        for invoice in self:
            customer_type = invoice.partner_id.customer_type
            invoice.customer_is_fund = True if customer_type == 'fund' else False

    @api.model
    def create(self, values):
        if values.get('origin') and values.get('type') == 'out_refund':
            reference = values.get('origin')
            invoice = self.env['account.invoice'].search([('number', '=', reference)], limit=1)
            values['class_code'] = invoice.class_code.id if invoice.partner_id.customer_type == 'fund' else False
        return super(accountInvoiceInherit2, self).create(values)
    

   
    def search_classcode(self, cr, uid, ids, context=None): 
        record= []
        for rec in self.browse(cr, uid, ids, context): 
            record.append((rec.class_code.id, (rec.class_code.code and (rec.class_code.code + ' [] ')) + rec.class_code.name))
            # searching = rec.env['class.code'].search([('code', '=', rec.class_code.id),('name', '=', rec.class_code.name)])
            # record.append((searching))
        return record
    

    # def name_get(self, cr, uid, ids, context=None):
    #     result = []
    #     for bank in self.browse(cr, uid, ids, context):
    #         result.append((bank.id, (bank.bic and (bank.bic + ' - ') or '') + bank.name))
    #     return result
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         record_name = '[' + record.code + '] ' + record.name
    #         result.append((record.id, record_name))
    #     return result

    """
    @api.depends('type')
    def _compute_btn_credit_note(self):
        for invoice in self:
            from_zone = tz.gettz('UTC')
            to_zone = tz.gettz('America/Panama')
            utc = datetime.now(from_zone)
            date_current = utc.astimezone(to_zone)


            date_invoice = invoice.
    """