from odoo import models, fields, api
from datetime import datetime, date


class UpdateEffectiveDate(models.TransientModel):
    _name = "update.effective.date"

    date_done = fields.Datetime(string="Effective Date")

    # def update_date_done(self):
    #     picking_id = self.env['stock.picking'].browse(self.env.context.get('active_id'))
    #     if picking_id:
    #         picking_id.date_done = picking_id.scheduled_date

    def update_date_done(self):
        # Get all selected picking records
        picking_ids = self.env.context.get('active_ids', [])
        pickings = self.env['stock.picking'].browse(picking_ids)

        for picking in pickings:
            if picking:
                # Update the 'date_done' field with the scheduled date or a custom date
                picking.date_done = picking.scheduled_date