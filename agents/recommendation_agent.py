# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:40:25 2026

@author: user
"""

import pandas as pd


class RecommendationAgent:

    def __init__(self):

        self.products_file = (
            "data/products.csv"
        )

        self.substitutes_file = (
            "data/substitutes.csv"
        )

    def load_products(self):

        return pd.read_csv(
            self.products_file
        )

    def load_substitutes(self):

        return pd.read_csv(
            self.substitutes_file
        )

    def get_substitutes(
        self,
        brand_name
    ):

        df = self.load_substitutes()

        result = df[

            df[
                "Parent Brand"
            ]
            .str.lower()
            ==
            brand_name.lower()

        ]

        return result

    def manufacturer_summary(self):

        df = self.load_products()

        return (
            df[
                "Manufacturer"
            ]
            .value_counts()
        )

    def top_manufacturers(
        self,
        top_n=10
    ):

        return (
            self
            .manufacturer_summary()
            .head(top_n)
        )