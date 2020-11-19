# -*- coding: utf-8 -*-
from odoo import models, api , fields


class PosSession(models.Model):
    _inherit = ['pos.session']

    @api.multi
    def action_pos_session_validate(self):
        self.action_close_session_button()
        self._check_pos_session_balance()
        self.action_pos_session_close()

    @api.multi
    def action_pos_session_closing_control(self):
        for session in self:
            session.write({'state': 'closing_control', 'stop_at': fields.Datetime.now()})
            if not session.config_id.cash_control:
                self.action_close_session_button()
                session.action_pos_session_close()

    @api.multi
    def action_close_session_button(self):
        for session in self:
            orders = session.order_ids.filtered(lambda order: order.state == 'paid' and order.partner_id)
            for order in orders:
                order.action_pos_order_invoice()
                order.invoice_id.sudo().action_invoice_open()



