"""Display helpers for the AI Engineer session notebooks.

Kept out of the notebooks so the slides stay focused on the LLM concepts
rather than on plotting code.
"""

from __future__ import annotations

import html

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display

_PALETTE = ["#ffd6a5", "#caffbf", "#9bf6ff", "#bdb2ff", "#ffc6ff", "#fdffb6"]
_PLOT_COLOURS = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#b279a2"]


def show_tokens(text: str, encoder) -> None:
    """Render each token as a coloured chip, like the OpenAI tokenizer page."""
    ids = encoder.encode(text)

    chips = []
    for position, token_id in enumerate(ids):
        piece = encoder.decode([token_id]).replace(" ", "\u00b7").replace("\n", "\\n")
        chips.append(
            f'<span style="background:{_PALETTE[position % len(_PALETTE)]};'
            "padding:3px 5px;margin:2px;border-radius:4px;color:#111;"
            'font-family:monospace;font-size:15px;display:inline-block">'
            f"{html.escape(piece)}</span>"
        )

    display(
        HTML(
            f'<div style="line-height:2.2">{"".join(chips)}</div>'
            f'<p style="font-family:sans-serif;color:#555">'
            f"<b>{len(ids)}</b> tokens &middot; {len(text)} characters "
            f"&middot; <code>&middot;</code> marks a leading space</p>"
        )
    )


def plot_temperature(labels, scores, temperatures=(0.2, 1.0, 2.0)) -> None:
    """Show how temperature reshapes the same set of next-token scores."""
    scores = np.asarray(scores, dtype=float)

    fig, axes = plt.subplots(
        1, len(temperatures), figsize=(4.2 * len(temperatures), 3.4), sharey=True
    )

    for axis, temperature in zip(np.atleast_1d(axes), temperatures):
        if temperature == 0:
            # No dice roll at all: the highest score wins every time.
            probabilities = np.zeros_like(scores)
            probabilities[scores.argmax()] = 1.0
        else:
            shifted = scores / temperature
            weights = np.exp(shifted - shifted.max())
            probabilities = weights / weights.sum()

        axis.bar(labels, probabilities, color="#4c78a8")
        axis.set_title(f"temperature = {temperature}")
        axis.set_ylim(0, 1)
        axis.tick_params(axis="x", rotation=45)
        axis.grid(axis="y", alpha=0.3)

    np.atleast_1d(axes)[0].set_ylabel("Probability of being picked")
    fig.suptitle("Same scores from the model — only the sampling changes")
    fig.tight_layout()
    plt.show()


def plot_token_growth(sent_per_turn, cumulative) -> None:
    """Bars for what each turn sends, line for the running total."""
    turns = range(1, len(cumulative) + 1)

    fig, axis = plt.subplots(figsize=(7, 4))
    axis.bar(turns, sent_per_turn, alpha=0.4, label="Tokens sent this turn")
    axis.plot(turns, cumulative, marker="o", color="crimson", label="Cumulative tokens")
    axis.set_xlabel("Conversation turn")
    axis.set_ylabel("Tokens")
    axis.set_title("What it costs to 'remember'")
    axis.set_xticks(list(turns))
    axis.legend()
    axis.grid(alpha=0.3)
    plt.show()


def launch_chat(respond, title=""):
    """Launch a Gradio chat window, smoothing over differences between Gradio versions.

    `respond` always receives history as OpenAI-style message dicts.
    """
    import inspect

    import gradio as gr

    def adapted(message, history):
        if all(isinstance(item, dict) for item in history):
            history = [{"role": item["role"], "content": item["content"]} for item in history]
        else:
            history = [
                {"role": role, "content": text}
                for user_text, assistant_text in history
                for role, text in (("user", user_text), ("assistant", assistant_text))
                if text
            ]

        yield from respond(message, history)

    supports_type = "type" in inspect.signature(gr.ChatInterface.__init__).parameters
    options = {"type": "messages"} if supports_type else {}

    return gr.ChatInterface(adapted, title=title, **options).launch()


def plot_vectors(vectors, labels, hover_texts, dimensions=2, title="The knowledge base as geometry"):
    """Squash embeddings down to 2D or 3D with t-SNE and plot them coloured by label."""
    import plotly.graph_objects as go
    from sklearn.manifold import TSNE

    vectors = np.asarray(vectors)
    perplexity = min(30, max(5, len(vectors) - 1))

    reduced = TSNE(
        n_components=dimensions,
        random_state=42,
        perplexity=perplexity,
        init="pca",
    ).fit_transform(vectors)

    groups = sorted(set(labels))
    colours = {name: _PLOT_COLOURS[i % len(_PLOT_COLOURS)] for i, name in enumerate(groups)}

    traces = []
    for name in groups:
        picked = [i for i, label in enumerate(labels) if label == name]
        coords = reduced[picked]
        marker = {"size": 5, "color": colours[name], "opacity": 0.85}
        shared = {
            "mode": "markers",
            "name": name,
            "marker": marker,
            "hovertext": [hover_texts[i] for i in picked],
            "hoverinfo": "text",
        }

        if dimensions == 3:
            traces.append(go.Scatter3d(x=coords[:, 0], y=coords[:, 1], z=coords[:, 2], **shared))
        else:
            traces.append(go.Scatter(x=coords[:, 0], y=coords[:, 1], **shared))

    figure = go.Figure(data=traces)
    figure.update_layout(
        title=title,
        width=880,
        height=620,
        margin={"l": 10, "r": 10, "t": 50, "b": 10},
    )
    figure.show()
