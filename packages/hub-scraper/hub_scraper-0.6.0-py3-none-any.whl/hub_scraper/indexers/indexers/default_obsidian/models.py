import asyncio
import json

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from aiofile import async_open
from loguru import logger

import hub_scraper.indexers.utils as utils

from hub_scraper import conf
from hub_scraper.models import ArticleMeta


@dataclass(frozen=True)
class Tag:
    name: str

    def __lt__(self, other):
        return self.name < other.name

    @property
    def slug(self):
        return utils.transliteration(self.name)

    @property
    def filename(self) -> str:
        return f"{self.slug}.md"


class Metas(List[ArticleMeta]):
    @classmethod
    async def from_folders(cls, article_folders: List[Path]) -> "Metas":
        tasks = [cls._get_meta_from_folder(i) for i in article_folders]
        metas = await asyncio.gather(*tasks)
        return cls(metas)

    @staticmethod
    async def _get_meta_from_folder(article_folder):
        filename = article_folder.joinpath(conf.META_FILE_NAME)
        logger.info(f"Getting meta from {filename}")
        async with async_open(filename, "r") as f:
            meta_data = await f.read()
            js_data = json.loads(meta_data)
        return ArticleMeta(**js_data)

    def sort_by_tags(self) -> Dict[Tag, "Metas"]:
        sorted_metas: Dict[Tag, "Metas"] = defaultdict(self.__class__)
        for i in self:
            if len(i.tags) == 0:
                tag = Tag("Others")
                sorted_metas[tag].append(i)
                continue
            for t in i.tags:
                tag = Tag(t)
                sorted_metas[tag].append(i)
        return sorted_metas
