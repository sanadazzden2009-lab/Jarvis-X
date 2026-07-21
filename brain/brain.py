from providers import route


def decide(text: str) -> dict:
    """
    Decision layer.

    Looks at the incoming request and decides how it should be handled.
    Right now there is only one possible outcome (respond via the provider
    router), but this is the seam where future logic - tool use, search,
    other action types - plugs in later without changing process_message's
    shape. Brain no longer needs to know which provider answers it; that
    choice now belongs entirely to providers/router.py.
    """
    return {"action": "respond", "text": text}


def process_message(text: str) -> str:
    """
    Brain layer entry point: get a decision, then act on it.
    """
    decision = decide(text)

    if decision["action"] == "respond":
        return route(decision["text"])

    return "Unhandled decision."
