import autogen
from agents.llm_config import llm_config

def create_risk_agent():

    system_prompt = """
    You are a Risk & Open Issues Agent.

    Identify:
    - unresolved questions
    - missing data
    - assumptions
    - potential risks

    Return STRICT JSON format:

    {
        "risks":[
            {
                "issue": "",
                "type": "risk/question/assumption",
                "impact": ""
            }
        ]
    }
    """

    return autogen.AssistantAgent(
        name="risk_agent",
        system_message=system_prompt,
        llm_config=llm_config
    )
