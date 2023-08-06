from pathlib import Path
from typing import List, Optional, Protocol

from hub_scraper.models import ArticleListing


class Hub(Protocol):
    threads_number: int
    time_delay: float

    def listing_pages_generator(self) -> List[str]:
        ...


class DataFolder(Protocol):
    articles_folder: Path


class ArticleFilter(Protocol):
    def filter_article(self, article: ArticleListing) -> Optional[ArticleListing]:
        ...
