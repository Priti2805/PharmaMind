# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:25:32 2026

@author: user
"""

from scrapers.one_mg import (
    get_1mg_substitutes
)


class SubstituteAgent:

    def run(
        self,
        products
    ):

        all_substitutes = []

        for product in products:

            url = product.get(
                "URL",
                ""
            )

            try:

                substitutes = (
                    get_1mg_substitutes(
                        url
                    )
                )

                all_substitutes.extend(
                    substitutes
                )

            except Exception as e:

                print(
                    f"Substitute Error: {e}"
                )

        return all_substitutes