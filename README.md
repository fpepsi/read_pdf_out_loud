# read_pdf_out_loud
Load your pdf files and have your computer read them for you
Both input pdf files and output mp3 files must be placed on a "files" folder to be handled by the code 
This program version uses basic PyPDF2 library and limits thetext output to 5000 bytes to comply with google cloud limit

"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""