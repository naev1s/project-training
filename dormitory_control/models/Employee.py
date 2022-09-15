from odoo import api, fields, models

class Employee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee Model from employee module"

    is_active = fields.Boolean(string="is Active")