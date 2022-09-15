from odoo import api, fields, models

class CleaningService(models.Model):
    _inherit = 'res.partner'
    _description = 'Cleaning Service'