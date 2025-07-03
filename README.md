# Smart Files

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/status-In--Development-yellow?style=for-the-badge" />
</p>

![banner](banner.png)

> This project focuses on managing PDF and TXT files to simplify conversions, reading, and processing, with AI integration.

## ✨ Features

- 🤖 AI-powered PDF and TXT summarization.
- 📖 Convert files (PDF, TXT) to plain text.
- 📚 Merge multiple PDF files into one.
- 📄 Extract raw text from PDF documents.

## ⚙️ Requirements

- Python3
- requests

## 🔐 API Token (Required)

To use the summarization feature, you need a Hugging Face API token.

1. Go to [hugging face](https://huggingface.co/settings/tokens).
2. Create a new token. (read access is enough)
3. Copy the token and paste it into your `config.json` file.

## 🚀 How to Run

1. Install requirements.
``` bash
    pip install -r requirements.txt
```
2. Run the main.py file!
``` bash
    python3 src/main.py 
```

## ❓ How to use

You need to move your files (PDF or TXT) to the designated folders (src/documents/pdf or src/documents/txt) before using the application.

## 📝 License

Licensed under the [MIT License](LICENSE).