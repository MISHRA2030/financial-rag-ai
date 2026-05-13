from crewai import Agent


analyzer_agent = Agent(
    role="Financial Analyzer",

    goal="Analyze financial information",

    backstory="""
    Expert financial analyst that explains
    financial data clearly.
    """,

    llm="gemini/gemini-1.5-flash",

    verbose=True
)