from odoo import models, fields, api


class SaleOrder(models.Model):
    _name = 'erp.sale.order'
    _description = 'Sale Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default='New')
    partner_id = fields.Many2one('erp.partner', string='Customer', required=True)
    date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    order_line = fields.One2many('erp.sale.order.line', 'order_id', string='Order Lines')

    total_amount = fields.Float(string='Total', compute='_compute_total_amount', store=True)

    @api.depends('order_line.price_subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.price_subtotal for line in order.order_line)


class SaleOrderLine(models.Model):
    _name = 'erp.sale.order.line'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('erp.sale.order', string='Order', ondelete='cascade')
    product_id = fields.Many2one('erp.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Float(string='Price Unit', related='product_id.price', store=True)
    price_subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.price_subtotal = line.quantity * line.price_unit