from odoo import models, fields,api
class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['mail.thread']
    name = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Publication Date')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('available', 'Available'),
            ('borrowed', 'Borrowed'),
            ('lost', 'Lost'),
        ],
        string='Status',
        default='available',
        tracking=True
    )
    borrow_ids = fields.One2many('library.borrow', 'book_id', string='Borrowed')

    borrow_count = fields.Integer(
        string='Borrow Count',
        compute='_compute_borrow_count'
    )

    @api.depends('borrow_ids')
    def _compute_borrow_count(self):
        for record in self:
            record.borrow_count = len(record.borrow_ids)

    _isbn_unique = models.Constraint(
        'UNIQUE(isbn)',
        'ISBN must be unique.'
    )

    def get_available_books(self):
       books = self.env['library.book'].search([('state', '=', 'available')])
       return books

    @api.model_create_multi
    def create(self, vals_list):
        res = super(LibraryBook, self).create(vals_list)
        return res

    def borrow_book(self):
        book =self.env['library.book'].search([('name', '=', 'Clean Code')], limit=1)
        book.write({'state':'borrowed'})
        return book

    def write(self, vals):
        res = super(LibraryBook, self).write(vals)
        return res

    def unlink(self):
        res =super(LibraryBook,self).unlink()
        return res
