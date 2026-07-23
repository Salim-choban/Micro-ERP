from odoo import models, fields


class ErpPartner(models.Model):
    _name = 'erp.partner'
    _description = 'TEST TEST TEST'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone Number')
    address = fields.Text(string='Address')

    date_registered = fields.Date(
        string='Registration Date',
        default=fields.Date.context_today
    )

    partner_type = fields.Selection([
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
    ], string='Partner Type', default='customer', required=True)