# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:54:58 2026

@author: user
"""

from playwright.sync_api import (
    sync_playwright
)

from bs4 import BeautifulSoup

from utils.parser import (
    parse_salt_info
)


def scrape_netmeds(url):

    data = {

        "Brand Name": "",
        "Clean Brand Name": "",
        "API": "",
        "Strength": "",
        "Dosage Form": "",
        "Manufacturer": "",
        "Salt": "",
        "API Grade": "Unknown",
        "Source": "Netmeds",
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
                timeout=15000
            )

            page.wait_for_timeout(
                3000
            )

            html = page.content()

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            print(
                soup.title.text
            )

            text = soup.get_text(
                separator="\n"
            )

            print(
                text[:12000]
            )

        except Exception as e:

            print(e)

        browser.close()

    return data


if __name__ == "__main__":

    result = scrape_netmeds(
        "https://www.netmeds.com/product/dolo-650-tablet-15s-lui1wb-8231049"
    )

    print(result)