# Website Summarizer with Ollama

A Python application that extracts website content and generates concise Persian summaries using a local LLM powered by Ollama.

## Features

* Extract website title and content
* Remove irrelevant HTML elements
* Generate Persian summaries
* Run completely locally with Ollama

## Requirements

* Python 3.9+
* Ollama
* Qwen 3 4B model

## Installation

```bash
pip install -r requirements.txt
ollama pull qwen3:4b
```

## Run

```bash
python main.py
```

## Project Structure

```text
.
├── main.py
├── scraper.py
├── requirements.txt
└── README.md
```

## Technologies

* Python
* Ollama
* Qwen 3 4B
* BeautifulSoup
* Requests
