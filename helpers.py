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
