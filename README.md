# AI Engineer — hands-on session

Supporting notebooks for an introductory talk on LLMs. Everything runs in **Google Colab** against free models on [Groq](https://groq.com/), using the `openai` library.

The idea that runs through the whole session:

> **An LLM is a stateless function: text in, text out.**
> Everything else — memory, tools, RAG — is scaffolding we build around it.

## Notebooks

| | Contents | Colab |
|---|---|---|
| [01_llm_fundamentals.ipynb](01_llm_fundamentals.ipynb) | Basic call, tokens, streaming, temperature, the memory experiment, the cost of context, Gradio, tools | [Open](https://colab.research.google.com/github/ingmiguelfernando/AIExperiment/blob/main/01_llm_fundamentals.ipynb) |
| [02_rag.ipynb](02_rag.ipynb) | Chunking, embeddings, Chroma, 2D/3D vector visualisation, with and without RAG | [Open](https://colab.research.google.com/github/ingmiguelfernando/AIExperiment/blob/main/02_rag.ipynb) |

[helpers.py](helpers.py) holds the plotting and display code, so the notebooks stay readable on a shared screen. The notebooks download it automatically when they run in Colab.

[knowledge-base/](knowledge-base) holds the documents used by the RAG notebook: sixteen Markdown files describing **KiwiAir**, a fictional New Zealand regional airline. Every name, figure and contract in there is invented.

## Setup

Create a free API key at https://console.groq.com/keys

In Colab, open the **Secrets** panel (key icon), add it as `GROQ_API_KEY` and enable *Notebook access*. Outside Colab, set it as an environment variable or let the notebook prompt you.

Then run the cells in order.

> Never commit your API key. Use Colab Secrets or an environment variable.
