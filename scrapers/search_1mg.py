# from urllib.parse import quote

# from playwright.sync_api import (
#     sync_playwright
# )

# from bs4 import BeautifulSoup


# def search_1mg(search_term):

#     all_urls = []

#     search_url = (
#         "https://www.1mg.com/search/all?name="
#         + quote(search_term)
#     )

#     with sync_playwright() as p:

#         browser = p.chromium.launch(
#             headless=True
#         )

#         page = browser.new_page()

#         try:

#             page.goto(
#                 search_url,
#                 wait_until="networkidle"
#             )

#             page.wait_for_timeout(
#                 3000
#             )

#             # INFINITE SCROLL
#             last_height = 0

#             for _ in range(100):

#                 page.evaluate(
#                     """
#                     window.scrollTo(
#                         0,
#                         document.body.scrollHeight
#                     )
#                     """
#                 )

#                 page.wait_for_timeout(
#                     2000
#                 )

#                 new_height = page.evaluate(
#                     """
#                     document.body.scrollHeight
#                     """
#                 )

#                 if (
#                     new_height
#                     == last_height
#                 ):

#                     break

#                 last_height = new_height

#             html = page.content()

#             soup = BeautifulSoup(
#                 html,
#                 "html.parser"
#             )

#             links = soup.find_all(
#                 "a"
#             )

#             for link in links:

#                 href = link.get(
#                     "href"
#                 )

#                 if (
#                     href
#                     and "/drugs/" in href
#                 ):

#                     full_url = (
#                         "https://www.1mg.com"
#                         + href
#                     )

#                     all_urls.append(
#                         full_url
#                     )

#         except Exception as e:

#             print(
#                 f"Error: {e}"
#             )

#         browser.close()

#     all_urls = list(
#         dict.fromkeys(
#             all_urls
#         )
#     )

from urllib.parse import quote

from playwright.sync_api import (
    sync_playwright
)

from bs4 import BeautifulSoup


def search_1mg(search_term):

    all_urls = []

    search_url = (
        "https://www.1mg.com/search/all?name="
        + quote(search_term)
    )

    print(f"\nSearch URL: {search_url}")

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        try:

            page.goto(
                search_url,
                wait_until="networkidle",
                timeout=60000
            )

            page.wait_for_timeout(
                3000
            )

            print("\nStarting scroll...\n")

            # INFINITE SCROLL DEBUG
           
            last_height = 0
            same_height_count = 0


            for i in range(100):

                page.evaluate(
                    """
                    window.scrollTo(
                        0,
                        document.body.scrollHeight
                    )
                    """
                )

                page.wait_for_timeout(
                    6000
                )

                links_count = page.locator(
                    "a[href*='/drugs/']"
                ).count()

                new_height = page.evaluate(
                    """
                    document.body.scrollHeight
                    """
                )

                print(
                    f"Scroll {i} | "
                    f"Height={new_height} | "
                    f"DrugLinks={links_count}"
                )

                if new_height == last_height:

                    same_height_count += 1
                
                else:
                
                    same_height_count = 0
                
                if same_height_count >= 5:
                
                    print(
                        "\nScrolling stopped\n"
                    )
                
                    break
                
                last_height = new_height

                

            html = page.content()
            print("=" * 50)
            print("HTML LENGTH:", len(html))
            print(html[:2000])
            print("=" * 50)

            # SAVE PAGE FOR INSPECTION
            with open(
                "dexa_search.html",
                "w",
                encoding="utf-8"
            ) as f:

                f.write(html)

            print(
                "HTML saved -> dexa_search.html"
            )

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            links = soup.find_all(
                "a"
            )

            print(
                f"\nTotal <a> tags found: "
                f"{len(links)}"
            )

            for link in links:

                href = link.get(
                    "href"
                )

                if (
                    href
                    and "/drugs/" in href
                ):

                    if href.startswith(
                        "http"
                    ):

                        full_url = href

                    else:

                        full_url = (
                            "https://www.1mg.com"
                            + href
                        )

                    all_urls.append(
                        full_url
                    )

            all_urls = list(
                dict.fromkeys(
                    all_urls
                )
            )

            print(
                f"\nUnique Drug URLs Found: "
                f"{len(all_urls)}"
            )

            print(
                "\nFirst 20 URLs:\n"
            )

            for url in all_urls[:20]:

                print(url)

        except Exception as e:

            print(
                f"Error: {e}"
            )

        browser.close()

    return all_urls


if __name__ == "__main__":

    urls = search_1mg(
        "Dexamethasone"
    )

    print(
        f"\nFinal URL Count: "
        f"{len(urls)}"
    )

#     return all_urls


# # if __name__ == "__main__":

# #     urls = search_1mg(
# #         "Dexamethasone Dipropionate"
# #     )

# #     print(
# #         f"\nFound {len(urls)} URLs\n"
# #     )

# #     for url in urls:

# #         print(url)
