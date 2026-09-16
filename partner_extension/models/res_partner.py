from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = ['res.partner']
    library_member = fields.Boolean(string="Library Member")
    membership_date = fields.Date(string="Membership Date")
