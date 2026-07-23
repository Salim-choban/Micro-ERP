from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _name = 'erp.purchase.order'
    _description = 'Purchase Order'

    name = fields.Char(string='Order Reference', required=True, readonly=True, default='New')
    partner_id = fields.Many2one(
        'erp.partner',
        string='Supplier',
        domain=[('partner_type', '=', 'supplier')],
        required=True
    )
    order_line = fields.One2many(
        'erp.purchase.order.line',
        'order_id',
        string='Ordered Lines'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft', readonly=True)

    amount_total=fields.Float(string='Total',compute='_compute+amount',store=True)

    @api.depends('order_line.price_subtotal')
    def _compute_amount(self):
        for order in self:
            order.amount_total =sum(line.price_subtotal for line in order.order_line)

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_done(self):
        self.write({'state': 'done'})


class PurchaseOrderLine(models.Model):
    _name = 'erp.purchase.order.line'
    _description = 'Purchase Order Line'

    order_id = fields.Many2one('erp.purchase.order', string='Order Reference', ondelete='cascade',required=True)
    product_id = fields.Many2one('erp.product', string='Product')
    quantity = fields.Float(string='Quantity', default=1.0)
    price_unit=fields.Float(string='Unit Price')
    price_subtotal=fields.Float(string='Subtotal', compute='compute_subtotal',store=True)

    @api.depends('quantity','price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.price_subtotal=line.quantity * line.price_unit