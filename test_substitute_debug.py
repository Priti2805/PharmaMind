# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:38:25 2026

@author: user
"""

from scrapers.one_mg import (
    get_1mg_substitutes
)

url = (
    "https://www.1mg.com/drugs/betnesol-tablet-70138"
)

result = get_1mg_substitutes(
    url
)

print(result)
print(
    f"\nCount: {len(result)}"
)