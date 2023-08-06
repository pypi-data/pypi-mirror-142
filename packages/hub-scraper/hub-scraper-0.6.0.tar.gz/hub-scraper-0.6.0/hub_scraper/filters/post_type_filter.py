from typing import Optional

from hub_scraper.models import ArticleListing

from .article_filter import ArticleFilter


class PostTypeFilter(ArticleFilter):
    def __init__(self, *args):
        self.article_types = set(*args)
        super().__init__(*args)

    def filter_article(self, article: ArticleListing) -> Optional[ArticleListing]:
        if article.post_type in self.article_types:
            return article
        return None
