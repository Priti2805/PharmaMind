# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:13:41 2026

@author: user
"""

import pandas as pd
import os


class StorageAgent:

    def save_products(
        self,
        products,
        filename="data/products.csv"
    ):

        if not products:

            return

        df = pd.DataFrame(
            products
        )

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"Products Saved: {filename}"
        )

    def save_substitutes(
        self,
        substitutes,
        filename="data/substitutes.csv"
    ):

        if not substitutes:

            return

        df = pd.DataFrame(
            substitutes
        )

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"Substitutes Saved: {filename}"
        )