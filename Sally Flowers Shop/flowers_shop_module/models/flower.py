# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Flower(models.Model):
    _name = 'flowers_shop_module.flower'
    _description = 'flower'
    _rec_name='common_name'

    common_name = fields.Char(string='Flower Common Name', required=True)
    scientific_name = fields.Char(string='Flower Scientific Name',help='scientific name!')
    season_start = fields.Date(string='Season Start', required=True,default=fields.Date.context_today)
    season_end = fields.Date(string='Season End', required=True,)
    watering_frequency = fields.Integer(string='Watering Frequency', default=1)
    watering_amount_ml = fields.Integer(string='Watering Amount (ml)')

    def name_get(self):
        return [(flower.id, "{} ({})".format(flower.scientific_name, flower.common_name)) for flower in self]
   
