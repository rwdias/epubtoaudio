# /Users/rafaeldias/anaconda3/bin/python

import os
from gtts import gTTS
import ebooklib
from ebooklib import epub

book = epub.read_epub('/Users/rafaeldias/Projetos/epubtoaudio/data/amanha.epub')

def convert_epub_to_audiobook(input_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the EPUB file
    book = epub.read_epub(input_file)

    # Extract the text content from the EPUB
    text_content = ""
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        text_content += item.get_content().decode("utf-8") + "\n"

    # Convert the text to speech
    tts = gTTS(text=text_content, lang='pt-br')
    audio_file = os.path.join(output_folder, "output.mp3")
    tts.save(audio_file)

    print("Audiobook generated successfully!")

# Example usage
input_file = "/Users/rafaeldias/Projetos/epubtoaudio/data/amanha.epub"
output_folder = "/Users/rafaeldias/Projetos/epubtoaudio/data"
convert_epub_to_audiobook(input_file, output_folder)
