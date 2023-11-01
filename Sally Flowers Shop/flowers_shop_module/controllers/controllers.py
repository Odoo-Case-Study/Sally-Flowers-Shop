# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule(http.Controller):
#     @http.route('/flowers_shop_module/flowers_shop_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flowers_shop_module/flowers_shop_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flowers_shop_module.listing', {
#             'root': '/flowers_shop_module/flowers_shop_module',
#             'objects': http.request.env['flowers_shop_module.flowers_shop_module'].search([]),
#         })

#     @http.route('/flowers_shop_module/flowers_shop_module/objects/<model("flowers_shop_module.flowers_shop_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flowers_shop_module.object', {
#             'object': obj
#         })
