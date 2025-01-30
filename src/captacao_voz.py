import speech_recognition as sr

def ouvindo():

    rec = sr.Recognizer()
    #ESSA MERDA É TERRIVEL PELO AMOR DE DEUS 
    with sr.Microphone(0) as mic:
        rec.adjust_for_ambient_noise(mic)

        print('Gravando . . .')

        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        print(texto)
        letra = str(texto)

        return letra

