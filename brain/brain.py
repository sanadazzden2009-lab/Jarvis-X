from providers import generate_reply


def decide(text: str) -> dict:
    """
    Decision layer.

    Looks at the incoming request and decides how it should be handled.
    Right now there is only one possible outcome (route straight to Groq),
    but this is the seam where future logic - provider selection, tool
    use, retries - plugs in later without changing process_message's shape.
    """
    return {"action": "groq", "text": text}


def process_message(text: str) -> str:
    """
    Brain layer entry point: get a decision, then act on it.
    """
    decision = decide(text)

    if decision["action"] == "groq":
        return generate_reply(decision["text"])

    return "Unhandled decision."
