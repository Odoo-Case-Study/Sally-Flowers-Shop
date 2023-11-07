from odoo import models, fields, api
from datetime import date
class StockProductionLot(models.Model):

    _inherit = 'stock.lot'
  

    water_ids = fields.One2many("flower.water", "serial_id")
    is_flower=fields.Boolean(related='product_id.is_flower')

    def action_water_flower(self):
        flowers = self.filtered(lambda rec: rec.is_flower)
        for record in flowers:
            if record.water_ids:
                last_watered_date = record.water_ids[0].date
                frequency = record.product_id.flower_id.watering_frequency
                today = fields.Date.today()

                # Calculate the number of days since the last watering
                days_since_last_watering = (today - last_watered_date).days

                # Check if it's time to water based on the watering frequency
                if days_since_last_watering < frequency:
                    # If not time to water, skip this flower
                    continue
            else:
            id=record.id
        
            # Create a new flower.water record              
            flower_water_record = self.env["flower.water"].create({'serial_id': id})
            flower_water_records = self.env["flower.water"].search([])
             


    def action_open_watering_times(self):
        action = {
                'name': 'Watering Times',
                'type': 'ir.actions.act_window',
                'res_model': 'flower.water',
                'view_mode': 'tree,form',
                'domain': [('serial_id', '=', self.id)],
                'target': 'current',
            }
        return action

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product = self.env["product.product"].browse(vals["product_id"])
            if product.sequence_id:
                vals["name"] = product.sequence_id.next_by_id()
        return super().create(vals_list)




