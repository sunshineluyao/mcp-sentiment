---
title: MCP Sentiment Analysis
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: gradio
python_version: "3.10"
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

Add this section to README.md:

````md


## Match ZeroGPU Space Settings

This app uses the `spaces` package so it can run correctly on a Hugging Face **ZeroGPU** Space. To match the default ZeroGPU setup:

### 1) Ensure `spaces` is in requirements

Already included in `requirements.txt`:

````text
gradio[mcp]
textblob
spaces
````

### 2) Decorate GPU-bound functions

Any function that needs GPU access must be wrapped with `@spaces.GPU`:

````python
import spaces

@spaces.GPU
def predict(text):
    # ...existing code...
    return result
````

### 3) Set Space hardware to ZeroGPU

In the Space settings (`https://huggingface.co/spaces/zlysunshine/mcp-sentiment/settings`):

1. Go to **Settings** → **Hardware**.
2. Select **ZeroGPU**.
3. Save changes.

### 4) Verify Space metadata

Ensure the YAML frontmatter in this README does **not** conflict with ZeroGPU (no `sdk_version` mismatch, and `sdk: gradio` is set, as shown at the top of this file).

### 5) Redeploy

After hardware changes, redeploy:

````bash
python deploy_to_hf.py
````

### Notes

- ZeroGPU allocates GPU only during the decorated function call; keep GPU-only code inside `@spaces.GPU` functions.
- If GPU access fails, confirm the Space hardware is set to ZeroGPU and the `spaces` package is installed (see requirements.txt).



## Deploy to Hugging Face Space

This repository includes `deploy_to_hf.py` to upload the app to the existing Hugging Face Space:

- **Space repo:** `zlysunshine/mcp-sentiment`
- The script does **not** create the Space. It must already exist.

### 1) Install dependency

````bash
pip install huggingface_hub
`````

Add the missing sections after the current end of the file:


````bash
pip install huggingface_hub
````

### 2) Login to Hugging Face

1. Open the token settings page in your host browser:

````bash
"$BROWSER" https://huggingface.co/settings/tokens
````

2. Create a new token with **write** access to Spaces.
3. Login from the terminal:

````bash
huggingface-cli login
````

4. Paste the token when prompted.

### 3) Deploy

Run from the repository root:

````bash
python deploy_to_hf.py
````

### 4) Verify deployment

On success, the script prints:

- authenticated username
- commit URL
- Space URL: `https://huggingface.co/spaces/zlysunshine/mcp-sentiment`

### Troubleshooting

- `Space ... does not exist`: create the Space first, then rerun.
- `Deployment rejected` / HTTP error: check token permissions and Space access.
````

Then commit and push:

````bash
git add README.md
git commit -m "Add Hugging Face login and deployment steps to README"
git push origin main
````