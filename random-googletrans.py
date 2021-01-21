# -*- coding: iso-8859-1 -*-
#Google Translator "Breaker" by https://github.com/quasarKroete
#originally made to mess up the .lang file from Galaxy on Fire 2
import random
import time
import googletrans
from googletrans import Translator

isquit = False

def stringlengthhex(stringtocount):
    '''
    Diese Funktion zeigt die Länge des strings in Decimal und Hexadecimal an.
    '''

    stringlength = len(stringtocount)

    stringlengthhex = hex(stringlength)

    print('String length in dec: ' + str(stringlength))

    print('String length in hex: ' + str(stringlengthhex))


def breaktranslation():
    '''
    Diese Funktion übersetzt, wie oft der Benutzer will, einen String durch
    mehrere zufällige Sprachen durch googletrans. Das Ziel ist, dass am Ende totaler Blödsinn rauskommt.
    Kann auch eine Liste an Sprachen nehmen
    '''

    translator = Translator()

    stringuntranslated = input('Enter the String: ')
    stringfortrans = stringuntranslated
    #main language of text
    mainlang = str(input("What language is the Text in? For example : en = English, de = German (ISO 639-1 Codes)\n"))

    
    
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
        listoflangs = answer.split(";")
    

    priorlang = mainlang

    if withlist == False:
        #number of translations
        numoftrans = int(input("How many times do you want it to be translated?\n"))
        print(stringuntranslated)
        stringlengthhex(stringuntranslated)
        for i in range(0, numoftrans):

            nextlang = random.choice(list(googletrans.LANGUAGES))
            print(priorlang + "->" + nextlang)
            
            translation = translator.translate(stringfortrans, src = priorlang, dest = nextlang)

            priorlang = nextlang

            #Um es zu verhindern, dass man kurzzeitig "geblockt" wird. Verhindert es nicht komplett,
            #aber ich versuche alles um das irgendwie zu umgehen
            time.sleep(0.5)

            stringfortrans = translation.text

        finaltext = translator.translate(stringfortrans, dest = mainlang)
        print(priorlang + "->" + mainlang)
        if finaltext.text == stringuntranslated:
            #Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
            #aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
            #was dazu führt, dass ich kurz "blockiert" werde.
            print("String could not be translated. Please try again later")
            print("\nResult: \n"+ finaltext.text+ "\n")

        else:
            print("\nResult: \n"+ finaltext.text+ "\n")
            stringlengthhex(finaltext.text)
    
    elif withlist == True:
        print(stringuntranslated)
        stringlengthhex(stringuntranslated)
        for i in listoflangs:

            nextlang = i
            print(priorlang + "->" + nextlang)
            
            translation = translator.translate(stringfortrans, src = priorlang, dest = nextlang)

            priorlang = nextlang

            #Um es zu verhindern, dass man kurzzeitig "geblock" wird. Verhindert es nicht komplett,
            #aber ich versuche alles um das irgendwie zu umgehen
            time.sleep(0.5)

            stringfortrans = translation.text

        finaltext = translator.translate(stringfortrans, dest = mainlang)
        print(priorlang + "->" + mainlang)
        if finaltext.text == stringuntranslated:
            #Fehler, der erscheint wenn man zu schnell/oft übersetzt. Ich hab zwar kaum Ahnung von Servern und sowas,
            #aber ich schätze dass es damit zu tun hat, dass zu schnell zu oft Sachen an die Google-Server geschickt werden,
            #was dazu führt, dass ich kurz "blockiert" werde.
            print("String could not be translated. Please try again later")
            print("\nResult: \n"+ finaltext.text+ "\n")

        else:
            print("\nResult: \n"+ finaltext.text+ "\n")
            stringlengthhex(finaltext.text)

    else:
        print("Something went wrong")

#mainloop
#Kleine Input möglichkeit, weil ich es cool fand
while isquit == False:

    antwort = input("What do you want to do?\n1: 'translate'\n2: count\n3: quit\nEnter of one the numbers: ")

    if antwort == '1':
        breaktranslation()
        time.sleep(2)
    elif antwort == '2':

        tocount = str(input("Enter the string: "))
        stringlengthhex(tocount)

        time.sleep(2)

    elif antwort == '3':
        isquit = True
    
    else:
        print("Answer not Valid: Please enter 1, 2 or 3")

        time.sleep(2)
