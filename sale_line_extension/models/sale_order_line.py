from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_custom_note = fields.Char(
        string='Custom Note'
    )