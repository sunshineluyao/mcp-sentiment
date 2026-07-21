import json

import gradio as gr
from textblob import TextBlob


def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of a piece of text.

    Args:
        text: The text whose sentiment should be analyzed.

    Returns:
        A JSON string containing polarity, subjectivity, and an assessment.
    """
    cleaned_text = text.strip()

    if not cleaned_text:
        return json.dumps(
            {
                "error": "Please provide some text to analyze."
            }
        )

    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2),
        "subjectivity": round(sentiment.subjectivity, 2),
        "assessment": (
            "positive"
            if sentiment.polarity > 0
            else "negative"
            if sentiment.polarity < 0
            else "neutral"
        ),
    }

    return json.dumps(result, indent=2)


demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(
        label="Text",
        placeholder="Enter text to analyze...",
        lines=5,
    ),
    outputs=gr.Textbox(
        label="Sentiment result",
        lines=8,
    ),
    title="MCP Sentiment Analysis",
    description=(
        "Analyze text sentiment with TextBlob. "
        "The same function is also exposed as an MCP Tool."
    ),
)


if __name__ == "__main__":
    demo.launch(
        mcp_server=True,
        server_name="0.0.0.0",
    )