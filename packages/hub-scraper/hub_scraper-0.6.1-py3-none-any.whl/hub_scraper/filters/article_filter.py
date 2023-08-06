from abc import ABC, abstractmethod
from typing import Optional

from hub_scraper.models import ArticleListing


class ArticleFilter(ABC):
    def __init__(self, *args):
        pass

    def __repr__(self):
        return self.__class__.__name__

    @abstractmethod
    def filter_article(self, articles: ArticleListing) -> Optional[ArticleListing]:
        ...
