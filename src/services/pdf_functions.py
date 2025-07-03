from PyPDF2 import PdfReader, PdfMerger  
import os  
import requests  
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config_path = os.path.join(BASE_DIR, 'config.json')

with open(config_path, 'r') as c:
    config = json.load(c)

user_api = config['API']
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"  
headers = {  
    "Authorization": f"Bearer {user_api}"  
}  
  
def show_pdf_files():  
    print('📁-----These are your files-----📁\n'.center(70))  
    for file in os.listdir('./documents/pdf'):  
        if file.endswith('.pdf'):  
            print(f'📙 - {file}'.center(70))  
    print('=' * 70)  
  
  
def save_txt(content):  
    title = str(input('Title for the TXT file: '))  
    try:  
        path = f"./documents/txt/{title}.txt"  
        with open(path, 'w') as f:  
            f.write(content)  
        print(f'Done! The file {title}.txt was saved.')  
    except Exception as e:  
        print(f'Error: {e}')  
  
  
def split_text(text, max_words=300):  
    words = text.split()  
    for i in range(0, len(words), max_words):  
        yield ' '.join(words[i:i+max_words])  
  
  
def summarize_text(content):  
    payload = {"inputs": content}  
    response = requests.post(API_URL, headers=headers, json=payload)  
    if response.status_code == 200:  
        result = response.json()  
        return result[0]["summary_text"]  
    else:  
        print(f"Error: {response.status_code}")  
        print("Response:", response.text)  
        return None  
  
  
def summarize_chunks(content):  
    parts = []  
    for chunk in split_text(content):  
        summary = summarize_text(chunk)  
        if summary:  
            parts.append(summary)  
    full_summary = " ".join(parts)  
    return summarize_text(full_summary)  
  
  
def extract_text_to_txt(file):  
    if file.endswith('.pdf'):  
        try:  
            reader = PdfReader(file)  
            content = ""  
            for page in reader.pages:  
                text = page.extract_text()  
                if text:  
                    content += text + '\n'  
            save_txt(content)  
        except Exception as e:  
            print(f'Error: {e}')  
  
  
def manage_summary(file):  
    if file.endswith('.pdf'):  
        try:  
            reader = PdfReader(file)  
            content = ""  
            for page in reader.pages:  
                text = page.extract_text()  
                if text:  
                    content += text + '\n'  
            print('> PDF loaded.\n')  
            option = input('''  
            [1] View summary now  
            [2] Export summary to TXT file  
            Option: ''')  
            if option.isnumeric():  
                match option:  
                    case '1':  
                        summary = summarize_chunks(content)  
                        print('\nSummary:\n', summary)  
                    case '2':                                 save_txt(summarize_chunks(content))  
        except Exception as e:  
            print(f'Error: {e}')  
            return ""  
    else:  
        print('This file is not a PDF!')  
        return ""
        
        
def merge_pdfs():
    merger = PdfMerger()
    try:
        num = int(input('How many files?: '))
        c = 0
        pdfs = []
        while c < num:
            filename = input(f'filename{c + 1}: ')
            if '.pdf' in filename:
                filename = filename.replace('.pdf', '')
            file = f'./documents/pdf/{filename}.pdf'
            pdfs.append(file)
            c += 1
            
        for pdf_file in pdfs:
            merger.append(pdf_file)
            
        pdf_merger_name = input('New pdf name: ')
        if '.pdf' in pdf_merger_name:
             pdf_merger_name = pdf_merger_name.replace('.pdf', '')
         
        merger.write(f'./documents/pdf/{pdf_merger_name}.pdf')
        merger.close()
        print(f"Merged PDF saved as ./documents/pdf/{pdf_merger_name}.pdf'")
 
    except Exception as e:
         print(f'Error: {e}')