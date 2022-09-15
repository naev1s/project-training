from odoo import http, models, fields
from odoo.http import request
import json

class Agusmart(http.Controller):
    @http.route('/dormitory_control/getdormitory', auth='public', method=['GET'])
    def getDormitory(self, **kw):
        dormitory = request.env['dormitory_control.dormitory'].search([])
        data = []
        for bb in dormitory:
            data.append({
                'dormitory_name' : bb.name,
                'initial' : bb.initial,
                'total_rooms' : bb.total_rooms
            })
        return json.dumps(data)

    @http.route('/dormitory_control/getroom', auth='public', method=['GET'])
    def getRoom(self, **kw):
        room = request.env['dormitory_control.room'].search([])
        data = []
        for r in room:
            room.append({
                'room_id' : r.room_id,
                'capacity' : r.capacity,
                'no_telepon' : r.dormitory_id,
                'barang' : r.total_occupants,
            })
        return json.dumps(data)