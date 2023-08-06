from abc import ABC, abstractmethod

from hub_scraper.models import DataFolder


class Indexer(ABC):
    def __init__(self, data_folder: DataFolder, **kwargs):
        self.data_folder = data_folder
        self.kwargs = kwargs

    @abstractmethod
    async def make_index(self):
        pass
