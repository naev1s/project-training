import string
from odoo import api, fields, models

class Room(models.Model):
    _name = "dormitory_control.room"
    _rec_name = "room_id"
    _description = "Room"

    room_id = fields.Char(string="ID Kamar")
    capacity = fields.Integer(string="Kapasitas Kamar")

    # Dormitory
    dormitory_id = fields.Many2one(comodel_name="dormitory_control.dormitory", string="Asrama", ondelete="cascade")

    # Occupants
    occupant_ids = fields.One2many(comodel_name="dormitory_control.occupant", inverse_name="room_id", string="Penghuni")
    occupants = fields.Char(string='Daftar Penghuni')
    total_occupants = fields.Char(compute="_compute_occupants", string="Total Penghuni Kamar")

    # Occupants
    @api.depends('occupant_ids')
    def _compute_occupants(self):
        for record in self:
            a = self.env["dormitory_control.occupant"].search([("room_id", "=", record.id)]).mapped("name")
            b = len(a)
            record.total_occupants = b
            record.occupants = a

    # Contraints
    _sql_constraints = [
        ('unique_room_id','unique(room_id)','Nomor kamar tidak boleh sama')
    ]