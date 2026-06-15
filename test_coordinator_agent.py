# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:50:55 2026

@author: user
"""

from agents.coordinator_agent import (
    CoordinatorAgent
)

agent = CoordinatorAgent()

results = agent.run(
    "Betamethasone Dipropionate"
)

print(
    f"\nProducts Found: {len(results)}"
)

for product in results:

    print(
        product.get(
            "Brand Name",
            ""
        )
    )