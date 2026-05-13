from crewai import Crew, Task

from app.agents.retriever_agent import retriever_agent
from app.agents.analyzer_agent import analyzer_agent
from app.agents.validator_agent import validator_agent

from app.rag.query_engine import retrieve_documents

def run_crew(query):

    # Retrieve context
    context = retrieve_documents(query)

    # Task 1
    retrieval_task = Task(
        description=f"""
        Retrieve important context
        for the query:

        {query}

        Context:
        {context}
        """,

        expected_output="Relevant retrieved context",

        agent=retriever_agent
    )

    # Task 2
    analysis_task = Task(
        description=f"""
        Analyze the following context
        and answer the user query.

        Query:
        {query}

        Context:
        {context}
        """,

        expected_output="Detailed helpful answer",

        agent=analyzer_agent
    )

    # Task 3
    validation_task = Task(
        description="""
        Validate whether the generated
        answer is correct and useful.
        """,

        expected_output="Validation result",

        agent=validator_agent
    )

    crew = Crew(
        agents=[
            retriever_agent,
            analyzer_agent,
            validator_agent
        ],

        tasks=[
            retrieval_task,
            analysis_task,
            validation_task
        ],

        verbose=True
    )

    result = crew.kickoff()

    return result