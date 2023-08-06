import asyncio

from functools import wraps
from typing import Optional

import click

from hub_scraper.indexers import indexer
from hub_scraper.models import DataFolder, Hub
from hub_scraper.scraper import HabrScraper

from .utils import get_article_filters


def coro(f):
    """
    Make click async:
    https://github.com/pallets/click/issues/85
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command()
@coro
@click.option(
    "-h",
    "--hub",
    help="Hub name, e.g. 'python' ",
    type=str,
    required=True,
)
@click.option(
    "-of",
    "--output-folder",
    help="Folder to save scraped data, e.g. /home/user/data",
    type=str,
    required=True,
)
@click.option(
    "-t",
    "--threads",
    help="Number async requests to the website, default: 1",
    type=int,
    required=False,
    default=1,
)
@click.option(
    "-d",
    "--time-delay",
    help="Time delay between requests to the website, default: 1",
    type=int,
    required=False,
    default=1,
)
@click.option(
    "-mp",
    "--max-page",
    help="Max page to scrape, default: 50",
    type=int,
    required=False,
    default=50,
)
@click.option(
    "--filter-min-datetime",
    help="Filter articles by min date and time of publications, e.g. 'dd-mm-yyyy hh:mm', default: None",
    type=str,
    required=False,
    default=None,
)
@click.option(
    "--filter-post-type",
    help="List of post types to include articles, e.g. 'article, news', default: article",
    type=str,
    required=False,
    default="article",
)
@click.option(
    "--filter-up-votes-count",
    help="Filter articles by minimum up-votes count, default: 0",
    type=int,
    required=False,
    default=0,
)
async def main(
    hub: str,
    output_folder: str,
    threads: int,
    time_delay: float,
    max_page: int,
    filter_min_datetime: Optional[str],
    filter_post_type: Optional[str],
    filter_up_votes_count: int,
):
    hub_settings = Hub(
        hub_name=hub,
        threads_number=threads,
        time_delay=time_delay,
        max_page=max_page,
        min_up_votes=filter_up_votes_count,
    )
    data_folder = DataFolder(output_folder)
    article_filters = get_article_filters(
        filter_min_datetime=filter_min_datetime,
        filter_post_type=filter_post_type,
    )
    scraper = HabrScraper(hub_settings, article_filters, data_folder)  # type: ignore
    articles = scraper.get_articles()
    async for i in articles:
        if i is None:
            continue
        await i.save()
    index_maker = indexer("default-obsidian", data_folder)
    await index_maker.make_index()


if __name__ == "__main__":
    main()
