import speech_recognition as sr
import sys
while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as sourse:
        print('Говорите:')
        audio = r.listen(sourse)
    try:
        query = r.recognize_google(audio, language='ru-RU').lower()
        print('->' + query)
        if query in ('привет','хай','здравствуй','прив','здорово','здравствуйте','алло'):
            print('Здравствуйте')
        elif query in ('пока','покеда','прощай','до свидания','до встречи','закройся','конец общения','конец разговора','выключись'):
            print('До свидания')
            sys.exit()
    except SystemExit:
        sys.exit()
    except:
        print()
