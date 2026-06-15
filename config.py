"""
Configuration constants for the LinkedIn Post Generator.

Centralizes all tunable parameters — languages, tones, providers, and model
defaults — so nothing is hardcoded across the codebase.
"""

# ──────────────────────────────────────────────
# Supported Languages
# ──────────────────────────────────────────────
LANGUAGES = [
    "English",
    "Bengali (বাংলা)",
    "Spanish (Español)",
    "French (Français)",
    "German (Deutsch)",
    "Hindi (हिन्दी)",
    "Arabic (العربية)",
    "Chinese (中文)",
    "Japanese (日本語)",
    "Portuguese (Português)",
]

# ──────────────────────────────────────────────
# Tone Presets
# ──────────────────────────────────────────────
TONES = {
    "🎯 Professional": "professional, authoritative, and polished",
    "💡 Inspirational": "uplifting, motivational, and thought-provoking",
    "📖 Storytelling": "narrative-driven, personal, and relatable",
    "😄 Casual": "friendly, conversational, and approachable",
    "🔥 Bold & Provocative": "contrarian, attention-grabbing, and debate-sparking",
}

# ──────────────────────────────────────────────
# Post Length Presets
# ──────────────────────────────────────────────
LENGTH_OPTIONS = {
    "Short (1–2 paragraphs)": "1 to 2 concise paragraphs",
    "Medium (2–3 paragraphs)": "2 to 3 well-developed paragraphs",
    "Long (3–4 paragraphs)": "3 to 4 detailed paragraphs",
}

# ──────────────────────────────────────────────
# LLM Provider Configuration
# ──────────────────────────────────────────────
PROVIDERS = {
    "Groq (Free — Llama 3.3 70B)": {
        "provider": "groq",
        "model": "llama-3.3-70b-versatile",
        "env_key": "GROQ_API_KEY",
    },
    "OpenAI (GPT-4o Mini)": {
        "provider": "openai",
        "model": "gpt-4o-mini",
        "env_key": "OPENAI_API_KEY",
    },
    "OpenAI (GPT-4o)": {
        "provider": "openai",
        "model": "gpt-4o",
        "env_key": "OPENAI_API_KEY",
    },
}

DEFAULT_TEMPERATURE = 0.7
