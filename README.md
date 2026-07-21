---
title: MCP Sentiment Analysis
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: gradio
python_version: "3.11"
app_file: app.py
pinned: false
short_description: A Gradio sentiment analysis app exposed as an MCP server.
tags:
  - mcp
  - gradio
  - sentiment-analysis
  - textblob
---

# MCP Sentiment Analysis

A minimal end-to-end Model Context Protocol application based on the
Hugging Face MCP Course.

## Capabilities

- Gradio web interface
- TextBlob sentiment analysis
- Automatically generated MCP Tool
- Deployment to Hugging Face Spaces
- Automatic synchronization from GitHub

## MCP Tool

The application exposes the Python function:

```text
sentiment_analysis