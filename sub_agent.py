from google.adk.agents.llm_agent import Agent

planner_agent = Agent(
    name="planner_agent",
    model="gemini-3.5-flash",
    instruction="You are a travel planning assistant."
)

weather_agent = Agent(
    name="weather_agent",
    model="gemini-3.5-flash",
    instruction="You provide weather information."
)

place_agent = Agent(
    name="place_agent",
    model="gemini-3.5-flash",
    instruction="You suggest tourist attractions and places."
)

budget_agent = Agent(
    name="budget_agent",
    model="gemini-3.5-flash",
    instruction="You help users estimate travel costs and budgets."
)