from PyPDF2 import PdfReader, PdfMerger
import os
import requests
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config_path = os.path.join(BASE_DIR, "config.json")

with open(config_path, "r") as c:
    config = json.load(c)

user_api = config["API"]
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {user_api}"}


def show_pdf_files():
    print("📁-----Seus arquivos-----📁\n".center(70))
    try:
        for file in os.listdir("./documents/pdf"):
            if file.endswith(".pdf"):
                print(f"📙 - {file}".center(70))
        print("=" * 70)
    except Exception:
        print("Falha ao carregar arquivos...")


def save_txt(content):
    title = str(input("Titulo para o arquivo.txt: "))
    try:
        path = f"./documents/txt/{title}.txt"
        with open(path, "w") as f:
            f.write(content)
        print(f"Pronto! o arquivo {title}.txt foi salvo.")
    except Exception as e:
        print(f"Falha ao salvar {title}.txt")


def split_text(text, max_words=300):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i : i + max_words])


def summarize_text(content):
    try:
        payload = {"inputs": content}
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result[0]["summary_text"]
        else:
            print(f"Error: {response.status_code}")
            print("Response:", response.text)
            return None
    except Exception:
        print("Erro desconhecido.")


def summarize_chunks(content):
    try:
        parts = []
        for chunk in split_text(content):
            summary = summarize_text(chunk)
            if summary:
                parts.append(summary)
        full_summary = " ".join(parts)
        return summarize_text(full_summary)
    except Exception:
        print("Erro desconhecido.")


def extract_pdf_to_txt(file):
    if file.endswith(".pdf"):
        try:
            reader = PdfReader(file)
            content = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    content += text + "\n"
            save_txt(content)
        except Exception as e:
            print("Falha ao extrair texto. (cheque seu arquivo)")


def manage_summary(file):
    if file.endswith(".pdf"):
        try:
            reader = PdfReader(file)
            content = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    content += text + "\n"
            print("> PDF carregado.\n")
            option = input(
                """
            [1] Visualizar o resumo agora
            [2] Exportar o resumo para um arquivo txt
            Option: """
            )
            if option.isnumeric():
                match option:
                    case "1":
                        summary = summarize_chunks(content)
                        print("\nResumo:\n", summary)
                    case "2":
                        save_txt(summarize_chunks(content))
        except Exception as e:
            print(f"Erro: {e}")
            return ""
    else:
        print("Esse arquivo não é um PDF!")
        return ""


def merge_pdfs():
    merger = PdfMerger()
    try:
        num = int(input("Quantos arquivos?: "))
        c = 0
        pdfs = []
        while c < num:
            filename = input(f"arquivo {c + 1}: ")
            if ".pdf" in filename:
                filename = filename.replace(".pdf", "")
            file = f"./documents/pdf/{filename}.pdf"
            pdfs.append(file)
            c += 1

        for pdf_file in pdfs:
            merger.append(pdf_file)

        pdf_merger_name = input("Nome para o novo PDF: ")
        if ".pdf" in pdf_merger_name:
            pdf_merger_name = pdf_merger_name.replace(".pdf", "")

        merger.write(f"./documents/pdf/{pdf_merger_name}.pdf")
        merger.close()
        print(f"Salvo em ./documents/pdf/{pdf_merger_name}.pdf")

    except Exception as e:
        print(f"Erro: {e}")