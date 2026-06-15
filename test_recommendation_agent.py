# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:41:41 2026

@author: user
"""

from agents.recommendation_agent import (
    RecommendationAgent
)

agent = (
    RecommendationAgent()
)

print(
    "\nTOP MANUFACTURERS\n"
)

print(
    agent.top_manufacturers()
)

print(
    "\nBETNI SUBSTITUTES\n"
)

subs = agent.get_substitutes(
    "Betni Injection"
)

print(subs)

print(
    "\nTotal Substitutes:",
    len(subs)
)
