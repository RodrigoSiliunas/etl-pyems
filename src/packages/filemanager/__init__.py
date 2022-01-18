import os
import pandas as pd


class FileManager:
    def __init__(self, dict_data: dict):
        self._dict_data = dict_data

    def preview_csv(self):
        return pd.DataFrame(data=self._dict_data)

    def create_csv(self, filename: str):
        path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), f"../../../out/{filename}"))
        print(f'🚀 Arquivo CSV gerado com sucesso na pasta out!')
        data = pd.DataFrame(data=self._dict_data)

        return data.to_csv(path, encoding='utf-8-sig')
