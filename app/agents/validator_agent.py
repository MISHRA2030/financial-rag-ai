
from crewai import Agent


validator_agent = Agent(
    role="Validator Agent",

    goal="Validate financial responses",

    backstory="""
    Ensures generated financial
    responses are accurate.
    """,

    llm="gemini/gemini-1.5-flash",

    verbose=True
)