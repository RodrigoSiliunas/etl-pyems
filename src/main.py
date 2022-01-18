import pandas as pd
from pymongo import MongoClient
from packages.linkfinder import *
from packages.filemanager import *
from packages.poemextractor import *


if __name__ == '__main__':
    # Obtendo os dados do site https://www.escritas.org/pt com selenium e BSoup4;
    linkFinder = LinkFinder(2)
    poemExtractor = PoemExtractor(linkFinder.get_target_informations())

    # Pega os dados obtidos, formata e transforma em arquivo CSV;
    file = FileManager(poemExtractor.get_poems_data())
    filename = input('Filename: ')
    file.create_csv(filename)

    # Conexão com o MongoDB e acesso a database e collection;
    client = MongoClient('mongodb://localhost:27017/')
    database = client.get_database('flask')
    collection = database.get_collection('poems')

    # Obtendo o path do arquivo a ser lido;
    path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), f"../out/{filename}"))

    csv = pd.read_csv(path, header=0)
    dicionary = csv.to_dict('records')

    # Load das informações obtidas no banco de dados com UPSERT;
    for line in dicionary:
        collection.update_one(
            { "title": line['title'] },
            {
                "$setOnInsert": {
                    "title": line['title'], "author": line['author'], "content": line['content']
                }
            },
            upsert=True
        )
