import autogen
from agents.llm_config import llm_config

def create_action_agent():

    system_prompt = """
    You are an Action & Dependency Extraction Agent.

    Extract actionable tasks from document.

    For each task extract:
    - task
    - owner (if mentioned)
    - deadline (if mentioned)
    - dependencies (if mentioned)

    Return STRICT JSON format:

    {
        "actions":[
            {
                "task": "",
                "owner": "",
                "deadline": "",
                "dependencies": []
            }
        ]
    }
    """

    return autogen.AssistantAgent(
        name="action_agent",
        system_message=system_prompt,
        llm_config=llm_config
    )
