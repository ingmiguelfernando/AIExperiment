# AI Engineer — hands-on session

Supporting notebooks for an introductory talk on LLMs. Everything runs in **Google Colab** against free [OpenRouter](https://openrouter.ai/) models, using the `openai` library.

The idea that runs through the whole session:

> **An LLM is a stateless function: text in, text out.**
> Everything else — memory, tools, RAG — is scaffolding we build around it.

## Notebooks

| | Contents | Colab |
|---|---|---|
| [01_llm_fundamentals.ipynb](01_llm_fundamentals.ipynb) | Basic call, streaming, temperature, the model has no memory, the cost of context, Gradio, tools | [Open](https://colab.research.google.com/github/ingmiguelfernando/AIExperiment/blob/main/01_llm_fundamentals.ipynb) |
| `02_rag.ipynb` | *(pending)* Embeddings, Chroma, 2D/3D visualisation, with and without RAG | |

## Setup

1. Create an API key at https://openrouter.ai/keys
2. In Colab: **Secrets** panel (key icon) → secret named `OPENROUTER_API_KEY` → enable *Notebook access*
3. Run the cells in order

> Never commit your API key. Use Colab Secrets or an environment variable.
