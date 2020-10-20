from odoo import fields,models,api

class SaleWizard(models.TransientModel):
    _name = 'school.sale.wizard'
    _description = 'Wizard: Quick sale orders for session students'

    def _default_session(self):
        return self.env['school.session'].browse(self._context.get('active_id'))

    session_id= fields.Many2one(comodel_name='school.session',
                                string='session',
                                required=True,
                                default=_default_session)

    session_course_ids = fields.Many2many(comodel_name='res.partner',
                                 string='Courses in Current Session',
                                 related='session_id.course_ids',
                                 help='These are the courses in current session')

    course_ids = fields.Many2many(comodel_name='res.partner',
                                  string='Courses for sale order')

    def create_sale_orders(self):
        session_product_id = self.env['product.product'].search([('is_session_product', '=', True)], limit=1)
        if session_product_id:
            for course in self.course_ids:
                order_id = self.env['sale.order'].create({
                    'partner_id': course.id,
                    'session_id': self.session_id.id,
                    'order_line': [(0,0, {'product_id': session_product_id.id, 'price_unit': self.session_id.total_price})]
                })
