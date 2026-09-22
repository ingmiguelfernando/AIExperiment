# OpenRouter Colab Experiment

A minimal notebook that asks a question to a free LLM through [OpenRouter](https://openrouter.ai/) using the `openai` Python library.

It is meant to run in **Google Colab** — no local setup required.

## Usage

1. Open [openrouter_colab_example.ipynb](openrouter_colab_example.ipynb) in Google Colab.
2. Create an API key at https://openrouter.ai/keys.
3. In Colab, open the **Secrets** panel (key icon) and add a secret named `OPENROUTER_API_KEY`. Enable *Notebook access*.
4. Run the cells in order.

The notebook covers a basic chat completion, a streaming response, and how to list the currently available `:free` models.

> Never commit your API key. Use Colab Secrets or an environment variable.
