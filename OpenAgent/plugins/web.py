# scop: inline
# SPDX-License-Identifier: MIT

from __future__ import annotations

import html
import re
from typing import Any
from urllib.parse import quote


class WebPlugin:
    name = "web"
    version = "0.2.0"
    author = "@dev_dolbaeb"
    description = "Web search and URL fetch tools"

    tool_registry = (
        "web.search",
        "web.fetch_url",
        "web.read_html",
        "web.extract_links",
        "web.summarize_page",
    )

    tool_map = {
        "web_search": "cmd_web",
        "web.search": "cmd_web",
        "web.fetch_url": "cmd_web",
        "web.read_html": "cmd_web",
        "web.extract_links": "cmd_web",
        "web.summarize_page": "cmd_web",
    }

    tool_docs = {
        "web.search": {"desc": "Search the web or fetch a URL", "args": "query (str) or q (str) or url (str) — search query or web page URL", "body": "query or URL"},
        "web.fetch_url": {"desc": "Fetch and return text content of a URL", "args": "url (str) — the web page to fetch", "body": "URL"},
        "web.read_html": {"desc": "Fetch a URL and extract readable text from HTML", "args": "url (str) — page to read", "body": "URL"},
        "web.extract_links": {"desc": "Fetch a URL and extract all links", "args": "url (str) — page to scan", "body": "URL"},
        "web.summarize_page": {"desc": "Fetch a URL and return its content as plain text", "args": "url (str) — page to summarize", "body": "URL"},
    }

    config_defaults = {
        "web_timeout": 30,
    }

    def __init__(self, agent: Any) -> None:
        self.agent = agent

    def _looks_like_url(self, value: str) -> bool:
        value = value.strip()
        if value.startswith(("http://", "https://")):
            return True
        import re as _re
        return bool(_re.match(r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)+(?:\/[^\s]*)?$", value))

    def _html_to_text(self, value: str) -> str:
        value = re.sub(r"<script\b[^>]*>.*?</script>", " ", value, flags=re.I | re.S)
        value = re.sub(r"<style\b[^>]*>.*?</style>", " ", value, flags=re.I | re.S)
        value = re.sub(r"<[^>]+>", " ", value)
        value = re.sub(r"\s+", " ", value)
        value = re.sub(r"&amp;", "&", value)
        value = re.sub(r"&lt;", "<", value)
        value = re.sub(r"&gt;", ">", value)
        value = re.sub(r"&quot;", '"', value)
        value = re.sub(r"&#x27;", "'", value)
        value = re.sub(r"&#x2F;", "/", value)
        value = re.sub(r"&nbsp;", " ", value)
        return value.strip()[:12000]
    
    async def cmd_web(self, tool_name: str, attrs_raw: str, body: str) -> str:
        import aiohttp
        attrs = self.agent._parse_xml_attrs(attrs_raw)
        query = (
            body.strip()
            or attrs.get("url")
            or attrs.get("query")
            or attrs.get("q")
            or attrs.get("text")
            or ""
        )
        if not query:
            return "query or url is required"
        
        query = query.strip()
        if self._looks_like_url(query):
            url = query if query.startswith(("http://", "https://")) else "https://" + query
            headers = {"User-Agent": "Mozilla/5.0"}
            timeout = aiohttp.ClientTimeout(total=int(self.agent.config.get("web_timeout", 30) or 30))
            async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session:
                async with session.get(url, allow_redirects=True) as resp:
                    text = await resp.text(errors="replace")
                    if resp.status >= 400:
                        raise RuntimeError(f"Fetch HTTP {resp.status}: {text[:500]}")
                    content_type = resp.headers.get("Content-Type", "")
            if "html" in content_type.lower():
                return f"Fetched URL: {url}\n\n" + self._html_to_text(text)
            return f"Fetched URL: {url}\nContent-Type: {content_type}\n\n{text[:12000]}"
        
        url = f"https://duckduckgo.com/html/?q={quote(query)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        timeout = aiohttp.ClientTimeout(total=int(self.agent.config.get("web_timeout", 30) or 30))
        async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session:
            async with session.get(url) as resp:
                text = await resp.text()
                if resp.status >= 400:
                    raise RuntimeError(f"Search HTTP {resp.status}: {text[:500]}")
        
        results = []
        blocks = re.findall(
            r'<a[^>]+class="result__a"[^>]*>(.*?)</a>.*?class="result__snippet"[^>]*>(.*?)</a>',
            text,
            flags=re.DOTALL | re.I,
        )
        if not blocks:
            blocks = re.findall(
                r'<a[^>]+class="result__a"[^>]*>(.*?)</a>',
                text,
                flags=re.DOTALL | re.I,
            )
            blocks = [(title, "") for title in blocks]
        
        result_lines = []
        for title, snippet in blocks[:5]:
            title_text = html.unescape(re.sub(r"<[^>]+>", "", title)).strip()
            snippet_text = html.unescape(re.sub(r"<[^>]+>", "", snippet)).strip()
            if title_text:
                result_lines.append(f"- {title_text}: {snippet_text}".strip())
        return "\n".join(result_lines) or "No search results found"
