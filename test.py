from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# print(tavily_search("best hotels in india?"))

# print(run_travel_agent("Plan a 7 days Japan trip from Bangladesh"))
# print("\n" + "=" * 80 + "\n")
# print(search_flights("all country flight info"))

user_input = input("Enter your travel query: ")
resp =run_travel_agent(user_input=user_input, thread_id='test_user')
print("final response:")
print(resp["answer"])
