# -*- coding: utf-8 -*-
"""
Created on Mon Jun 8 12:07:56 2026

@author: user
"""

from scrapers.search_1mg import search_1mg
from scrapers.search_apollo import search_apollo


class SearchAgent:

    def __init__(self):

        self.sources = [
            "1mg",
            "apollo"
        ]

    def get_search_term(
        self,
        medicine_name
    ):

        tokens = medicine_name.split()

        if len(tokens) > 1:
            return tokens[0]

        return medicine_name

    def search_1mg_source(
        self,
        medicine_name
    ):

        try:

            urls = search_1mg(
                medicine_name
            )

            return {
                "source": "1mg",
                "urls": urls,
                "count": len(urls)
            }

        except Exception as e:

            print(
                f"1mg Search Error: {e}"
            )

            return {
                "source": "1mg",
                "urls": [],
                "count": 0
            }

    def search_apollo_source(
        self,
        medicine_name
    ):

        try:

            urls = search_apollo(
                medicine_name
            )

            return {
                "source": "apollo",
                "urls": urls,
                "count": len(urls)
            }

        except Exception as e:

            print(
                f"Apollo Search Error: {e}"
            )

            return {
                "source": "apollo",
                "urls": [],
                "count": 0
            }

    def run(
        self,
        medicine_name
    ):

        search_term = (
            self.get_search_term(
                medicine_name
            )
        )

        print(
            f"\nOriginal Search: "
            f"{medicine_name}"
        )

        print(
            f"Search Term Used: "
            f"{search_term}"
        )

        one_mg_result = (
            self.search_1mg_source(
                search_term
            )
        )

        apollo_result = (
            self.search_apollo_source(
                search_term
            )
        )

        all_urls = list(
            dict.fromkeys(
                one_mg_result["urls"]
                +
                apollo_result["urls"]
            )
        )

        result = {

            "medicine_name":
            medicine_name,

            "search_term":
            search_term,

            "one_mg_count":
            one_mg_result["count"],

            "apollo_count":
            apollo_result["count"],

            "total_urls":
            len(all_urls),

            "urls":
            all_urls
        }

        print(
            f"\n1mg URLs: "
            f"{result['one_mg_count']}"
        )

        print(
            f"Apollo URLs: "
            f"{result['apollo_count']}"
        )

        print(
            f"Total URLs: "
            f"{result['total_urls']}"
        )

        return result