{
    'name' : 'Library Management',
    'version': '19.0.1.0.0',
    'summary': 'Manage library books and borrowing operations',
    'depends': ['base' ,'mail'],
    'data': [
        'views/base_menu.xml',
        'views/library_borrow_view.xml',
        'views/library_book_view.xml',

    ],
    'installable': True,
    'application': True,

}