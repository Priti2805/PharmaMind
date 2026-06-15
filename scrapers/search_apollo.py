from urllib.parse import quote

from playwright.sync_api import (
    sync_playwright
)


def search_apollo(search_term):

    all_urls = []

    search_url = (
        "https://www.apollopharmacy.in/search-medicines/"
        + quote(search_term)
    )

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        try:

            page.goto(
                search_url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(
                8000
            )

            # Scroll to load products

            page.evaluate(
                """
                window.scrollTo(
                    0,
                    document.body.scrollHeight
                )
                """
            )

            page.wait_for_timeout(
                3000
            )

            links = page.locator("a").evaluate_all(
                """
                elements =>
                elements.map(
                    e => e.href
                )
                """
            )

            for href in links:

                if (
                    href
                    and "/medicine/" in href
                ):

                    all_urls.append(
                        href
                    )

        except Exception as e:

            print(
                f"Apollo Search Error: {e}"
            )

        browser.close()

    urls = list(
        dict.fromkeys(
            all_urls
        )
    )

    print(
        f"Apollo Products Found: "
        f"{len(urls)}"
    )

    return urls