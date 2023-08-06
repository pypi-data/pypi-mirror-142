from pathlib import Path
from typing import Optional, Set

from hub_scraper.models import ArticleListing

from .article_filter import ArticleFilter


class ExistedFilter(ArticleFilter):
    def __init__(self, *args):
        self.data_folder = args[0]
        if not isinstance(self.data_folder, Path):
            raise TypeError("data_folder must be a Path object")

        super().__init__(*args)

        self.existed_articles_id = self._get_existed_articles_id()

    def filter_article(self, article: ArticleListing) -> Optional[ArticleListing]:
        if article.id not in self.existed_articles_id:
            return article
        return None

    def _get_existed_articles_id(self) -> Set[str]:
        ids = set([i.name for i in self.data_folder.iterdir() if i.is_dir()])
        return ids
