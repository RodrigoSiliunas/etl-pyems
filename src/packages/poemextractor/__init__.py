class PoemExtractor:
    def __init__(self, links):
        self._links = links

    def get_poems_data(self):
        # Função que altera letras maiusculas no meio das palavras do texto;
        def __word_changer(word_list: list):
            for i in range(len(word_list)):
                if word_list[i] == word_list[i].capitalize():
                    continue

                for letter in word_list[i]:
                    if letter == letter.upper():
                        word_list[i] = word_list[i].replace(
                            letter, letter.lower())

            return " ".join(word_list)

        data = {'title': [], 'author': [], 'content': []}
        poems = self._links.findAll(
            'div', attrs={'class': 'card border-0 shadow h-100 text-center'})

        for poem in poems:
            data['title'].append(
                poem.find('h5', attrs={'class': 'card-title impact mb-3'}).text)
            data['author'].append(
                poem.find('a', attrs={'class': 'card-header'}).text)

            #  Tratamento dos dados;
            content = poem.find(
                'div', attrs={'class': 'card-text collapse'}).text
            content = content.strip()
            content = content.replace("'\n'", " ")
            content = content.split(" ")
            content = __word_changer(content)

            data['content'].append(content)

        return data
