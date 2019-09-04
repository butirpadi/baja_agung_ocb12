# -*- coding: utf-8 -*-
from odoo import http

# class BajaAgungOcb12(http.Controller):
#     @http.route('/baja_agung_ocb12/baja_agung_ocb12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/baja_agung_ocb12/baja_agung_ocb12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('baja_agung_ocb12.listing', {
#             'root': '/baja_agung_ocb12/baja_agung_ocb12',
#             'objects': http.request.env['baja_agung_ocb12.baja_agung_ocb12'].search([]),
#         })

#     @http.route('/baja_agung_ocb12/baja_agung_ocb12/objects/<model("baja_agung_ocb12.baja_agung_ocb12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('baja_agung_ocb12.object', {
#             'object': obj
#         })