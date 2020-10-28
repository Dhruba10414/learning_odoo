{
    'name': 'Tourism Agency',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Dhruba',
    'website': 'abc.com',
    'license': 'AGPL-3',
    'summary': 'Tour and Ticket Package Module',
    'description': """Module to manage tourism agency""",
    'depends': ['base', 'mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'view/menu.xml',
        'view/package.xml',
        'view/customer.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}