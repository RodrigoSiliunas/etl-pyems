# import os
# import pandas as pd
# from time import sleep, time
# from bs4 import BeautifulSoup
# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options

from packages.linkfinder import *
from packages.filemanager import *
from packages.poemextractor import *


if __name__ == '__main__':
    linkFinder = LinkFinder(2)
    poemExtractor = PoemExtractor(linkFinder.get_target_informations())

    file = FileManager(poemExtractor.get_poems_data())
    file.create_csv('poemas.csv')
