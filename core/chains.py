"""
LangChain LCEL chain for the LinkedIn Post Generator.

Uses the modern LangChain Expression Language (LCEL) pattern:
    prompt | llm | parser

This replaces the deprecated LLMChain / chain.run() approach.
"""

from langchain_core.output_parsers import StrOutputParser

from core.prompts import linkedin_post_prompt
from config import DEFAULT_TEMPERATURE


class LinkedInPostGeneratorError(Exception):
    """Custom exception for post generation failures."""
    pass


def _get_llm(provider: str, model: str, api_key: str, temperature: float):
    """
    Factory function to instantiate the correct LLM based on provider.

    Args:
        provider: Either "groq" or "openai".
        model: The model name string (e.g., "llama-3.3-70b-versatile").
        api_key: The API key for the chosen provider.
        temperature: Sampling temperature (0.0–1.0).

    Returns:
        A LangChain chat model instance.

    Raises:
        LinkedInPostGeneratorError: If the provider is unsupported.
    """
    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(
            model=model,
            api_key=api_key,
            temperature=temperature,
        )
    elif provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=model,
            api_key=api_key,
            temperature=temperature,
        )
    else:
        raise LinkedInPostGeneratorError(f"Unsupported provider: {provider}")


def get_chain(provider: str, model: str, api_key: str, temperature: float = DEFAULT_TEMPERATURE):
    """
    Build and return the LCEL chain: prompt → LLM → string output.

    This is the modern LangChain pattern (LCEL) that replaces the deprecated
    LLMChain class. The chain is composable, streamable, and type-safe.

    Args:
        provider: LLM provider name ("groq" or "openai").
        model: Model identifier string.
        api_key: Provider API key.
        temperature: Sampling temperature.

    Returns:
        A LangChain Runnable chain.
    """
    llm = _get_llm(provider, model, api_key, temperature)
    chain = linkedin_post_prompt | llm | StrOutputParser()
    return chain


def generate_post(
    topic: str,
    language: str,
    tone: str,
    length: str,
    provider: str,
    model: str,
    api_key: str,
    temperature: float = DEFAULT_TEMPERATURE,
) -> str:
    """
    Generate a LinkedIn post using the configured LCEL chain.

    Args:
        topic: The subject of the LinkedIn post.
        language: Target language for the post.
        tone: Desired writing tone description.
        length: Desired post length description.
        provider: LLM provider name.
        model: Model identifier.
        api_key: Provider API key.
        temperature: Sampling temperature.

    Returns:
        The generated LinkedIn post as a string.

    Raises:
        LinkedInPostGeneratorError: If generation fails for any reason.
    """
    try:
        chain = get_chain(provider, model, api_key, temperature)
        result = chain.invoke({
            "topic": topic,
            "language": language,
            "tone": tone,
            "length": length,
        })
        return result
    except Exception as e:
        raise LinkedInPostGeneratorError(f"Post generation failed: {e}") from e
