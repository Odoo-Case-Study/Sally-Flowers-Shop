# -*- coding: utf-8 -*-
from collections import defaultdict
from odoo import models, fields, api


class Product(models.Model):

    _inherit = 'product.product'

    _description = 'the flower product'


    is_flower = fields.Boolean("Is Flower Product?",default=False)
    flower_id = fields.Many2one('flowers_shop_module.flower',string="Flower Product")
    needs_watering =fields.Boolean("Needs Watering",default=False)#,compute='_compute_needs_watering')
    sequence_id = fields.Many2one("ir.sequence", "Flower Sequence")
    gardeners_ids = fields.Many2many('res.users', string="Gardeners Users")
    # @api.depends('serial_id')
    # def _compute_needs_watering(self):
    #     print("_compute_needs_watering",self.needs_watering)

    def action_needs_watering(self):
        flowers = self.env["product.product"].search([("is_flower", "=", True)])
        print("flowers",flowers)
        serials = self.env["stock.lot"].search([("product_id", "in", flowers.ids)])
        print("serials",serials)
        lot_vals = defaultdict(bool)
        for serial in serials:
            if serial.water_ids:
                last_watered_date = serial.water_ids[0].date
                frequency = serial.product_id.flower_id.watering_frequency
                today = fields.Date.today()
                needs_watering = (today - last_watered_date).days >= frequency
                lot_vals[serial.product_id.id] |= needs_watering
            else:
                lot_vals[serial.product_id.id] = True
        for flower in flowers:
            flower.needs_watering = lot_vals[flower.id]

        print("lot_vals",lot_vals)

