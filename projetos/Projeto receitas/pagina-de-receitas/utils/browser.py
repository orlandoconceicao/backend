import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.service import Service


ROOT_PATH = Path(__file__).parent.parent

def make_edge_browser(*options):
    edge_options = webdriver.EdgeOptions()
    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    load_dotenv(ROOT_PATH / '.env')
    if os.environ.get('SELENIUM_HEADLESS') == '1':
        edge_options.add_argument('--headless')

    edge_service = Service()
    browser = webdriver.Edge(service=edge_service, options=edge_options)
    return browser

if __name__ == '__main__':
    browser = make_edge_browser('--headless')
    browser.get('https://www.google.com.br/')
    sleep(5)
