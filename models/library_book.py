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

    _sql_constraints = [
        (
            'isbn_unique',
            'UNIQUE(isbn)',
            'ISBN must be unique.'
        ),
    ]

    def get_available_books(self):
       books = self.env['library.book'].search([('state', '=', 'available')])
       return books
    def create_books(self):
       new_books= self.env['library.book'].create({'name':'Clean Code','author':'Robert Martin','isbn':'9780132350884'})
       return new_books

    def borrow_book(self):
        book =self.env['library.book'].search([('name', '=', 'Clean Code')], limit=1)
        book.write({'state':'borrowed'})
        return book

    def delete_book(self):
        book=self.env['library.book'].search([('name', '=', 'Clean Code')], limit=1)
        book.unlink()