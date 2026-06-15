# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:55:01 2026

@author: user
"""

from agents.coordinator_agent import (
    CoordinatorAgent
)

from agents.manufacturer_agent import (
    ManufacturerAgent
)

coordinator = (
    CoordinatorAgent()
)

products = coordinator.run(
    "Betamethasone Dipropionate"
)

manufacturer_agent = (
    ManufacturerAgent()
)

result = manufacturer_agent.run(
    products
)

print(result)