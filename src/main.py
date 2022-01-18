from time import sleep, time
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class LinkFinder:
    def __init__(self, sleep_time: int, options=[]):
        self.sleep_time = sleep_time
        self._options = options
        self._driver = Firefox()
        self._site_informations = None

    def _get_target_informations(self):
        start = time()
        number_of_poems = 0

        #  Caso for necessário setar as opções;
        if self._options:
            options = Options()

            for option in self.options:
                options.add_argument(option)

            self._driver = Firefox(options=options)

        self._driver.get('https://www.escritas.org/pt/poemas')
        sleep(self.sleep_time)

        try:
            while True:
                # Instanciando a página e buscando pelos poemas;
                content = BeautifulSoup(self._driver.page_source, 'html.parser')
                father = content.find('div', {'id': 'htmlDiv'})

                # # Altera o número de poemas recebidos;
                number_of_poems = len(father)

                if (len(father) != number_of_poems) and (number_of_poems != 20):
                    self.site_informations = father
                    print(
                        f'😎✌ Sucesso! O script coletou todos os dados do site.\nVocê consegiu informações sobre um total de {number_of_poems} publicações nesse site.')
                    break

                button = self._driver.find_elements_by_tag_name('button')[-1]
                button.click()
                sleep(self.sleep_time / 2)
        except:
            self.site_informations = father
            print(
                f'😢👎 Algo não saiu como planejado. O script se encerrou de forma precoce. Você conseguiu informações sobre um total de {number_of_poems} poemas.')
        finally:
            print(
                f'\n🚀 O tempo total de execução do algoritimo para obtenção dos links foi de {(time() - start):.2f} segundos.')
            return self._site_informations


if __name__ == '__main__':
    finder = LinkFinder(2, ['--headless'])
    finder._get_target_informations()
    print(finder.site_informations.prettify())
