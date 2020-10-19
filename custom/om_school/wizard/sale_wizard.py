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
                                 related='session_id.course_ids'
                                 help='These are the courses in current session')

    course_ids = fields.Many2many(comodel_name='res.partner',
                                  string='Courses for sale order')
