from odoo import fields, models, api

class TourismPackage(models.Model):
    _name = 'tourism.package'
    _description = 'Available Packages'

    name = fields.Char(string="Name", required=True)
    duration = fields.Integer(string="duration")
    price = fields.Integer(string='price')
    transport = fields.Selection([
        ('bus', 'Bus'),
        ('air', 'Air'),
    ], string='transport', default='bus')