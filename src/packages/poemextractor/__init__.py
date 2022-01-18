class PoemExtractor:
    def __init__(self, links):
        self._links = links

    def get_poems_data(self):
        data = {'title': [], 'author': [], 'content': []}
        poems = self._links.findAll(
            'div', attrs={'class': 'card border-0 shadow h-100 text-center'})

        for poem in poems:
            data['title'].append(
                poem.find('h5', attrs={'class': 'card-title impact mb-3'}).text)
            data['author'].append(
                poem.find('a', attrs={'class': 'card-header'}).text)
            data['content'].append(
                poem.find('div', attrs={'class': 'card-text collapse'}).text)

        return data
