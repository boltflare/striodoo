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

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pos_event_ok = fields.Boolean(string='Is an Event Ticket', help="If checked this product automatically "
      "creates an event registration at the sales order confirmation.")


class Product(models.Model):
    _inherit = 'product.product'

    pos_event_ticket_ids = fields.One2many('pos.event.ticket', 'product_id', string='Event Tickets')

    @api.onchange('pos_event_ok')
    def _onchange_pos_event_ok(self):
        """ Redirection, inheritance mechanism hides the method on the model """
        if self.pos_event_ok:
            self.type = 'service'

class PosOrderLine(models.Model):

    _inherit = 'pos.order.line'

    event_id = fields.Many2one('event.event', string='Event',
       help="Choose an event and it will automatically create a registration for this event.")
    pos_event_ticket_id = fields.Many2one('pos.event.ticket', string='Event Ticket', help="Choose "
        "an event ticket and it will automatically create a registration for this event ticket.")
    pos_event_ok = fields.Boolean(related='product_id.pos_event_ok', readonly=True)

    def _order_line_fields(self, line, session_id=None):
        lines = super(PosOrderLine, self)._order_line_fields(line, session_id=None)
        lines[2].update({'event_id': line[2].get('event_id', False)})
        lines[2].update({'pos_event_ticket_id': line[2].get('pos_event_ticket_id', False)})
        return line


class EventTicket(models.Model):
    _name = 'pos.event.ticket'
    _description = 'Event Ticket'

    def _default_product_id(self):
        return self.env.ref('event_sale.product_product_event', raise_if_not_found=False)

    name = fields.Char(string='Name', required=True, translate=True)
    event_id = fields.Many2one('event.event', string="Event", ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product',
                                 required=True, domain=[("pos_event_ok", "=", True)],
                                 default=_default_product_id)

class Event(models.Model):
    _inherit = 'event.event'

    pos_event_ticket_ids = fields.One2many(
        'pos.event.ticket', 'event_id', string='Event Ticket',
        copy=True)

class EventRegistration(models.Model):
    _inherit = 'event.registration'
    pos_event_ticket_id = fields.Many2one('pos.event.ticket', string='Event Ticket', readonly=True)
    pos_order_line_id = fields.Many2one('pos.order.line', string='Sales Order Line', ondelete='cascade')

class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def _process_order(self, pos_order):
        res = super(PosOrder, self)._process_order(pos_order)
        Registration = self.env['event.registration'].sudo()
        for line in res.lines:
            for each in range(int(line.qty)):
                if line.event_id:
                    data = {
                        'pos_order_line_id': line.id,
                        'event_id' : line.event_id.id or False,
                        'pos_event_ticket_id': line.pos_event_ticket_id.id or False,
                        'state':'open',
                    }
                    Registration.create(data)
        return res

class PosSession(models.Model):
    _inherit = 'pos.session'

    event_count = fields.Integer(string="Registration Count", compute="event_registration_count")

    def event_registration_count(self):
        for session in self:
            order_line_count = 0
            for order in session.order_ids:
                order_line_count += sum(order.lines.filtered(lambda line: line.event_id).mapped('qty'))
            session.event_count = order_line_count

    def open_registration(self):
        order_line_ids = []
        for order in self.order_ids:
            order_line_ids.extend(order.lines.filtered(lambda line : line.event_id).ids)
        return {
            'name': _('Event Registration'),
            'type': 'ir.actions.act_window',
            'res_model': 'event.registration',
            'view_mode': 'tree,form',
            'domain': [('pos_order_line_id', 'in', order_line_ids)],
        }




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
