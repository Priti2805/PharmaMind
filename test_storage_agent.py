# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:14:18 2026

@author: user
"""

from agents.coordinator_agent import (
    CoordinatorAgent
)

from agents.substitute_agent import (
    SubstituteAgent
)

from agents.storage_agent import (
    StorageAgent
)

coordinator = (
    CoordinatorAgent()
)

products = coordinator.run(
    "Betamethasone Dipropionate"
)

substitute_agent = (
    SubstituteAgent()
)

substitutes = (
    substitute_agent.run(
        products[:20]
    )
)

storage = (
    StorageAgent()
)

storage.save_products(
    products
)

storage.save_substitutes(
    substitutes
)

print(
    f"\nProducts: {len(products)}"
)

print(
    f"Substitutes: {len(substitutes)}"
)