# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:17:45 2026

@author: user
"""

from agents.coordinator_agent import (
    CoordinatorAgent
)

from agents.manufacturer_agent import (
    ManufacturerAgent
)

from agents.manufacturer_normalizer_agent import (
    ManufacturerNormalizerAgent
)

coordinator = CoordinatorAgent()

products = coordinator.run(
    "Betamethasone Dipropionate"
)

manufacturer_agent = (
    ManufacturerAgent()
)

manufacturer_summary = (
    manufacturer_agent.run(
        products
    )
)

normalizer = (
    ManufacturerNormalizerAgent()
)

normalized = (
    normalizer.run(
        manufacturer_summary
    )
)

print(normalized)