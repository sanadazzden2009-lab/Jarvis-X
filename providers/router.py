from . import groq_provider


def route(text: str) -> str:
    """
    Provider router.

    Currently always uses Groq, so behavior is unchanged. This is the seam
    where provider selection and failover (try Groq, fall back to Gemini,
    etc.) will be added once more than one provider is actually connected.
    """
    return groq_provider.generate_reply(text)
