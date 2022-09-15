# -*- coding: utf-8 -*-
# from odoo import http


# class Agusmart(http.Controller):
#     @http.route('/agusmart/agusmart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agusmart/agusmart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('agusmart.listing', {
#             'root': '/agusmart/agusmart',
#             'objects': http.request.env['agusmart.agusmart'].search([]),
#         })

#     @http.route('/agusmart/agusmart/objects/<model("agusmart.agusmart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agusmart.object', {
#             'object': obj
#         })
