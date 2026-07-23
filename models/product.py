from odoo import models, fields


class ErpProduct(models.Model):
    _name = 'erp.product'
    _description = 'Product Management'

    name = fields.Char(string='Product Name', required=True)
    price = fields.Float(string='Price', required=True)
    qty_available = fields.Float(string='Available Quantity', default=0.0)

    product_type = fields.Selection([
        ('storable', 'Storable Product'),
        ('service', 'Service'),
        ('consumable', 'Consumable Product'),
    ], string='Product Type', default='storable')

    supplier_id = fields.Many2one(
        'erp.partner',
        string='Supplier',
        domain=[('partner_type', '=', 'supplier')]
    )

    default_code=fields.Char(string='Internal Reference')
    standard_price=fields.Float(string='cost')
    uom=fields.Char(string='Unit of Measure',default='Unit')
    image_1920=fields.Image(string='Product Image')
    active=fields.Boolean(default=True)
    description=fields.Text(string='description')