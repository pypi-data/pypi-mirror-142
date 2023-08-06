from datetime import datetime
from typing import List

from pydantic import BaseModel

from .article_author import Author


class ArticleMeta(BaseModel):
    id: str
    url: str
    time_published: datetime
    is_corporative: bool
    lang: str
    title: str
    description: str
    author: Author
    tags: List[str]

    def __repr__(self):
        return f"<ArticleMeta {self.title}>"

    @property
    def tags_as_string(self) -> str:
        return ", ".join(self.tags)
