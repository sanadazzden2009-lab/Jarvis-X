from providers import generate_reply


def process_message(text: str) -> str:
    """
    Brain layer entry point.

    Currently forwards straight to the Groq provider placeholder. Once more
    than one provider exists, routing logic (retries, provider switching,
    model choice) will live here instead.
    """
    return generate_reply(text)
