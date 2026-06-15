# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:43:23 2026

@author: user
"""

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)
from agents.scraping_agent import ScrapingAgent

agent = ScrapingAgent()

urls = [
    "https://www.1mg.com/drugs/betnesol-tablet-70138"
]

results = agent.run(
    urls,
    limit=1
)

print(results)