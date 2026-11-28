from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_edge_browser
from selenium.webdriver.common.by import By
import time


class AuthorBaseTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = make_edge_browser()
        return super().setUp()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def sleep(self, duration=5):
        time.sleep(duration)
        
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(By.XPATH, f'.//input[@placeholder="{placeholder}"]')
    
