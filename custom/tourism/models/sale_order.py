# -*- coding: utf-8 -*-

from odoo import fields,api,models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_id = fields.Many2one(comodel_name='tourism.customer',
                                    string='Related Customer',
                                    ondelete='set null')

    package_id = fields.Many2one(string='Customer Package',
                                    related='customer_id.package_id')



