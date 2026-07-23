{
    'name': 'Micro-ERP System',
    'version': '1.0',
    'category': 'Sales/Purchase',
    'summary': 'Micro system for managing sales and purchases',

    'depends': ['base'],

    'data': [
    'security/ir.model.access.csv',

    'views/partner_views.xml',
    'views/product_views.xml',
    'views/sale_views.xml',
    'views/purchase_views.xml',
],

    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}