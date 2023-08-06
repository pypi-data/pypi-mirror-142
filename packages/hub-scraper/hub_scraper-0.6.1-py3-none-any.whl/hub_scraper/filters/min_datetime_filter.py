from datetime import datetime
from typing import Optional

from hub_scraper.models import ArticleListing

from .article_filter import ArticleFilter


class MinDateTimeFilter(ArticleFilter):
    def __init__(self, *args):
        self.threshold: datetime = args[0]

        if not isinstance(self.threshold, datetime):
            raise ValueError(
                "MinDateTimeFilter requires a datetime object as threshold"
            )

        super().__init__(*args)

    def filter_article(self, article: ArticleListing) -> Optional[ArticleListing]:
        if article.time_published >= self.threshold:
            return article
        return None
