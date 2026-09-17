from odoo import models, fields ,api
from datetime import timedelta
from odoo.exceptions import ValidationError

class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library Borrow'

    book_id = fields.Many2one( 'library.book',string='Book',  required=True )
    member_id = fields.Many2one( 'res.partner',string='Member', required=True )
    borrow_date = fields.Date( string='Borrow Date',  required=True)
    return_date = fields.Date( string='Return Date'  )
    @api.onchange('borrow_date')
    def onchange_borrow_date(self):
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=14)

    @api.constrains('book_id')
    def _check(self):
        if self.book_id.state == 'borrowed':
            raise ValidationError('This book cannot be borrowed')

    def _check_lost(self):
        limit_date =fields.Date.today() - timedelta(days=30)
        borrow_date = self.search([('borrow_date', '<=', limit_date)])
        for borrow_date in borrow_date:
            borrow_date.book_id.write({'state': 'lost'})
