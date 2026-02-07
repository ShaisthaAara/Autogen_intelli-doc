import sys
import os
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.orchestrator import MultiAgentOrchestrator


def load_document(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():

    document_text = load_document("sample.txt")

    orchestrator = MultiAgentOrchestrator()

    results = orchestrator.process_document(document_text)

    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
