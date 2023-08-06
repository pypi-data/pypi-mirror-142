from hub_scraper.models import DataFolder

from .indexer import Indexer
from .indexers import DefaultObsidian


INDEXERS = {"default-obsidian": DefaultObsidian}


def indexer(indexer_name: str, data_folder: DataFolder, **kwargs) -> Indexer:
    try:
        return INDEXERS[indexer_name](data_folder, **kwargs)
    except KeyError:
        raise ValueError(
            f"Indexer {indexer_name} not found, indexer name must be one of: {', '.join(INDEXERS.keys())}"
        )
