from dataclasses import dataclass
from typing import List, Optional
from urllib.parse import urlencode


@dataclass()
class Hub:
    hub_name: str
    threads_number: int
    time_delay: float
    max_page: int
    min_up_votes: Optional[int]
    _max_pages: int = 50
    _base_api_url: str = "https://habr.com/kek/v2/articles/?{params}"

    def get_page_url(self, page_number: int) -> Optional[str]:
        if page_number > self._max_pages:
            return None

        url_params = self._get_url_params(page_number)
        url = self._base_api_url.format(params=url_params)
        return url

    def _get_url_params(self, page_number: int) -> str:
        # hub=python&sort=all&fl=ru&hl=ru&page=1
        url_params = {
            "hub": self.hub_name,
            "sort": "all",
            "fl": "ru",
            "hl": "ru",
            "page": page_number,
        }
        if self.min_up_votes:
            url_params["score"] = self.min_up_votes

        return urlencode(url_params)

    def listing_pages_generator(self) -> List[str]:
        urls = []
        for page_number in range(1, self.max_page + 1):
            url = self.get_page_url(page_number)
            if url:
                urls.append(url)
        return urls
