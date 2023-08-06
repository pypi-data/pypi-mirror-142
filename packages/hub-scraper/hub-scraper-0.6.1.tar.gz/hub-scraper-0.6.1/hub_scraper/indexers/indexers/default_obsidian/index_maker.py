import asyncio

from typing import List

from aiofile import async_open
from loguru import logger

from hub_scraper import conf
from hub_scraper.indexers.indexer import Indexer

from .models import Metas, Tag


class DefaultObsidian(Indexer):
    async def make_index(self):
        meta_data = await self._get_metas()
        sorted_metas = meta_data.sort_by_tags()
        sorted_tags = sorted(list(sorted_metas.keys()))

        tasks = [self._save_table(tag, sorted_metas[tag]) for tag in sorted_tags]
        tasks.append(self._make_index_file(sorted_tags))
        await asyncio.gather(*tasks)

    async def _make_index_file(self, tags: List[Tag]):
        filepath = self.data_folder.data_folder.joinpath(conf.INDEX_FILE_NAME)
        async with async_open(filepath, "w") as f:
            for tag in tags:
                hub_index = f"{conf.INDEX_FOLDER_NAME}/{tag.slug}.md"
                line = f"- [[{hub_index} | {tag.name}]]\n"
                await f.write(line)

    async def _get_metas(self) -> Metas:
        article_folders = self.data_folder.get_article_folders()
        metas = await Metas.from_folders(article_folders)
        return metas

    async def _save_table(self, tag: Tag, metas: Metas):
        logger.info(f"Saving index for {tag}")
        filepath = self.data_folder.index_folder.joinpath(tag.filename)
        async with async_open(filepath, "w") as f:
            await f.write(f"# {tag.name}\n")

            for meta in metas:
                article_filepath = (
                    f"../{conf.ARTICLES_FOLDER_NAME}/{meta.id}/{conf.ARTICLE_FILE_NAME}"
                )
                line = f"- [[{article_filepath} | {meta.title}]]\n"
                await f.write(line)
