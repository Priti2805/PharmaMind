from playwright.sync_api import (
    sync_playwright
)

from bs4 import BeautifulSoup

from utils.parser import (
    parse_salt_info
)


def scrape_apollo(url):

    data = {

        "Brand Name": "",
        "Clean Brand Name": "",
        "API": "",
        "Strength": "",
        "Dosage Form": "",
        "Manufacturer": "",
        "Salt": "",
        "API Grade": "Unknown",
        "Source": "Apollo",
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
                wait_until="networkidle",
                timeout=30000
            )

            page.wait_for_timeout(
                3000
            )

            soup = BeautifulSoup(
                page.content(),
                "html.parser"
            )

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

            # Composition

            for i, line in enumerate(
                lines
            ):

                if (
                    "composition"
                    in line.lower()
                ):

                    if (
                        i + 1
                        < len(lines)
                    ):

                        data["Salt"] = (
                            lines[i + 1]
                        )

                    break

            # Manufacturer

            for i, line in enumerate(
                lines
            ):

                if (
                    "manufacturer/marketer"
                    in line.lower()
                ):

                    if (
                        i + 1
                        < len(lines)
                    ):

                        data["Manufacturer"] = (
                            lines[i + 1]
                        )

                    break

            # Parse Salt

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


def get_apollo_substitutes(url):

    substitutes = []

    parent_brand = ""

    dosage_forms = [

        "TABLET",
        "CAPSULE",
        "INJECTION",
        "DROPS",
        "CREAM",
        "OINTMENT",
        "GEL",
        "SPRAY",
        "LOTION",
        "SYRUP",
        "SUSPENSION"

    ]

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        try:

            page.goto(
                url,
                wait_until="networkidle",
                timeout=30000
            )

            page.wait_for_timeout(
                5000
            )

            soup = BeautifulSoup(
                page.content(),
                "html.parser"
            )

            h1 = soup.find("h1")

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

            for i, line in enumerate(
                lines
            ):

                if (
                    "all substitutes"
                    in line.lower()
                ):

                    start_idx = i

                    break

            if start_idx is not None:

                i = start_idx + 1

                while i < len(lines):

                    if (

                        "habit forming"
                        in lines[i].lower()

                        or

                        "faqs"
                        in lines[i].lower()

                    ):

                        break

                    if any(

                        form in lines[i].upper()

                        for form in dosage_forms

                    ):

                        brand = lines[i]

                        manufacturer = ""

                        if (
                            i + 1
                            < len(lines)
                        ):

                            manufacturer = (
                                lines[i + 1]
                            )

                        substitutes.append(
                            {

                                "Parent Brand":
                                parent_brand,

                                "Substitute Brand":
                                brand,

                                "Manufacturer":
                                manufacturer,

                                "Source":
                                "Apollo"

                            }
                        )

                    i += 1

        except Exception as e:

            print(
                f"Apollo Substitute Error: {e}"
            )

        browser.close()

    return substitutes