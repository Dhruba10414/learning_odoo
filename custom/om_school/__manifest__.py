{
    'name': 'School Management',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Odoo Mates',
    'website': 'odoomates.com',
    'license': 'AGPL-3',
    'summary': 'School Management Module',
    'description': """Module to manage school""",
    'depends': ['base', 'mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'view/student.xml',
        'view/menuitem.xml',
        'view/session.xml',
        'view/saleinherit.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}