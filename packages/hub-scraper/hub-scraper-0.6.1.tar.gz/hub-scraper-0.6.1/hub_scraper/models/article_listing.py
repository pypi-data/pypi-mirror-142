from __future__ import annotations

from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Author(BaseModel):
    id: str
    alias: str
    fullname: Optional[str] = None
    avatar_url: str = Field(..., alias="avatarUrl")
    speciality: str


class Statistics(BaseModel):
    comments_count: int = Field(..., alias="commentsCount")
    favorites_count: int = Field(..., alias="favoritesCount")
    reading_count: int = Field(..., alias="readingCount")
    score: int
    votes_count: int = Field(..., alias="votesCount")


class Hub(BaseModel):
    related_data: Any = Field(..., alias="relatedData")
    id: str
    alias: str
    type: str
    title: str
    title_html: str = Field(..., alias="titleHtml")
    is_profiled: bool = Field(..., alias="isProfiled")


class Flow(BaseModel):
    id: str
    alias: str
    title: str


class LeadData(BaseModel):
    text_html: str = Field(..., alias="textHtml")
    image_url: Any = Field(..., alias="imageUrl")
    button_text_html: str = Field(..., alias="buttonTextHtml")
    image: Any


class Tag(BaseModel):
    title_html: str = Field(..., alias="titleHtml")


class ArticleListing(BaseModel):
    id: str
    time_published: datetime = Field(..., alias="timePublished")
    is_corporative: bool = Field(..., alias="isCorporative")
    lang: str
    title_html: str = Field(..., alias="titleHtml")
    post_type: str = Field(..., alias="postType")
    author: Author
    statistics: Statistics
    hubs: List[Hub]
    flows: List[Flow]
    tags: List[Tag]

    @property
    def article_url(self) -> str:
        return f"https://habr.com/{self.lang}/post/{self.id}/"
