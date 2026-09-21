{
    'name': 'Sale Line Extension',
    'version': '19.0.1.0.0',
    'depends': [
        'sale_management',
        'sale_stock',

    ],
    'data': [
        'views/sale_order_line_views.xml',
        'views/stock_move_views.xml',
    ],
    'installable': True,
    'application': False,
}