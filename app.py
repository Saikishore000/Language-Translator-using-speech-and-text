#Importing required libraries for Speech recognition and translation

import speech_recognition as sr
#The above module is used for speech recognition

from deep_translator import GoogleTranslator
#The above module is used for translate

from gtts import gTTS
#The above module is used for google text to speech

from playsound import playsound
#The above module is used for playing sounds
import os

import streamlit as st
#streamlit module is used to create webapp
import datetime as dt

#Creating the object for class
r = sr.Recognizer()
trans = GoogleTranslator()

# -*- coding: utf-8 -*-
"""
@author: Satyala Saikishore
"""

#Creating the background for webapp
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2020/05/29/03/00/portuguese-5233295_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

#date display
now = dt.date.today()

#Text Display
st.write(f"Today's date:{now}")

#Title for webapp
st.title("Language Translator by typing text")

#Source lanuage and Target language
src_lang = trans.get_supported_languages(as_dict=True)
trg_lang = trans.get_supported_languages(as_dict=True)

#Creating columns
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", src_lang)
with col2:
    dest_lang = st.selectbox("Target Language", trg_lang)

#Text to enter to translate
text = st.text_input("Enter text to translate:")

#Creating button
if st.button("Translate"):
    result = GoogleTranslator(source=source_lang, target=dest_lang).translate(text=text)
    st.success(result)

#Title for audio translation
st.title("Language Translator by voice")
if st.button("Audio Translate"):
    st.success("Speak Now!")
    with sr.Microphone() as source:
        audio = r.listen(source)

    #Creating try and except block to handle error
    try:
        speak = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Couldn't Understand")
    except sr.RequestError:
        print("Couldn't request result from Google")

    #Translating audio to target language
    text = GoogleTranslator(source='auto', target='te').translate(text=speak)
    st.text("Speaked Language:{}".format(speak))
    st.text("Translated Language:{}".format(text))

    #Genearting voice
    voice = gTTS(text, lang='te')
    voice.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")