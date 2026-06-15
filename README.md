# 🚀 LinkedIn Post Generator — AI Agent

> An AI-powered LinkedIn post generator built with **LangChain (LCEL)** and **Streamlit**. Generate professional, engaging, and multilingual LinkedIn posts in seconds.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **Multi-Provider LLM** | Supports **Groq (free)** and **OpenAI** — switch providers from the sidebar |
| 🌐 **10+ Languages** | English, Bengali, Spanish, French, German, Hindi, Arabic, Chinese, Japanese, Portuguese |
| 🎨 **5 Tone Presets** | Professional, Inspirational, Storytelling, Casual, Bold & Provocative |
| 📏 **Length Control** | Short, Medium, or Long post output |
| 📜 **Post History** | Session-based history of all generated posts in the sidebar |
| 🌡️ **Temperature Slider** | Fine-tune the creativity of the output |
| ⚡ **Modern LCEL** | Uses LangChain Expression Language — no deprecated `LLMChain` |

---

## 🏗️ Architecture

```
linkedin-post-generator/
├── app.py               # Streamlit UI — entry point
├── config.py            # Constants: languages, tones, providers
├── core/
│   ├── __init__.py
│   ├── chains.py        # LCEL chain: prompt | llm | parser
│   └── prompts.py       # ChatPromptTemplate (System + Human)
├── .env.example         # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

### How It Works

```
User Input (topic, language, tone, length)
        │
        ▼
  ┌─────────────┐
  │  prompts.py  │  ChatPromptTemplate with SystemMessage + HumanMessage
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  chains.py   │  LCEL: prompt | llm | StrOutputParser()
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  LLM API    │  Groq (Llama 3.3 70B) or OpenAI (GPT-4o)
  └──────┬──────┘
         │
         ▼
  Generated LinkedIn Post
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

### 3. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
# Get your free Groq API key at: https://console.groq.com/keys
GROQ_API_KEY=your_groq_api_key_here

# (Optional) OpenAI key: https://platform.openai.com/api-keys
OPENAI_API_KEY=your_openai_api_key_here
```

> **💡 Tip:** Groq offers a **free tier** — no credit card required!

### 4. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 🧪 Test Cases

| # | Topic | Language | Tone | Expected |
|---|---|---|---|---|
| 1 | AI in Healthcare | English | Professional | 2–4 para, formal, hashtags |
| 2 | Remote Work Productivity | Bengali | Inspirational | Bengali text, motivational |
| 3 | Climate Tech | Spanish | Storytelling | Spanish, narrative style |

---

## 🛠️ Tech Stack

- **[LangChain](https://python.langchain.com/)** — LLM orchestration framework (LCEL pattern)
- **[Streamlit](https://streamlit.io/)** — Interactive web UI
- **[Groq](https://groq.com/)** — Ultra-fast LLM inference (Llama 3.3 70B)
- **[OpenAI](https://openai.com/)** — GPT-4o / GPT-4o Mini

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ using LangChain & Streamlit
</p>
