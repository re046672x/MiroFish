"""
Web Search Service - DuckDuckGo based (no API key required)
"""

import logging
from typing import List, Dict
from duckduckgo_search import DDGS

logger = logging.getLogger(__name__)


class WebSearchService:
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 5, region: str = "wt-wt") -> List[Dict[str, str]]:
        try:
            results = list(self.ddgs.text(keywords=query, max_results=max_results, region=region))
            logger.info(f"Web search: {len(results)} results")
            return results
        except Exception as e:
            logger.error(f"Web search failed: {e}")
            return []

    def search_news(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        try:
            results = list(self.ddgs.news(keywords=query, max_results=max_results))
            logger.info(f"News search: {len(results)} results")
            return results
        except Exception as e:
            logger.error(f"News search failed: {e}")
            return []

    def format_results(self, results: List[Dict[str, str]], search_type: str = "web") -> str:
        if not results:
            return f"No {search_type} results found."
        formatted = []
        for i, r in enumerate(results, 1):
            title = r.get("title", "No title")
            url = r.get("href", r.get("url", ""))
            body = r.get("body", r.get("description", ""))
            formatted.append(f"[{i}] {title}\n    URL: {url}\n    {body}")
        return f"=== Web Search Results ({len(results)} found) ===\n\n" + "\n\n".join(formatted)
