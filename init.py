import speech_recognition as sr

def get_speech():
    recognizer = sr.Recognizer()
        
    with sr.Microphone() as audio_src:
        recognizer.adjust_for_ambient_noise(audio_src)
        
        print('Say something... ')
        speech = recognizer.listen(audio_src)
        
        try:
            text = recognizer.recognize_google(speech, language='en-US')
            
            print('Got something... ', text)
        except sr.UnknownValueError:
            print('Something went wrong')

if __name__ == '__main__':
    get_speech()