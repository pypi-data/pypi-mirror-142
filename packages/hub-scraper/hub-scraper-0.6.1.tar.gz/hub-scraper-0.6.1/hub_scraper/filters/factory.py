from enum import Enum, auto

from .article_filter import ArticleFilter
from .existed_filter import ExistedFilter
from .min_datetime_filter import MinDateTimeFilter
from .post_type_filter import PostTypeFilter


class ArticleFilterType(Enum):
    """
    Enum of all possible article filters
    """

    min_datetime_filter = auto()
    post_type_filter = auto()
    existed_filter = auto()


FILTERS = {
    ArticleFilterType.min_datetime_filter: MinDateTimeFilter,
    ArticleFilterType.post_type_filter: PostTypeFilter,
    ArticleFilterType.existed_filter: ExistedFilter,
}


def get_filter(*args, filter_type: ArticleFilterType) -> ArticleFilter:
    """
    Returns a filter function for a given filter type
    """
    try:
        return FILTERS[filter_type](*args)  # type: ignore
    except KeyError:
        raise ValueError(f"No filter for type {filter_type}")
