import fitz
import re
from bs4 import BeautifulSoup
import os
import glob
import requests
from datetime import datetime
from pathlib import Path


FILES_DIR = Path(__file__).resolve().parent.parent.joinpath('files')
URL = "https://habr.com/ru/news/t/721172/"
URL_TEST_HTML = 'https://webformyself.com/kak-skachat-fajly-v-python/'
URL_TEST_PDF = 'https://www.africau.edu/images/default/sample.pdf'


def text_from_pdf(file_in: str, file_out: str) -> bool:
    try:
        doc = fitz.open(file_in)
        if doc.is_pdf:
            with open(file_out, "w") as out:
                for page in doc.pages():
                    text = page.get_text()

                    out.write(''.join(re.findall(r'\s{,1}\S', text)))

            return True
    except Exception as e: # fitz.fitz.FileDataError
        return False


def text_from_html(file_in: str, file_out: str):

    with open(file_in, 'r') as html:
        text_in = html.read()
    # UnicodeDecodeError
    result = ''
    soup = BeautifulSoup(text_in, 'html.parser')
    divs = soup.find_all('div')
    for div in divs:
        ps = div.find_all('p')
        for p in ps:
            result += p.get_text()

    if result:
        result = ''.join(re.findall(r'\s{,1}\S', result))
        with open(file_out, "w") as out:
            out.write(result)
        return True
    return False


def get_file_from_link(url: str, temp_filename: str) -> bool:
    req = requests.get(url)
    if req.status_code:
        with open(temp_filename, 'wb') as file:
            file.write(req.content)
            return True
    return False


def temp_file_name() -> str:
    name = [s for s in str(datetime.now()) if s.isdigit()]
    return ''.join(name)


def get_text_from_link(link_url: str):
    filename = str(FILES_DIR.joinpath(temp_file_name()))
    get_file_from_link(link_url, filename)

    if text_from_pdf(filename, str(filename) + '.txt'):
        return filename + '.txt'
    else:
        if text_from_html(str(FILES_DIR.joinpath(filename)), str(filename) + '.txt'):
            return str(filename) + '.txt'
    return None


def remove_all_temp_files():
    for file in os.scandir(FILES_DIR):
        os.remove(FILES_DIR.joinpath(file))
