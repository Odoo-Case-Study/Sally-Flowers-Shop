from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    flower_ids = fields.Many2many('flowers_shop_module.flower')