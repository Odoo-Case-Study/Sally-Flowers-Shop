# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Flower(models.Model):
    _name = 'flowers_shop_module.flower'
    # _inherit= ['mail.thread','mail.activity.mixin']
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
    # water_full_amount= fields.Integer(string="Water Full Amount", compute='_compute_full_watering')
    # active=fields.Boolean(string='Active',default=0)
    # SEASONS = [
    #     ('spring', 'Spring'),
    #     ('summer', 'Summer'),
    #     ('autumn', 'Autumn'),
    #     ('winter', 'Winter'),
    # ]
    # season = fields.Selection(SEASONS, string='Season', required=True)
    # creater_user_id=fields.Many2one('res.users', string='Creater User')
    # models_id = fields.Many2one('flowers_shop_module.model', string="Model Type")
    # name = fields.Char(related='models_id.name')
    # description=fields.Html(string='Description')
    # priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    # state = fields.Selection([('planted', 'Planted'), ('not_planted', 'Not Planted'), ('sold', 'Sold'), ('canceled', 'Canceled')], string='Status',
    #                          default='planted',required='1')
    #
    # @api.depends('watering_frequency','watering_amount_ml')
    # def _compute_full_watering(self):
    #     # print("here ", self)
    #     for a in self:
    #         if a.watering_amount_ml and a.watering_frequency:
    #             a.water_full_amount= a.watering_amount_ml * a.watering_frequency
    #         else:
    #             a.water_full_amount =0
    #
    # @api.onchange('models_id')
    # def onchange_model_id(self):
    #     self.name="model name is changed!"

    # def object_btn_clicked(self):
    #     print("the object button is clicked!!!")
        # return {
        #     'effect': {
        #         'fadeout': 'slow',
        #         'type': 'rainbow_man',
        #         'message': 'Successfully Button Clicked!',
        #     }
        # }

