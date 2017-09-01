# -*- coding: utf-8 -*-
from odoo import http

# class NebizMenuItem(http.Controller):
#     @http.route('/nebiz_menu_item/nebiz_menu_item/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nebiz_menu_item/nebiz_menu_item/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nebiz_menu_item.listing', {
#             'root': '/nebiz_menu_item/nebiz_menu_item',
#             'objects': http.request.env['nebiz_menu_item.nebiz_menu_item'].search([]),
#         })

#     @http.route('/nebiz_menu_item/nebiz_menu_item/objects/<model("nebiz_menu_item.nebiz_menu_item"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nebiz_menu_item.object', {
#             'object': obj
#         })