import os
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub

def convert_epub_to_txt(input_file, output_file):
    # Load the EPUB file
    book = epub.read_epub(input_file)

    # Extract the text content from the EPUB
    text_content = ""
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        text_content += soup.get_text() + "\n"

    # Save the text content to a TXT file
    with open(output_file, "w", encoding="utf-8") as txt_file:
        txt_file.write(text_content)

    print("EPUB converted to TXT successfully!")

# Example usage
input_file = "/Users/rafaeldias/Projetos/epubtoaudio/data/amanha.epub"
output_file = "/Users/rafaeldias/Projetos/epubtoaudio/data/output.txt"
convert_epub_to_txt(input_file, output_file)
