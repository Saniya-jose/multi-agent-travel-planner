from google.adk.agents.llm_agent import Agent
from .sub_agent import (
    planner_agent,
    weather_agent,
    place_agent,
    budget_agent
)

root_agent = Agent(
    name="root_agent",
    model="gemini-3.5-flash",
    instruction="You are a travel coordinator.",
    sub_agents=[
        planner_agent,
        weather_agent,
        place_agent,
        budget_agent
    ]
)