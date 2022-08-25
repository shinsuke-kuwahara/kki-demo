# -*- coding: utf-8 -*-
# from odoo import http


# class KkiMaster001(http.Controller):
#     @http.route('/kki_master001/kki_master001/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_master001/kki_master001/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_master001.listing', {
#             'root': '/kki_master001/kki_master001',
#             'objects': http.request.env['kki_master001.kki_master001'].search([]),
#         })

#     @http.route('/kki_master001/kki_master001/objects/<model("kki_master001.kki_master001"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_master001.object', {
#             'object': obj
#         })
