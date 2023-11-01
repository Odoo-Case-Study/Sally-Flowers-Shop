from odoo import models, fields, api
from datetime import date
class FlowerWater(models.Model):
    _name = "flower.water"
    _description = "Flower Watering"
    _order = "date"

    serial_id = fields.Many2one('stock.lot', string="Serial ID")
    date = fields.Date(string="Watering Date",default=fields.Date.context_today)
    flower_name = fields.Char(string="Flower Name", related='serial_id.product_id.flower_id.common_name', store=True)

