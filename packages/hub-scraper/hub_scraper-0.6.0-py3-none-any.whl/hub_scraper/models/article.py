import asyncio
import re

from pathlib import Path
from typing import Optional, Protocol

import chompjs
import lxml.html as lh

from aiofile import async_open
from loguru import logger
from markdownify import markdownify

from hub_scraper import conf

from .article_author import Author
from .article_meta import ArticleMeta


RE_SCRIPT = re.compile(r"window.__INITIAL_STATE__=(.*);")


class Response(Protocol):
    text: str
    status_code: int
    url: str


class Article:
    def __init__(self, meta: ArticleMeta, text_html: str, output_folder: Path):
        self.meta = meta
        self.text_html = text_html
        self.article_folder = self._get_article_folder(output_folder)

    def __repr__(self) -> str:
        return f"<Article {self.meta.title}>"

    @property
    def text_md(self) -> str:
        dt = self.meta.time_published.strftime("%Y-%m-%d %H:%M")
        title = f"[{self.meta.title}]({self.meta.url})"
        tags = self.meta.tags
        article_text = f"# {title}\n**{self.meta.author.alias} {dt}**\n*{tags}*\n"
        article_text += markdownify(self.text_html)
        return article_text

    @classmethod
    def from_response(
        cls, response: Response, articles_output_folder: Path
    ) -> Optional["Article"]:
        if response is None or response.status_code >= 400:
            return None

        html = lh.fromstring(response.text)
        script_txt = "window.__INITIAL_STATE__="
        script = html.xpath(".//script[contains(text(), '" + script_txt + "')]/text()")[
            0
        ].strip()
        js_data = RE_SCRIPT.match(script).group(1)  # type: ignore
        raw_data = chompjs.parse_js_object(js_data)
        article_data = raw_data["articlesList"]["articlesList"]
        for _, v in article_data.items():
            author = Author(**v["author"])
            tags = [tag["title"] for tag in v["hubs"] if not tag["isProfiled"]]
            meta = ArticleMeta(
                id=v["id"],
                url=str(response.url),
                time_published=v["timePublished"],
                is_corporative=v["isCorporative"],
                lang=v["lang"],
                title=v["titleHtml"],
                description=v["leadData"]["textHtml"],
                author=author,
                tags=tags,
            )
            return cls(
                meta=meta,
                text_html=v["textHtml"],
                output_folder=articles_output_folder,
            )
        return None

    async def save(self):
        logger.info(f"Saving {self} to {self.article_folder.absolute()}")
        tasks = [self._save_article(), self._save_meta()]
        await asyncio.gather(*tasks)

    async def _save_article(self):
        await self._save_text_data(conf.ARTICLE_FILE_NAME, self.text_md)

    async def _save_meta(self):
        await self._save_text_data(conf.META_FILE_NAME, self.meta.json(indent=4))

    async def _save_text_data(self, filename: str, data: str):
        filepath = self.article_folder.joinpath(filename)
        async with async_open(filepath, "w") as f:
            await f.write(data)

    def _get_article_folder(self, output_folder: Path) -> Path:
        folder = output_folder.joinpath(self.meta.id)
        folder.mkdir(exist_ok=True, parents=True)
        return folder
