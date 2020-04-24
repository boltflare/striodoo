# -*- coding: utf-8 -*-
# Part of Browseinfo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models




class sale_order_line_inherite(models.Model):
    _inherit = "sale.order.line"

    product_cost = fields.Float(string="Cost",compute="_compute_cost_product",store=True)
    profit = fields.Float(string="Profit",compute="_compute_profit",store=True)
    order_date = fields.Datetime(string="Order Date",related="order_id.confirmation_date",store=True)
    return_qty = fields.Float(string="Return Quantity",compute="_compute_return_qty",store=True,default=0.0)
    return_rate = fields.Float(string="Return Rate",compute="_compute_return_rate",store=True)
    profitability = fields.Float(string="Profitability",compute="_compute_profitability",store=True)
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Sales Value', readonly=True, store=True)


    @api.multi
    @api.depends('profit','product_cost')
    def _compute_profitability(self):
        for line in self:
            if line.product_cost > 0.0:
                line['profitability'] = line.profit/line.product_cost
    
    @api.multi
    @api.depends('qty_delivered','return_qty')
    def _compute_return_rate(self):
        for line in self:
            if line.return_qty > 0.0:
                rate =  (line.qty_delivered - line.return_qty)/(line.return_qty)
                line['return_rate'] = rate/100

    @api.multi
    @api.depends('qty_delivered')
    def _compute_return_qty(self):
        for line in self:
            picking = self.env['stock.picking'].search([])
            for i in picking:
                if i.group_id.name == line.order_id.name:
                    for j in  i.move_ids_without_package:
                        if j.move_dest_ids:
                            for k in j.move_dest_ids:
                                if k.product_id.id == line.product_id.id and k.state != "done":
                                    line['return_qty'] = line.return_qty + k.product_uom_qty

    @api.multi
    @api.depends('product_id','product_uom_qty')
    def _compute_cost_product(self):
        for line in self:
            line['product_cost'] = line.product_id.standard_price * line.product_uom_qty

    @api.multi
    @api.depends('product_cost','price_subtotal')
    def _compute_profit(self):
        for line in self:
            line['profit'] = line.price_subtotal - line.product_cost
