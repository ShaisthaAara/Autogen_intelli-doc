from langchain_text_splitters import RecursiveCharacterTextSplitter

# --- Heuristic Keyword Dictionaries ---
ACTION_KEYWORDS = [
    "must", "should", "required", "deadline", "submit",
    "will", "responsible", "assigned", "complete"
]

RISK_KEYWORDS = [
    "risk", "delay", "failure", "issue", "concern",
    "pending", "blocked", "violation", "dependency"
]


def detect_tags(chunk):
    tags = []
    text = chunk.lower()

    if any(word in text for word in ACTION_KEYWORDS):
        tags.append("action")

    if any(word in text for word in RISK_KEYWORDS):
        tags.append("risk")

    # default fallback (helps summary)
    if not tags:
        tags.append("general")

    return tags


def chunk_document(text, chunk_size=300, chunk_overlap=100):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    raw_chunks = splitter.split_text(text)

    tagged_chunks = []

    for chunk in raw_chunks:
        tagged_chunks.append({
            "text": chunk,
            "tags": detect_tags(chunk)
        })

    return tagged_chunks
