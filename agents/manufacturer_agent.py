# -*- coding: utf-8 -*-
"""
Created on Mon Jun 8 12:54:32 2026

@author: user
"""

class ManufacturerAgent:

    def run(
        self,
        products
    ):

        manufacturer_summary = {}

        for product in products:

            manufacturer = product.get(
                "Manufacturer",
                "Unknown"
            )

            if (
                manufacturer
                not in manufacturer_summary
            ):

                manufacturer_summary[
                    manufacturer
                ] = {
                    "count": 0,
                    "products": []
                }

            manufacturer_summary[
                manufacturer
            ]["count"] += 1

            manufacturer_summary[
                manufacturer
            ]["products"].append(
                product.get(
                    "Brand Name",
                    ""
                )
            )

        return manufacturer_summary