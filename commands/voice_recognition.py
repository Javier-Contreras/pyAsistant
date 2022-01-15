import speech_recognition as sr

r = sr.Recognizer()


def voice2speech(threshold=200):
    global r
    with sr.Microphone() as source:
        audio = r.listen(source)
        #audio = r.record(source, duration=5)
        said = ""

        try:
            print("Empieza a reconocer")
            said = r.recognize_google(audio, language="es-ES")
            print("Reconoce")
            print(said)
        except Exception as e:
            print("Error:", str(e))
    return said.lower()


def time_recognition():
    global r
    r.energy_threshold = 200
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:
        print("Empieza a escuchar")
        audio = r.record(source, duration=4)
        said = ""

        try:
            print("Empieza a reconocer")
            said = r.recognize_google(audio, language="es-ES")
            print("Reconoce")
            print(said)
        except Exception as e:
            print("Error:", str(e))
    return said.lower()
"""
    r = sr.Recognizer()
    r.energy_threshold = 400
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-ES")
            return text

        except:
            print("Sorry could not recognize what you said")
            return ""
"""
