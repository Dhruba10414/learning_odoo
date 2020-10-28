from odoo import fields, api, models, exceptions
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta


class TourismCustomer(models.Model):
    _name = 'tourism.customer'
    _description = 'Customer Information'

    name = fields.Char(string="Name", required=True)

    package_id = fields.Many2one(comodel_name='tourism.package',
                                 string='package',
                                 ondelete='cascade',
                                 required=True)

    package_name = fields.Char(string='Package Title', related='package_id.name')

    quantity = fields.Integer(string="Quantity")

    price = fields.Integer(string='Price', related='package_id.price')

    guide_id = fields.Many2one(comodel_name='res.partner', string='Guide')

    total_price = fields.Float(string='Total Price', readonly=True)

    color = fields.Integer()

    start_date = fields.Date(string='Start Date',
                             default=fields.Date.today)

    duration = fields.Integer(string='Days',
                              default=3)

    end_date = fields.Date(string='End Date',
                           compute='_compute_end_date',
                           store=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
                continue
            duration = timedelta(days=record.duration)
            record.end_date = record.start_date + duration

    @api.onchange('price', 'quantity')
    def _onchange_total_price(self):
        if self.quantity < 0.00:
            raise UserError('Add a valid quantity.')

        self.total_price = self.price * self.quantity
