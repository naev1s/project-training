from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_security = fields.Boolean(string="Is Security")
    is_cleaning_service = fields.Boolean(string="Is Cleaning Service")