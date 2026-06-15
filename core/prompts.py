"""
Prompt templates for the LinkedIn Post Generator.

Uses ChatPromptTemplate with SystemMessage + HumanMessage — the correct
pattern for chat-based LLMs (not the deprecated PromptTemplate approach).
"""

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


# ──────────────────────────────────────────────
# System Prompt — defines the AI's persona
# ──────────────────────────────────────────────
SYSTEM_TEMPLATE = """You are a world-class LinkedIn content strategist and copywriter.
You craft posts that drive engagement, spark conversations, and build personal brands.

Your writing style principles:
- Open with a powerful hook that stops the scroll
- Use short paragraphs and line breaks for readability
- Include data points or specific examples when relevant
- End with a clear call-to-action or thought-provoking question
- Add 3–5 relevant hashtags at the very end
- Use appropriate emojis sparingly to enhance readability (not overuse)

You MUST write the entire post in the specified language.
You MUST match the specified tone exactly.
You MUST follow the specified length requirement."""

# ──────────────────────────────────────────────
# Human Prompt — carries the user's inputs
# ──────────────────────────────────────────────
HUMAN_TEMPLATE = """Generate a LinkedIn post with the following specifications:

📌 Topic: {topic}
🌐 Language: {language}
🎨 Tone: {tone}
📏 Length: {length}

Write the post now:"""

# ──────────────────────────────────────────────
# Assembled ChatPromptTemplate
# ──────────────────────────────────────────────
linkedin_post_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE),
    HumanMessagePromptTemplate.from_template(HUMAN_TEMPLATE),
])
