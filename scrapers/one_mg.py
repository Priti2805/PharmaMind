from playwright.sync_api import (
    sync_playwright
)

from bs4 import BeautifulSoup

from utils.parser import (
    parse_salt_info
)


def scrape_1mg(url):

# =============================================================================
#     data = {
# 
#         "Brand Name": "",
#         "Clean Brand Name": "",
#         "API": "",
#         "Strength": "",
#         "Dosage Form": "",
#         "Manufacturer": "",
#         "Salt": "",
#         "API Grade": "Unknown",
#         "URL": url
# 
#     }
# =============================================================================
    data = {

    "Brand Name": "",
    "Clean Brand Name": "",
    "API": "",
    "Strength": "",
    "Dosage Form": "",
    "Manufacturer": "",
    "Salt": "",
    "API Grade": "Unknown",
    "Source": "1mg",
    "URL": url

}

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        try:

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(
                1000
            )

            html = page.content()

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            # BRAND NAME
            h1 = soup.find("h1")

            if h1:

                data["Brand Name"] = (
                    h1.get_text(
                        strip=True
                    )
                )

            text = soup.get_text(
                separator="\n"
            )

            lines = [

                x.strip()

                for x in text.split("\n")

                if x.strip()

            ]

            # MANUFACTURER
            for i, line in enumerate(
                lines
            ):

                if line == "Marketer":

                    if i + 1 < len(lines):

                        data[
                            "Manufacturer"
                        ] = lines[
                            i + 1
                        ]

                        break

            # SALT DEBUG
            for i, line in enumerate(
                lines
            ):

                if (
                    line
                    == "SALT COMPOSITION"
                ):
                    if (
                        i + 1
                        < len(lines)
                    ):

                        data["Salt"] = (
                            lines[i + 1]
                        )

                    break

            parsed = parse_salt_info(

                data["Salt"],
                data["Brand Name"]

            )

            data["API"] = (
                parsed.get(
                    "API",
                    ""
                )
            )

            data["Strength"] = (
                parsed.get(
                    "Strength",
                    ""
                )
            )

            data["Dosage Form"] = (
                parsed.get(
                    "Dosage Form",
                    ""
                )
            )

            data[
                "Clean Brand Name"
            ] = parsed.get(
                "Clean Brand Name",
                ""
            )

        except Exception as e:

            print(
                f"Error scraping {url}: {e}"
            )

        browser.close()

    return data


def get_1mg_substitutes(url):

    from playwright.sync_api import (
        sync_playwright
    )

    from bs4 import BeautifulSoup

    substitutes = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(
            200
        )

        html = page.content()

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        h1 = soup.find("h1")

        parent_brand = ""

        if h1:

            parent_brand = (
                h1.get_text(
                    strip=True
                )
            )

        text = soup.get_text(
            separator="\n"
        )

        lines = [

            x.strip()

            for x in text.split("\n")

            if x.strip()

        ]

        start_idx = None

        for idx, line in enumerate(
            lines
        ):

            if (
                "For informational purposes only"
                in line
            ):

                start_idx = idx
                break

        if start_idx is not None:

            # Skip:
            # Disclaimer
            # Parent Brand
            # Parent Price

            i = start_idx + 3

            while i + 3 < len(lines):

                try:

                    substitute_name = (
                        lines[i]
                    )

                    manufacturer = (
                        lines[i + 1]
                    )

                    price = (
                        lines[i + 2]
                    )

                    # Stop when substitute section ends

                    if "₹" not in price:

                        break

                    substitutes.append(
                        {
                            "Parent Brand":
                            parent_brand,

                            "Substitute Brand":
                            substitute_name,

                            "Manufacturer":
                            manufacturer,

                            "Source":
                            "1mg"
                        }
                    )

                    i += 4

                except Exception:

                    break

        browser.close()

    return substitutes