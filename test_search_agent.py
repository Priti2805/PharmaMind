from agents.search_agent import SearchAgent

agent = SearchAgent()

result = agent.run(
    "Betamethasone Dipropionate"
)

print("\n========== RESULT ==========")

print(
    f"Medicine: {result['medicine_name']}"
)

print(
    f"Search Term: {result['search_term']}"
)

print(
    f"1mg URLs: {result['one_mg_count']}"
)

print(
    f"Apollo URLs: {result['apollo_count']}"
)

print(
    f"Total URLs: {result['total_urls']}"
)