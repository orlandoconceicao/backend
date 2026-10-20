from pathlib import Path
ROOT_PATH = Path(__file__).parent.parent
EDGEDRIVER_NAME = 'msedgedriver.exe'
EDGEDRIVER_PATH = ROOT_PATH / 'bin' / EDGEDRIVER_NAME

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep

# --headless = não abre o navegador mas faz tudo
def make_chrome_browser(*options):
    edge_options = webdriver.EdgeOptions()
    if options is not None:
        for option in options:
            edge_options.add_argument(option)
    
    edge_service = Service(executable_path=EDGEDRIVER_PATH)
    browser = webdriver.Edge(service=edge_service, options=edge_options)
    return browser

if __name__ == '__main__':
    browser = make_chrome_browser('--headless')
    browser.get('https://www.google.com.br/')
    sleep(5)
