from odoo.tests.common import TransactionCase
class TestLibraryBook(TransactionCase):
    def create_book(self):
        book = self.env['library.book'].create({'name': 'Test Book',
        'author': 'Test Author',
        'isbn': 'TEST-001',})
        self.assertEqual(book.state, 'draft')
        book.state = 'available'
        self.assertEqual(book.state, 'available')

