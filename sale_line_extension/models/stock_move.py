from odoo import models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'
    x_custom_note = fields.Char(
        string='Custom Note',
        related='sale_line_id.x_custom_note',
        store=True,
    )