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

        tagged_chunks = chunk_document(document_text)

        # --- Route chunks ---
        action_chunks = []
        risk_chunks = []
        all_chunks = []

        for chunk in tagged_chunks:
            text = chunk["text"]
            tags = chunk["tags"]

            all_chunks.append(text)

            if "action" in tags:
                action_chunks.append(text)

            if "risk" in tags:
                risk_chunks.append(text)

        # fallback if empty
        action_context = "\n\n".join(action_chunks) if action_chunks else ""
        risk_context = "\n\n".join(risk_chunks) if risk_chunks else ""
        summary_context = "\n\n".join(all_chunks)

        # ---- Summary ----
        summary_response = self.user_proxy.initiate_chat(
            self.summary_agent,
            message=summary_context,
            max_turns=1
        )

        # ---- Actions ----
        action_response = self.user_proxy.initiate_chat(
            self.action_agent,
            message=action_context,
            max_turns=1
        )

        # ---- Risks ----
        risk_response = self.user_proxy.initiate_chat(
            self.risk_agent,
            message=risk_context,
            max_turns=1
        )

        return {
            "summary": summary_response.summary,
            "actions": action_response.summary,
            "risks": risk_response.summary
        }
