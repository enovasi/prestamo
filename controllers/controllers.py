# -*- coding: utf-8 -*-
from odoo import http

# class Prestamo(http.Controller):
#     @http.route('/prestamo/prestamo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prestamo/prestamo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prestamo.listing', {
#             'root': '/prestamo/prestamo',
#             'objects': http.request.env['prestamo.prestamo'].search([]),
#         })

#     @http.route('/prestamo/prestamo/objects/<model("prestamo.prestamo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prestamo.object', {
#             'object': obj
#         })