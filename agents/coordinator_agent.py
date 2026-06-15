# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:50:18 2026

@author: user
"""

from agents.search_agent import (
    SearchAgent
)

from agents.scraping_agent import (
    ScrapingAgent
)


class CoordinatorAgent:

    def __init__(self):

        self.search_agent = (
            SearchAgent()
        )

        self.scraping_agent = (
            ScrapingAgent()
        )

    def run(
        self,
        medicine_name
    ):

        search_result = (
            self.search_agent.run(
                medicine_name
            )
        )

        print(
            "Starting Scraping..."
        )

        products = (
            self.scraping_agent.run(
                search_result["urls"],
                limit=None
            )
        )

        substitutes = []

        for url in search_result[
            "urls"
        ][:5]:

            substitutes.extend(

                self.scraping_agent
                .scrape_substitutes(
                    url
                )

            )

        print(
            f"Scraping Finished. Products={len(products)}"
        )

        print(
            f"Substitutes Found={len(substitutes)}"
        )

        return {

            "products": products,

            "substitutes": substitutes

        }