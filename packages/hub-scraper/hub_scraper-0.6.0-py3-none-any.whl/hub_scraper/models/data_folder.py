from pathlib import Path
from typing import List

from hub_scraper import conf


class DataFolder:
    articles_folder_name = conf.ARTICLES_FOLDER_NAME
    index_folder_name = conf.INDEX_FOLDER_NAME

    def __init__(self, data_folder: str):
        self.data_folder = Path(data_folder)
        self._create_folders()

    @property
    def articles_folder(self) -> Path:
        return self.data_folder / self.articles_folder_name

    @property
    def index_folder(self) -> Path:
        return self.data_folder / self.index_folder_name

    def _create_folders(self):
        self.articles_folder.mkdir(parents=True, exist_ok=True)
        self.index_folder.mkdir(parents=True, exist_ok=True)

    def get_article_folders(self) -> List[Path]:
        return [i for i in self.articles_folder.iterdir() if i.is_dir()]
