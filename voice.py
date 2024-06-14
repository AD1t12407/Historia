import os
import streamlit as st
from google.cloud import texttospeech
from io import BytesIO

# Set up Google Cloud authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="./mythic-chalice-426409-d9-5c87d58fa64c.json"

# Initialize Google Cloud Text-to-Speech client
client = texttospeech.TextToSpeechClient()

def synthesize_text(text, language_code="en-US", gender=texttospeech.SsmlVoiceGender.NEUTRAL):
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, ssml_gender=gender
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)
    return response.audio_content

def main():
    st.title("Google Cloud Text-to-Speech in Streamlit")
    text_input = "hello world!"
    language = st.selectbox("Select Language:", ["en-US", "en-GB", "fr-FR", "de-DE"])
    gender = st.selectbox("Select Voice Gender:", ["Neutral", "Male", "Female"])

    gender_map = {
        "Neutral": texttospeech.SsmlVoiceGender.NEUTRAL,
        "Male": texttospeech.SsmlVoiceGender.MALE,
        "Female": texttospeech.SsmlVoiceGender.FEMALE,
    }

    if st.button("Convert to Speech"):
        if text_input:
            with st.spinner("Generating speech..."):
                audio_content = synthesize_text(text_input, language, gender_map[gender])
                st.audio(BytesIO(audio_content), format="audio/mp3")

if __name__ == "__main__":
    main()