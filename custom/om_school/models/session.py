from odoo import models,api,fields

class SchoolSession(models.Model):
    _name = 'school.session'
    _description = 'Session Info'

    student_id = fields.Many2one(comodel_name='school.student',
                                 string='student',
                                 ondelete='cascade',
                                 required=True)

    name = fields.Char(string='Titile',related='student_id.name')

    instructor_id = fields.Many2one(comodel_name='res.partner',string='Instructor')

    course_ids = fields.Many2many(comodel_name='res.partner',string='Courses')