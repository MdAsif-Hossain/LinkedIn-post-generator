# 🚀 LinkedIn Post Generator — AI Agent with LangChain

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-F55036?style=for-the-badge&logo=groq&logoColor=white)

**An AI-powered agent that generates professional, multilingual LinkedIn posts in seconds.**
Built with modern LangChain Expression Language (LCEL) — no deprecated APIs.

</div>

---

## 📽️ Demo

<div align="center">

https://github.com/user-attachments/assets/REPLACE_WITH_YOUR_VIDEO_ID

</div>

> **How to add your video to GitHub:**
> 1. Go to your repo → open a new Issue
> 2. Drag & drop `demo.mp4` into the comment box
> 3. GitHub generates a URL like `https://github.com/user-attachments/assets/abc123...`
> 4. Copy that URL and replace the placeholder above
> 5. Close the issue — the video link stays permanent
>
> The video will render in a **player frame** with autoplay directly in your README.

---

## ✨ Features

- 🤖 **Multi-Provider LLM Support** — Switch between **Groq (free)** and **OpenAI** from the sidebar
- 🌐 **10+ Languages** — English, Bengali, Spanish, French, German, Hindi, Arabic, Chinese, Japanese, Portuguese
- 🎨 **5 Tone Presets** — Professional, Inspirational, Storytelling, Casual, Bold & Provocative
- 📏 **Adjustable Post Length** — Short, Medium, or Long output
- 📜 **Session-Based Post History** — Track and revisit all generated posts
- 🌡️ **Temperature Control** — Fine-tune creativity from focused (0.0) to creative (1.0)
- ⚡ **Modern LCEL Architecture** — Uses `prompt | llm | StrOutputParser()`, not deprecated `LLMChain`

---

## 🏗️ Project Architecture

```
linkedin-post-generator/
│
├── app.py                  # Streamlit UI — entry point
├── config.py               # Constants: languages, tones, providers, models
│
├── core/
│   ├── __init__.py
│   ├── prompts.py          # ChatPromptTemplate (SystemMessage + HumanMessage)
│   └── chains.py           # LCEL chain: prompt | llm | StrOutputParser()
│
├── .env                    # API keys (git-ignored)
├── .env.example            # Template for environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```
┌──────────────────────────────────────────────────────────────┐
│                        User Input                            │
│   Topic · Language · Tone · Post Length                       │
└──────────────────┬───────────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  prompts.py — ChatPromptTemplate                             │
│  SystemMessage (persona + rules) + HumanMessage (user input) │
└──────────────────┬───────────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  chains.py — LCEL Chain                                      │
│  prompt | ChatGroq/ChatOpenAI | StrOutputParser()            │
└──────────────────┬───────────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────────┐
│  Generated LinkedIn Post (2–4 paragraphs + hashtags)         │
└──────────────────────────────────────────────────────────────┘
```

The chain uses **LangChain Expression Language (LCEL)** — the modern, composable pattern that replaces the deprecated `LLMChain` class:

```python
# core/chains.py
chain = linkedin_post_prompt | llm | StrOutputParser()
result = chain.invoke({"topic": ..., "language": ..., "tone": ..., "length": ...})
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key

```bash
cp .env.example .env
```

Edit the `.env` file and add your Groq API key:

```env
GROQ_API_KEY=gsk_your_actual_key_here
```

> 💡 **Get a free Groq API key** at [console.groq.com/keys](https://console.groq.com/keys) — no credit card required.

### 4. Run the App

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` 🎉

---

## 🧪 Test Cases

| # | Topic | Language | Tone | Expected Output |
|---|---|---|---|---|
| 1 | AI in Healthcare | English | 🎯 Professional | Formal, structured, with relevant hashtags |
| 2 | Remote Work Productivity | Bengali (বাংলা) | 💡 Inspirational | Full Bengali text, motivational tone |
| 3 | Climate Tech Startups | Spanish (Español) | 📖 Storytelling | Spanish narrative with personal angle |

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| [LangChain](https://python.langchain.com/) | LLM orchestration (LCEL pattern) |
| [Streamlit](https://streamlit.io/) | Interactive web UI |
| [Groq](https://groq.com/) | Ultra-fast inference — Llama 3.3 70B |
| [OpenAI](https://openai.com/) | GPT-4o / GPT-4o Mini (optional) |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

**Built with ❤️ using LangChain & Streamlit**

</div>
