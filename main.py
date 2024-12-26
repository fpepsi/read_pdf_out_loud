import os
from dotenv import load_dotenv
from google.cloud import texttospeech
import PyPDF2

pdf_path = 'files/test.pdf'
load_dotenv()
api_key_string = os.environ.get('API_KEY')


# pdf to text section
def pdf_to_text(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


# text to speech section
def authenticate_with_api_key(api_key_string: str, text) -> None:
    # Limits the string size to 5000 bytes
    text = text.encode('utf-8')[:5000]

    # Instantiates a client
    client = texttospeech.TextToSpeechClient(client_options={"api_key": api_key_string})

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("files/output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "files/output.mp3"')

text = pdf_to_text(pdf_path)
authenticate_with_api_key(api_key_string, text)