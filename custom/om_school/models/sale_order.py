# -*- coding: utf-8 -*-

from odoo import fields,api,models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    session_id = fields.Many2one(comodel_name='school.session',
                                    string='Related Session',
                                    ondelete='set null')

    instructor_id = fields.Many2one(string='Session Instructor',
                                    related='session_id.instructor_id')

    course_ids = fields.Many2many(string='Courses',
                                   related='session_id.course_ids')

