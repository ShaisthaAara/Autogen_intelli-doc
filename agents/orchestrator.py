import json
import autogen

from agents.summary_agent import create_summary_agent
from agents.action_agent import create_action_agent
from agents.risk_agent import create_risk_agent
from utils.chunking import chunk_document


class MultiAgentOrchestrator:

    def __init__(self):

        self.summary_agent = create_summary_agent()
        self.action_agent = create_action_agent()
        self.risk_agent = create_risk_agent()

        self.user_proxy = autogen.UserProxyAgent(
            name="orchestrator_proxy",
            human_input_mode="NEVER",
            code_execution_config=False
        )

    def process_document(self, document_text):

        chunks = chunk_document(document_text)

        combined_context = "\n\n".join(chunks)

        # ---- Summary ----
        summary_response = self.user_proxy.initiate_chat(
            self.summary_agent,
            message=combined_context,
            max_turns=1

        )

        summary_text = summary_response.summary

        # ---- Actions ----
        action_response = self.user_proxy.initiate_chat(
            self.action_agent,
            message=combined_context,
            max_turns=1

        )

        # ---- Risks ----
        risk_response = self.user_proxy.initiate_chat(
            self.risk_agent,
            message=combined_context,
            max_turns=1

        )

        return {
            "summary": summary_text,
            "actions": action_response.summary,
            "risks": risk_response.summary, 
            # "riskser": risk_response.cost
        }
