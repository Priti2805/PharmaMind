# from urllib.parse import quote
# import json
# import requests
# from bs4 import BeautifulSoup


# def search_pharmeasy(search_term):

#     urls = []

#     search_url = (
#         f"https://pharmeasy.in/search/all?name={quote(search_term)}"
#     )

#     headers = {
#         "User-Agent":
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
#     }

#     response = requests.get(
#         search_url,
#         headers=headers,
#         timeout=30
#     )

#     print(f"Status Code: {response.status_code}")

#     soup = BeautifulSoup(
#         response.text,
#         "html.parser"
#     )

#     next_data = soup.find(
#         "script",
#         id="__NEXT_DATA__"
#     )

#     if not next_data:

#         print("__NEXT_DATA__ not found")
#         return []

#     data = json.loads(
#         next_data.text
#     )

#     page_props = (
#         data
#         .get("props", {})
#         .get("pageProps", {})
#     )
#     print(
#     "hasMorePages =",
#     page_props.get("hasMorePages")
# )

#     print(
#         "lastFetchedNormalPageNum =",
#         page_props.get("lastFetchedNormalPageNum")
#     )

#     print("\n========== PAGE PROPS KEYS ==========")
#     print(page_props.keys())

#     print("\n========== PAGE PROPS ==========")
#     print(
#         json.dumps(
#             page_props,
#             indent=2
#         )[:10000]
#     )

#     products = page_props.get(
#         "productList",
#         []
#     )

#     print(
#         f"\nProducts Returned: "
#         f"{len(products)}"
#     )

#     for product in products:

#         slug = product.get(
#             "slug",
#             ""
#         )

#         if slug:

#             urls.append(
#                 "https://pharmeasy.in/online-medicine-order/"
#                 + slug
#             )

#     urls = list(
#         dict.fromkeys(urls)
#     )

#     print(
#         f"\nUnique URLs Found: "
#         f"{len(urls)}"
#     )

#     return urls


# if __name__ == "__main__":

#     results = search_pharmeasy(
#         "dexamethasone"
#     )

#     print("\n========== URLS ==========\n")

#     for url in results:
#         print(url)

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json

for page in range(1, 6):

    url = f"https://pharmeasy.in/search/all?name={quote('dexamethasone')}&page={page}"

    print("\nPAGE =", page)

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    next_data = soup.find(
        "script",
        id="__NEXT_DATA__"
    )

    if not next_data:
        print("NO DATA")
        continue

    data = json.loads(next_data.text)

    products = (
        data
        .get("props", {})
        .get("pageProps", {})
        .get("productList", [])
    )

    print("Products =", len(products))

    if len(products):

        print(
            products[0]["name"]
        )