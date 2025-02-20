#Anna Julia  Cajado Bonadiman | Murilo Oliveira Quartezani | Luiz Felipe Kretli
import speech_recognition as sr

def ouvindo():

    rec = sr.Recognizer()

    with sr.Microphone(0) as microfone:

        rec.adjust_for_ambient_noise(microfone)
        print('\n\t\tOuvindo...')

        audio = rec.listen(microfone)

        try: 
            texto = rec.recognize_google(audio, language='pt-BR')
            print('\n\t\t', texto)
            return texto.split()
        except sr.UnknownValueError:
            print('\n\t\tLetra não entendida, tente novamente')
            return None
        except sr.RequestError:
            print('\n\t\tErro do sistema de voz')
            return None

