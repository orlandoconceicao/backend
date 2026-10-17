from unittest import TestCase
from utils.pagination import make_pagination_range

class TestPagination(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
        
    def test_make_pagination_range_first_range_is_static_if_current_page_is_less_than_middle_pages(self):
        # current_page = 1, middle page is 2, 
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
        
        # current_page = 2, middle page is 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
        
        # currente_page = 3, middle page is 2
        # here, the first range is [2, 3, 4, 5], because the current page is greater than the middle page
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([ 2, 3, 4, 5], pagination)
        
        # currente_page = 4, middle page is 2
        # here, the first range is [3, 4, 5, 6], because the current page is greater than the middle page
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([ 3, 4, 5, 6], pagination)
        
        
    def test_make_pagination_range_sure_middle_ranges_are_correct(self):

        # currente_page = 10, middle page is 2
        # here, the first range is [2, 3, 4, 5], because the current page is greater than the middle page
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([ 9, 10, 11, 12], pagination)
        
        # currente_page = 12, middle page is 2
        # here, the first range is [3, 4, 5, 6], because the current page is greater than the middle page
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qtd_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([ 11, 12, 13, 14], pagination)
        
    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # currente_page = 18, middle page is 2
        # here, the first range is [3, 4, 5, 6], because the current page is greater than the middle page
        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        qtd_pages=4,
        current_page=18,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
                
        # currente_page = 19, middle page is 2
        # here, the first range is [3, 4, 5, 6], because the current page is greater than the middle page
        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        qtd_pages=4,
        current_page=19,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
        
        # currente_page = 20, middle page is 2
        # here, the first range is [3, 4, 5, 6], because the current page is greater than the middle page
        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        qtd_pages=4,
        current_page=20,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
        
        # currente_page = 21, middle page is 2
        # here, the first range is [3, 4, 5, 6], because the current page is greater than the middle page
        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        qtd_pages=4,
        current_page=21,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
    
    # teste paginação com quantos itens tem na página
    def test_make_pagination_range_has_items_on_page(self):
        items = list(range(1, 11))
        self.assertEqual(10, len(items))
