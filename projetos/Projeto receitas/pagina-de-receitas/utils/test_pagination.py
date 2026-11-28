from unittest import TestCase
from utils.pagination import make_pagination_range


class TestPagination(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
        
    def test_make_pagination_range_first_range_is_static_if_current_page_is_less_than_middle_pages(self):
        # A janela inicial permanece fixa até a página atual ultrapassar o centro.
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
        

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
        


        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=3,
        )['pagination']
        self.assertEqual([ 2, 3, 4, 5], pagination)
        


        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=4,
        )['pagination']
        self.assertEqual([ 3, 4, 5, 6], pagination)
        
        
    def test_make_pagination_range_sure_middle_ranges_are_correct(self):



        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=10,
        )['pagination']
        self.assertEqual([ 9, 10, 11, 12], pagination)
        


        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            window_size=4,
            current_page=12,
        )['pagination']
        self.assertEqual([ 11, 12, 13, 14], pagination)
        
    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # A janela final permanece fixa quando a página atual chega ao fim.

        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        window_size=4,
        current_page=18,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
                


        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        window_size=4,
        current_page=19,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
        


        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        window_size=4,
        current_page=20,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
        


        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        window_size=4,
        current_page=21,
        )['pagination']
        self.assertEqual([ 17, 18, 19, 20], pagination)
    

    def test_make_pagination_range_has_items_on_page(self):
        items = list(range(1, 11))
        self.assertEqual(10, len(items))
