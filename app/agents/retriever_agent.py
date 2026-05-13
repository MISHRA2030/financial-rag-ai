from crewai import Agent


retriever_agent = Agent(
    role="Retriever Agent",

    goal="Retrieve relevant financial information",

    backstory="""
    Expert at retrieving relevant
    financial information from documents.
    """,

    llm="gemini/gemini-1.5-flash",

    verbose=True
)