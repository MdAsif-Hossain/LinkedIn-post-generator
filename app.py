"""
LinkedIn Post Generator — Streamlit Application

A professional AI-powered LinkedIn post generator built with LangChain (LCEL)
and Streamlit. Supports multiple LLM providers, tones, languages, and
maintains a session-based post history.

Run with:
    streamlit run app.py
"""

import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os

from config import LANGUAGES, TONES, LENGTH_OPTIONS, PROVIDERS
from core.chains import generate_post, LinkedInPostGeneratorError

# Load .env file if it exists
load_dotenv()

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="LinkedIn Post Generator — AI Agent",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# Custom CSS for Premium Look
# ──────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Import Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* ── Global Font ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero Header ── */
    .hero-header {
        background: linear-gradient(135deg, #0077B5 0%, #00A0DC 50%, #667eea 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 119, 181, 0.25);
    }
    .hero-header h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    .hero-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.05rem;
        margin: 0;
        font-weight: 400;
    }

    /* ── Output Card ── */
    .post-card {
        background: linear-gradient(145deg, #f8f9ff 0%, #f0f4ff 100%);
        border: 1px solid #e0e7ff;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        line-height: 1.75;
        font-size: 1.02rem;
        color: #1a1a2e;
        white-space: pre-wrap;
    }

    /* ── Sidebar Styling ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
    }
    [data-testid="stSidebar"] h1 {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0077B5;
    }

    /* ── History Items ── */
    .history-item {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        font-size: 0.85rem;
        color: #334155;
        transition: all 0.2s ease;
        cursor: default;
    }
    .history-item:hover {
        border-color: #0077B5;
        box-shadow: 0 2px 8px rgba(0, 119, 181, 0.1);
    }
    .history-topic {
        font-weight: 600;
        color: #0077B5;
        display: block;
        margin-bottom: 2px;
    }
    .history-meta {
        font-size: 0.75rem;
        color: #94a3b8;
    }

    /* ── Stats Badge ── */
    .stats-badge {
        background: linear-gradient(135deg, #0077B5, #00A0DC);
        color: white;
        padding: 0.6rem 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    /* ── Button Styling ── */
    .stButton > button {
        background: linear-gradient(135deg, #0077B5 0%, #00A0DC 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(0, 119, 181, 0.35);
        transform: translateY(-1px);
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #94a3b8;
        font-size: 0.8rem;
    }
    .footer a {
        color: #0077B5;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Session State Initialization
# ──────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "current_post" not in st.session_state:
    st.session_state.current_post = None


# ──────────────────────────────────────────────
# Sidebar — Configuration & History
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("# ⚙️ Configuration")
    st.markdown("---")

    # Provider selection
    provider_label = st.selectbox(
        "🤖 LLM Provider",
        options=list(PROVIDERS.keys()),
        index=0,
        help="Groq is free and fast. OpenAI requires a paid API key.",
    )
    provider_config = PROVIDERS[provider_label]

    # API Key input
    env_key_value = os.getenv(provider_config["env_key"], "")
    api_key = st.text_input(
        f"🔑 {provider_config['env_key']}",
        value=env_key_value,
        type="password",
        help="Your API key is never stored — it lives only in this session.",
    )

    # Temperature slider
    temperature = st.slider(
        "🌡️ Creativity (Temperature)",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher = more creative & varied. Lower = more focused & consistent.",
    )

    st.markdown("---")

    # ── Post History ──
    st.markdown("# 📜 Post History")

    if st.session_state.history:
        st.markdown(
            f'<div class="stats-badge">📝 {len(st.session_state.history)} post{"s" if len(st.session_state.history) != 1 else ""} generated</div>',
            unsafe_allow_html=True,
        )
        for i, entry in enumerate(reversed(st.session_state.history)):
            st.markdown(
                f"""<div class="history-item">
                    <span class="history-topic">{entry['topic']}</span>
                    <span class="history-meta">{entry['language']} · {entry['tone']} · {entry['time']}</span>
                </div>""",
                unsafe_allow_html=True,
            )
    else:
        st.caption("Your generated posts will appear here.")


# ──────────────────────────────────────────────
# Main Content Area
# ──────────────────────────────────────────────

# Hero Header
st.markdown("""
<div class="hero-header">
    <h1>🚀 LinkedIn Post Generator</h1>
    <p>AI-powered content creation with LangChain &nbsp;·&nbsp; Craft viral posts in seconds</p>
</div>
""", unsafe_allow_html=True)

# Input Form
col1, col2 = st.columns(2)
with col1:
    language = st.selectbox("🌐 Language", LANGUAGES, index=0)
    tone_label = st.selectbox("🎨 Tone", list(TONES.keys()), index=0)
with col2:
    length_label = st.selectbox("📏 Post Length", list(LENGTH_OPTIONS.keys()), index=1)
    st.markdown("<div style='height: 1.7rem'></div>", unsafe_allow_html=True)

topic = st.text_area(
    "📌 What should the post be about?",
    placeholder="e.g., How AI is transforming healthcare diagnostics in 2026...",
    height=100,
    help="Be specific for better results. Include context, angles, or key points you want covered.",
)

# Generate Button
generate_clicked = st.button("✨ Generate LinkedIn Post", use_container_width=True)

st.markdown("---")

# ──────────────────────────────────────────────
# Generation Logic
# ──────────────────────────────────────────────
if generate_clicked:
    # Validation
    if not api_key:
        st.error("🔑 Please enter your API key in the sidebar to continue.")
    elif not topic.strip():
        st.warning("📌 Please enter a topic for your post.")
    else:
        with st.spinner("🧠 Crafting your LinkedIn post..."):
            try:
                post = generate_post(
                    topic=topic.strip(),
                    language=language,
                    tone=TONES[tone_label],
                    length=LENGTH_OPTIONS[length_label],
                    provider=provider_config["provider"],
                    model=provider_config["model"],
                    api_key=api_key,
                    temperature=temperature,
                )
                st.session_state.current_post = post

                # Add to history
                st.session_state.history.append({
                    "topic": topic.strip()[:60] + ("..." if len(topic.strip()) > 60 else ""),
                    "language": language.split(" ")[0],
                    "tone": tone_label.split(" ", 1)[1] if " " in tone_label else tone_label,
                    "time": datetime.now().strftime("%I:%M %p"),
                    "full_post": post,
                })

                st.rerun()

            except LinkedInPostGeneratorError as e:
                st.error(f"❌ Generation failed: {e}")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")

# ──────────────────────────────────────────────
# Display Generated Post
# ──────────────────────────────────────────────
if st.session_state.current_post:
    st.subheader("📄 Your Generated Post")
    st.markdown(
        f'<div class="post-card">{st.session_state.current_post}</div>',
        unsafe_allow_html=True,
    )

    # Action Buttons
    col_copy, col_clear = st.columns([3, 1])
    with col_copy:
        st.code(st.session_state.current_post, language=None)
        st.caption("👆 Click the copy icon (top-right of the code block) to copy your post")
    with col_clear:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.current_post = None
            st.rerun()

# ── Load Previous from History ──
if st.session_state.history and not st.session_state.current_post:
    st.info("👈 Select a previous post from the sidebar history, or generate a new one above!")

# ──────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built with ❤️ using <a href="https://python.langchain.com/" target="_blank">LangChain</a> &
    <a href="https://streamlit.io/" target="_blank">Streamlit</a>
    &nbsp;·&nbsp; Powered by LCEL (LangChain Expression Language)
</div>
""", unsafe_allow_html=True)
