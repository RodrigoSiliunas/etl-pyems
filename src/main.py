from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class LinkFinder:
    def __init__(self, sleep_time: int, options=[]):
        self.sleep_time = sleep_time
        self.options = options
        self.driver = Firefox()

    def _get_target_informations(self):
        number_of_poems = 0
        #  Caso for necessário setar as opções;
        if self.options:
            options = Options()

            for option in self.options:
                options.add_argument(option)

            self.driver = Firefox(options=options)

        self.driver.get('https://www.escritas.org/pt/poemas')
        sleep(self.sleep_time)

        while True:
            # Instanciando a página e buscando pelos poemas;
            content = BeautifulSoup(self.driver.page_source, 'html.parser')
            father = content.find('div', {'id': 'htmlDiv'})

            # # Altera o número de poemas recebidos;
            number_of_poems = len(father)

            if (len(father) != number_of_poems) and (number_of_poems != 20):
                return print(father.prettify())

            button = self.driver.find_elements_by_tag_name('button')[-1]
            button.click()
            sleep(self.sleep_time / 2)


if __name__ == '__main__':
    finder = LinkFinder(3)
    finder._get_target_informations()
