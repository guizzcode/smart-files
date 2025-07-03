import os
from .menus import *
from utils import clear
from services import *

def run():
    while True:
        initial_menu()
        option = input('Option: ')
        if option.isnumeric():
            match option:
                case '1':
                    clear()
                    show_pdf_files()
                    pdf_options()
                    option = input('Option: ')
                    if option.isnumeric():
                        try:
                            match option:
                                case '1':
                                    file = input('Why file?: ')
                                    if '.pdf' in file:
                                        file = file.replace('.pdf', '')
                                    manage_summary(f'./documents/pdf/{file}.pdf')                                
                                    
                                case '2':
                                    file = input('Why file?: ')
                                    if '.pdf' in file:
                                         file = file.replace('.pdf', '')
                                    extract_text_to_txt(f'./documents/pdf/{file}.pdf')
                                
                                case '3':
                                    merge_pdfs()
                                    
                                case '4':
                                    clear()
                        except Exception as e:
                            print(f'Error: {e}')         
                            continue                          
                    else:
                        print ('Only numbers in 1-4.')    
                        continue                                                              
                case '2':
                    clear()
                    break
        else:
            print ('Only numbers.')
            continue