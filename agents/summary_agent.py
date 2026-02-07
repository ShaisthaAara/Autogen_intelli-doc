import autogen
from agents.llm_config import llm_config

def create_summary_agent():

    system_prompt = """
    You are a Context-Aware Summary Agent.

    Responsibilities:
    - Generate concise summary
    - Preserve intent, constraints, and critical decisions
    - Handle multiple document chunks

    Output only summary text.
    """

    return autogen.AssistantAgent(
        name="summary_agent",
        system_message=system_prompt,
        llm_config=llm_config
    )
