from odoo import api, fields, models

class Dormitory(models.Model):
    _name = "dormitory_control.dormitory"
    _description = "Dormitory"

    name = fields.Char(string="Nama Asrama")
    initial = fields.Char(string="Inisial Asrama")
    occupants_gender = fields.Selection([('putra', 'Putra'), ('putri', 'Putri')], string="Jenis Kelamin Penghuni")
    gender_code = fields.Char(string="Kode")

    # Gender
    @api.onchange('occupants_gender')
    def _onchange_occupants_gender(self):
        if self.occupants_gender == 'putra':
            self.gender_code = 'ASPA'
        elif self.occupants_gender == 'putri':
            self.gender_code = 'ASPI'

    # Rooms
    room_ids = fields.One2many(comodel_name="dormitory_control.room", inverse_name="dormitory_id", string="Daftar Kamar")
    total_rooms = fields.Integer(string="Jumlah Kamar")
    unused_rooms = fields.Char(compute="_compute_unused_rooms", string="Kamar Kosong")
    used_rooms = fields.Char(compute="_compute_used_rooms", string="Kamar Terisi")

    # SUM Used Rooms
    @api.depends("room_ids")
    def _compute_used_rooms(self):
        for record in self:
            record.used_rooms= len(self.env["dormitory_control.room"].search([("dormitory_id", "=", record.id),("occupants", "!=", "")]).mapped("room_id"))

    # SUM Unused Rooms 
    @api.depends("room_ids")
    def _compute_unused_rooms(self):
        for record in self:
            record.unused_rooms = record.total_rooms - len(self.env["dormitory_control.room"].search([("dormitory_id", "=", record.id),("occupants", "!=", "")]).mapped("room_id"))

    # occupant
    occupants_ids = fields.One2many(comodel_name="dormitory_control.occupant", inverse_name="dormitory_id", string="Daftar Mahasiswa")
    occupants = fields.Char(compute="_compute_occupants", string="Penghuni Asrama")

    # SUM Dormitory's Occupants
    @api.depends("occupants_ids")
    def _compute_occupants(self):
        for record in self:
            record.unused_rooms = len(self.env["dormitory_control.occupant"].search([("dormitory_id", "=", record.id)]).mapped("name"))