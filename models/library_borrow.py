from odoo import models,fields
class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library Borrow'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    member_id = fields.Many2one('res.partner', string='Member', required=True)
    borrow_date = fields.Date(string='Borrow Date',required=True)
    return_date = fields.Date(string='Return Date')