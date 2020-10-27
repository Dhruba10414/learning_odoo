from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Table"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    guardian = fields.Char(string="Guardian")
    note = fields.Text(string="Notes")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'FeMale'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    image = fields.Binary(string="Image")

    tuition_fee = fields.Float(string='Tuition Fee', default= 0.0)

    additional_donation= fields.Float(string='Additional Donation', default=10000.0)

    total_fee= fields.Float(string='Total Fees', readonly= True)

    session_ids=fields.One2many(comodel_name='school.session',
                                inverse_name='student_id',
                                string='sessions')

    @api.onchange('tuition_fee','additional_donation')
    def _onchnge_total_fee(self):
        if self.tuition_fee < 0.00:
            raise UserError('Add a valid tuition fee.')

        self.total_fee = self.tuition_fee + self.additional_donation

    @api.constrains('additional_donation')
    def _check_additional_donation(self):
        for record in self:
            if record.additional_donation < 10000:
                raise ValidationError('Add a donation more than 10000.')