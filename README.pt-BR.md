📄 🇺🇸 English version: [README.md](README.md)  

# Smart Files

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/status-Em--Desenvolvimento-yellow?style=for-the-badge" />
</p>

![banner](banner.png)

> Este projeto tem como foco o gerenciamento de arquivos PDF e TXT para simplificar conversões, leitura e processamento, com integração de IA.

## ✨ Funcionalidades

- 🤖 Resumo automático de arquivos PDF e TXT com IA.
- 📖 Conversão de arquivos (PDF, TXT) para texto simples.
- 📚 Mesclagem de múltiplos arquivos PDF em um só.
- 📄 Extração de texto bruto de documentos PDF.

## ⚙️ Requisitos

- Python3  
- requests

## 🔐 Token de API (Obrigatório)

Para usar a função de resumo, você precisa de um token de API do Hugging Face.

1. Acesse [hugging face](https://huggingface.co/settings/tokens).  
2. Crie um novo token (permissão de leitura é suficiente).  
3. Copie o token e cole no seu arquivo `config.json`.

## 🚀 Como Executar

1. Instale os requisitos.
``` bash
    pip install -r requirements.txt
```
2. Rode o arquivo main.py!
``` bash
    python3 src/main.py 
```

## ❓ Como Usar

Você deve mover seus arquivos (PDF ou TXT) para as pastas designadas (src/documents/pdf ou src/documents/txt) antes de usar a aplicação.

## 📝 Licença

Licenciado sob a [Licença MIT](LICENSE).