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

#Creating the object for class
r = sr.Recognizer()
trans = GoogleTranslator()

#Writing code
while True:
    #Using microphone class to access microphone
    with sr.Microphone() as source:
        print("Speak now!")
        #Listening audio using microphone
        audio = r.listen(source)
    try:
        #recognising the audio which we spoke
        speak = r.recognize_google(audio)
        if speak == 'exit':
            break
    #creating except block
    except sr.UnknownValueError:
        print("Couldn't Understand")
    except sr.RequestError:
        print("Couldn't request result from Google")
    #translating the audio to target language
    text = GoogleTranslator(source='auto', target='te').translate(text=speak)
    print("Speaked Language:{}".format(speak))
    print("Translated Language:{}".format(text))

    #generating voice and saving
    voice = gTTS(text, lang='te')
    voice.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")
