# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:26:04 2026

@author: user
"""

from agents.coordinator_agent import (
    CoordinatorAgent
)

from agents.substitute_agent import (
    SubstituteAgent
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
        products[:3]
    )
)

print(
    f"\nSubstitutes Found: "
    f"{len(substitutes)}"
)

print(
    substitutes[:5]
)