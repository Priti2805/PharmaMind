# -*- coding: utf-8 -*-

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

from scrapers.one_mg import (
    scrape_1mg,
    get_1mg_substitutes
)

from scrapers.apollo import (
    scrape_apollo
)


class ScrapingAgent:

    def scrape_url(
        self,
        url
    ):

        try:

            if (
                "apollo"
                in url.lower()
            ):

                return scrape_apollo(
                    url
                )

            return scrape_1mg(
                url
            )

        except Exception as e:

            print(
                f"Scraping Error: {e}"
            )

            return None

    def scrape_substitutes(
        self,
        url
    ):

        try:

            if (
                "1mg.com"
                in url.lower()
            ):

                return get_1mg_substitutes(
                    url
                )

            return []

        except Exception as e:

            print(
                f"Substitute Error: {e}"
            )

            return []

    def run(
        self,
        urls,
        limit=None
    ):

        if limit:

            urls = urls[:limit]

        print(
            f"Scraping {len(urls)} URLs..."
        )

        results = []

        with ThreadPoolExecutor(
            max_workers=15
        ) as executor:

            futures = [

                executor.submit(
                    self.scrape_url,
                    url
                )

                for url in urls

            ]

            for future in as_completed(
                futures
            ):

                result = (
                    future.result()
                )

                if result:

                    results.append(
                        result
                    )

                    print(
                        f"Scraped: {len(results)}"
                    )

        return results