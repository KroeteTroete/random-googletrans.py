# -*- coding: iso-8859-1 -*-
#Google Translator "Breaker" by https://github.com/KroeteTroete
#originally made to mess up the .lang file from Galaxy on Fire 2
#This uses googletrans3.1.0a0 to prevent AttributeError: 'NoneType' object has no attribute 'group' https://stackoverflow.com/a/65109346/15056366
#pip install googletrans==3.1.0a0
import random
import time
import googletrans
from googletrans import Translator

isquit = False

def stringLengthHex(stringtocount):
    '''
    Diese Funktion zeigt die Länge des strings in Decimal und Hexadecimal an.
    '''

    stringlength = len(stringtocount)

    stringLengthHex = hex(stringlength)

    print('String length in dec: ' + str(stringlength))

    print('String length in hex: ' + str(stringLengthHex))


def breakTranslation():
    '''
    Diese Funktion übersetzt, wie oft der Benutzer will, einen String durch
    mehrere zufällige Sprachen durch googletrans. Das Ziel ist, dass am Ende totaler Blödsinn rauskommt.
    Kann auch eine Liste an Sprachen nehmen
    '''

    translator = Translator()

    stringUntranslated = input('Enter the String: ')
    stringForTrans = stringUntranslated
    #main language of text
    mainLang = str(input("What language is the Text in? For example : en = English, de = German (ISO 639-1 Codes)\n"))



    #random or defining a list of languages
    #note: Diese Lösung ist dumm
    inloop = True
    while inloop == True:
        withlist = str(input("Do you want the languages to be chosen randomly or define a list of languages?\n1: random\n2: list\n"))
        if withlist == "1":
            withlist = False
            inloop = False
        elif withlist == "2":
            withlist = True
            inloop = False
        else:
            print("Not a valid answer. Please enter one of the numbers")

    if withlist == True:
        answer = input("Enter the list of languages. Each ISO-639-1 Code should be seperated by ';'\nFor example: en;de;es;fr;la\nThe Language the text is in will be appended automatically\n")
        listOfLangs = answer.split(";")

    inloop = True
    while inloop == True:
        retranslation = str(input("Do you want to enable retranslation? (The retranslation will not be used in the translations after it)\n1: Yes\n2: No\n"))
        if retranslation == "1":
            retranslation = True
            inloop = False
        elif retranslation == "2":
            retranslation = False
            inloop = False
        else:
            print("Not a valid answer. Please enter one of the numbers")


    priorLang = mainLang

    if withlist == False and retranslation == True:
        #number of translations
        numoftrans = int(input("How many times do you want it to be translated?\n"))
        print(stringUntranslated)
        stringLengthHex(stringUntranslated)
        for i in range(0, numoftrans):

            nextLang = random.choice(list(googletrans.LANGUAGES))
            print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[nextLang])

            translation = translator.translate(stringForTrans, src = priorLang, dest = nextLang)

            #Experimental
            TranslationInmainLang = translator.translate(translation.text, src = nextLang, dest = mainLang)
            print(TranslationInmainLang.text)

            priorLang = nextLang

            #Um es zu verhindern, dass man kurzzeitig "geblockt" wird. Verhindert es nicht komplett,
            #aber ich versuche alles um das irgendwie zu umgehen
            time.sleep(0.5)

            stringForTrans = translation.text

        finaltext = translator.translate(stringForTrans, dest = mainLang)
        print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[mainLang])
        if finaltext.text == stringUntranslated:
            #Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
            #aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
            #was dazu führt, dass ich kurz "blockiert" werde.
            print("String could not be translated. Please try again later")
            print("\nResult: \n"+ finaltext.text+ "\n")

        else:
            print("\nResult: \n"+ finaltext.text+ "\n")
            stringLengthHex(finaltext.text)

    elif withlist == False and retranslation == False:
        #number of translations
        numoftrans = int(input("How many times do you want it to be translated?\n"))
        print(stringUntranslated)
        stringLengthHex(stringUntranslated)
        for i in range(0, numoftrans):

            nextLang = random.choice(list(googletrans.LANGUAGES))
            print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[nextLang])

            translation = translator.translate(stringForTrans, src = priorLang, dest = nextLang)

            priorLang = nextLang

            #Um es zu verhindern, dass man kurzzeitig "geblockt" wird. Verhindert es nicht komplett,
            #aber ich versuche alles um das irgendwie zu umgehen
            time.sleep(0.5)

            stringForTrans = translation.text

        finaltext = translator.translate(stringForTrans, dest = mainLang)
        print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[mainLang])
        if finaltext.text == stringUntranslated:
            #Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
            #aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
            #was dazu führt, dass ich kurz "blockiert" werde.
            print("String could not be translated. Please try again later")
            print("\nResult: \n"+ finaltext.text+ "\n")

        else:
            print("\nResult: \n"+ finaltext.text+ "\n")
            stringLengthHex(finaltext.text)

    elif withlist == True and retranslation == True:
        print(stringUntranslated)
        stringLengthHex(stringUntranslated)
        for i in listOfLangs:

            nextLang = i
            print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[nextLang])

            translation = translator.translate(stringForTrans, src = priorLang, dest = nextLang)

            #Experimental
            TranslationInmainLang = translator.translate(translation.text, src = nextLang, dest = mainLang)
            print(TranslationInmainLang.text)

            priorLang = nextLang

            #Um es zu verhindern, dass man kurzzeitig "geblock" wird. Verhindert es nicht komplett,
            #aber ich versuche alles um das irgendwie zu umgehen
            time.sleep(0.2)

            stringForTrans = translation.text

        finaltext = translator.translate(stringForTrans, dest = mainLang)
        print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[mainLang])
        if finaltext.text == stringUntranslated:
            #Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
            #aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
            #was dazu führt, dass ich kurz "blockiert" werde.
            print("String could not be translated. Please try again later")
            print("\nResult: \n"+ finaltext.text+ "\n")

        else:
            print("\nResult: \n"+ finaltext.text+ "\n")
            stringLengthHex(finaltext.text)

    elif withlist == True and retranslation == False:
        print(stringUntranslated)
        stringLengthHex(stringUntranslated)
        for i in listOfLangs:

            nextLang = i
            print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[nextLang])

            translation = translator.translate(stringForTrans, src = priorLang, dest = nextLang)

            priorLang = nextLang

            #Um es zu verhindern, dass man kurzzeitig "geblock" wird. Verhindert es nicht komplett,
            #aber ich versuche alles um das irgendwie zu umgehen
            time.sleep(0.2)

            stringForTrans = translation.text

        finaltext = translator.translate(stringForTrans, dest = mainLang)
        print(googletrans.LANGUAGES[priorLang] + " -> " + googletrans.LANGUAGES[mainLang])
        if finaltext.text == stringUntranslated:
            #Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
            #aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
            #was dazu führt, dass ich kurz "blockiert" werde.
            print("String could not be translated. Please try again later")
            print("\nResult: \n"+ finaltext.text+ "\n")

        else:
            print("\nResult: \n"+ finaltext.text+ "\n")
            stringLengthHex(finaltext.text)

    else:
        print("Something went wrong")


#mainloop
#Kleine Input möglichkeit, weil ich es cool fand
while isquit == False:

    antwort = input("What do you want to do?\n1: 'translate'\n2: count\n3: quit\nEnter of one the numbers: ")

    if antwort == '1':
        breakTranslation()
        time.sleep(2)
    elif antwort == '2':

        tocount = str(input("Enter the string: "))
        stringLengthHex(tocount)

        time.sleep(2)

    elif antwort == '3':
        isquit = True

    else:
        print("Answer not Valid: Please enter 1, 2 or 3")

        time.sleep(2)
