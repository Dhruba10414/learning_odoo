from odoo import models,api,fields,exceptions
from datetime import timedelta


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

    color = fields.Integer()

    start_date = fields.Date(string='Start Date',
                             default=fields.Date.today)

    duration = fields.Integer(string='Session Days',
                              default=1)

    end_date = fields.Date(string='End Date',
                           compute='_compute_end_date',
                           inverse='_inverse_end_date',
                           store=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
                continue
            duration = timedelta(days=record.duration)
            record.end_date = record.start_date + duration

    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue
