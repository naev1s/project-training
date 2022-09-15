from odoo import api, fields, models

class Occupant(models.Model):
    _name = "dormitory_control.occupant"
    _description = "Occupant"

    name = fields.Char(string="Nama")
    contact = fields.Char(string="Kontak")
    address = fields.Char(string="Alamat")
    dob = fields.Datetime(string="Tanggal Lahir")
    dormitory_id = fields.Many2one(comodel_name="dormitory_control.dormitory", string="Asrama")
    room_id = fields.Many2one(comodel_name="dormitory_control.room", string="ID Kamar")

    # compute="_compute_room_id",
    # @api.depends('dormitory_id')
    # def _compute_room_id(self):
    #     for record in self:
    #         a = self.env["dormitory_control.room"].search([("dormitory_id", "=", record.id)]).mapped("room_id")
    #         record.room_id = a