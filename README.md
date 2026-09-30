# AI Playground

A personal collection of small, reusable AI code snippets, experiments, and reference scripts.

Instead of searching through old tutorials, bookmarks, or API documentation every time, this repository serves as a tested, self-contained reference library—covering LLM API calls, prompt patterns, structured outputs, and practical integrations ready to be dropped into future projects.

---

## 🎯 Repository Goals & Philosophy

- **Plug & Play:** Each snippet or script is designed to be minimal, self-contained, and easy to lift into other projects.
- **Battle-Tested:** Tested patterns against real API versions with working dependencies.
- **Zero Fluff:** Focused implementations without unnecessary abstraction or heavy framework lock-in unless specifically testing that framework.
- **Copy-Paste Friendly:** Clear inputs, outputs, and environment requirements documented per recipe.

---

## 📁 Repository Structure

```text
ai-playground/
├── llm-apis/            # Raw provider SDKs & unified clients (OpenAI, Anthropic, Gemini, Ollama)
│   ├── basic_completion.py
│   ├── streaming_response.py
│   └── vision_multimodal.py
├── structured-outputs/  # JSON schemas, Pydantic extraction, Instructor, Outlines
│   ├── pydantic_extraction.py
│   └── tool_calling_schema.py
├── prompt-patterns/     # System prompts, few-shot examples, chain-of-thought, persona templates
│   ├── chain_of_thought.py
│   └── dynamic_few_shot.py
├── embeddings-rag/      # Embeddings, vector search, chunking, and lightweight retrieval
│   ├── text_embeddings.py
│   └── simple_rag_pipeline.py
├── integrations/        # Integrations with databases, web search, function calling, agents
│   ├── web_search_tool.py
│   └── sqlite_tool_calling.py
├── experiments/         # Exploratory notebooks, benchmarks, and model evaluations
└── .env.example         # Template for required API keys
```

*(Directories can be expanded as new patterns are added.)*

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10+ (or latest stable)
- Recommended package manager: `uv`, `poetry`, or standard `venv` + `pip`

### 2. Environment Setup

Clone the repository and set up a virtual environment:

```bash
git clone <repo-url> ai-playground
cd ai-playground

# Using standard venv
python3 -m venv .venv
source .venv/bin/activate

# Or using uv
uv venv
source .venv/bin/activate
```

### 3. API Keys Configuration

Copy the sample `.env.example` file and supply the credentials for the providers you plan to test:

```bash
cp .env.example .env
```

Example `.env`:

```ini
# Major LLM Providers
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GEMINI_API_KEY=your_gemini_api_key

# Local / Open-source Models
OLLAMA_BASE_URL=http://localhost:11434

# Optional Tooling & Search
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🛠️ Snippet Conventions

When adding new scripts to this playground, stick to the following conventions:

1. **Self-Contained:** Strive for single-file scripts with minimal outside imports beyond standard provider SDKs.
2. **Type Hints & Docstrings:** Include clear parameter types and a top-level docstring explaining what the snippet demonstrates and its prerequisites.
3. **Environment Safe:** Always load API keys via environment variables (e.g. `python-dotenv`), never hardcode secrets.
4. **Runnable Example:** Provide a runnable `if __name__ == "__main__":` block demonstrating immediate usage with sample input and expected output.

---

## 📝 License

This playground is maintained for personal learning and reference. Code snippets are free to reuse, adapt, and integrate into personal or commercial projects.
