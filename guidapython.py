# -- Print


# Cosa è: la funzione "print()" serve per dire al programma di scrivere qualcosa


print("Hello World!")


# str: Nel caso il software deve scrivere dei numeri bisognia specificare str prima della funzione che scrive il numero
# Importante: bisogna sempre mettere la virgola "," per separare le due condizioni


print("Hello World!", str(2)) # in questo caso verra scritto 2 se cambiate il numero in lettere dara errore


# -- Variabili


# A cosa servono: hanno dieversi utilizzi, possono essere usate per riferire più volte alla stessa cosa ma anche per dichiarare alcune funzioni
# Booleane / Stringe / Intere : le variabili possono essere di 3 tipi 


var1 = True # Booleana (il nome è a scelta pero non si possono mettere spazzi) e può essere solo True o False

var2 = "Hello World" # Stringa, questa variabile si usa per riferirsi a un testo

var3 = 1 # Intere, si usa per riferirsi a un valore numerico

var4 = 1.5 # Intere, cambia solo che per fare il decimale si usa il punto


# -- Printare una variabile


# Ci sono due modi per printare una variabile:

print(var2) # primo: questo metodo viene utilizzato quando bisogna far scrivere solo la variavile

print(f"Ciao ecco la variabile : {var2}") # secondo: questo metodo viene utilizzato quando bisogna far scrivere una variabile nel mezzo di un testo

# Importante: se usi il secondo metodo devi specificare f prima delle graffette altrimenti non verra rilevata come variabile


# -- Trasformazione di una variabile


# da stringa a intero: se serve possiamo trasformare una variabile da str a int
# da intero a stringa: o da int a str


a = 1
variabile = str(a) # Si usa la funzione str() mettendo tra le parentesi la variabile da transformare

# Per convertire deve essere una condizione: la variabile stringa non deve avere parole all'interno, SOLO NUMERI altrimenti dara' errore

b = "1234"
variabile = int(b)


# -- If / Elif / Else


# A cosa servono: come si può capire questa funzione serve per determinare delle possibilita di una variabile o di un input
# Limiti: non ci sono limiti su quanti "elif" puoi mettere ne puoi mettere sostanzialmente infiniti


var5 = "A"

var5.upper() # si usa in modo che se l'input è "a" o "A" (maiuscolo o minuscolo) il software lo legga solo come maiuscolo in modo da evitare errori (esiste anche .lower())

if var5 == "A": # Pensate a "if" come se fosse un "se"

    print("La variabile dice A")

elif var5 == "B": # Pensate a "elif" come se fosse un "invece se"

    print("La variabile dice B")

else: # Pensate a "else" come se fosse "in qualunque altro caso"

    print("La variabile non dice ne A ne B")


# -- Input


# Cosa sono: l'input è una funzione che ci permette di dare al software una stringa


var6 = input("scrivi cio che vuoi --> ") # per creare un input come prima cosa devi definirlo come variabile in seconda cosa devi chiamare la funzione e per ultima cosa mettere un messaggio (opzionale) 

var6.upper() # si usa in modo che se l'input è "a" o "A" (maiuscolo o minuscolo) il software lo legga solo come maiuscolo in modo da evitare errori (esiste anche .lower())

if var6 == "A": # Pensate a "if" come se fosse un "se"

    print("La variabile input dice A")

elif var6 == "B": # Pensate a "elif" come se fosse un "invece se"

    print("La variabile input dice B")

else: # Pensate a "else" come se fosse "in qualunque altro caso"

    print("La variabile input non dice ne A ne B")


# -- Liste e Dizionari


# Cosa sono: le liste sono delle variabili che ti permettono di salvare dati, i dizionari sono delle tabelle dove possiamo assegnare un corrispondente a lettere, simboli o parole

list1 = [1234, "ciao"] # Possono contenere vari dati misti (sia stringhe che numeri)

diz1 = {"N":"1", "n":1, 1:"n1"} # Hanno una parola chiave a cui viene assegnata un informazione / variabile


# -- Numerazione item in una lista


# nel caso vogliamo avere un numero di tutti i valori presenti in una lista dobbiamo usare la funzione "len"

list2 = ["a", "b", "c"]

numero_item = len(list2)

# Attemzione: i valori di len partono da 0 quindi in questo n_valori sara' uguale a 2
# Attemzione: i valori che da la funzione len sono variabili intere


# -- For

# La funzione for viene usata per esaminare ogni elemento a lista a singolo
# Per vedere se un elemento si trova nella lista si usa:

list3 = ["ciao", "salute", "come va?"]

for elementi in list3: # Si assegna una parola a piacere al nome che prendera' ogni elemento in questo caso elementi

    if elementi == "salute": 

        print("la parola salute si trova nella lista") 

    else: # Se non si verifica la prima condizione esegue questa funzione else

        print("la parola salute non si trova nella lista")


# -- Come contare / funzione break

# Obiettivo: Contare gli elementi fino alla parola "ciao"

lista = [11, 2, 36, 4, 5, 6, 37, 8, 94, 80, "ciao", 345, 3619, 265289, 2580]

numero = 0

for elemento in lista:

    # Se la variabile è un intero si può usare la funzione += che permette di aggiungere un valore a quello già esistente
    numero += 1 # In questo caso lui aggiunge 1 per ogni elemento in lista

    if str(elemento) == "ciao": # Controlla se l'elemento è uguale alla parola ciao 

        # (ATTENZIONE: bisogna usare la funzione str() perchè non si può vedere se un intero è uguale ad una variabile stringa)

        break # Funzione che interrompe la funzione for fermando il codice

# Alla fine del for sulla stessa indentazione (spaziatura) del for si mette ciò che accade dopo il controllo
print(numero) # In questo caso alla fine del for scriverà il numero (che corrisponde al numero di variabili in lista)


# -- Def / Async Def

# In python esistono la funzione def (define) e la funzione async def 
# La differenza è che il def esegue una task alla volta (rende la esecuzione più lenta) mentre L'async def permette di fare più task allo stesso momento
# Il def si usa spesso per semplificare la creazione di codici che ripetono spesso la stessa funzione più e più volte
# Ma viene anche usata per creare le librerie

def def1(): # Dopo aver scritto "def" diamo un nome alla funzione 

    print("Ciaoooo") # Dentro la funzione scriviamo tutto ciò che vogliamo che venga eseguito

def1() # Per far partire la funzione la si deve chiamare in questo modo

# Variabili: Se vogliamo aggiungere una variabile che cambia a seconda della nostra esigienza nel codice la dobbiamo dichiarare nelle parentesi

def def2(var7:int, var8:str): # int se la variabile deve essere solo un intero, str se la variabile deve essere solo una stringa

    print(f"Questa è una variabile intera {var7}")

    print(f"Questa è una variabile stringa {var8}")


def2(var7=1, var8="ciaooo") # Quando chiamiamo la funzione nelle parentesi scriviamo la variabile + i campi richiesti


# Nel caso dobbiamo aggiungere una variabile non obligatoria bisogna aggiungere =None


def def3(var9, var10=None): 

    print(var9)

    if var10 is not None: # Nel caso la variabile è diversa da None la scrive, se è None la ignora e finisce il ciclo

        print("Variabile 10 :" + var10)

    else:

        pass # Pass si usa per quando non bisogna specificare azioni da eseguire sotto una funzione


import asyncio # Per usare gli async def è importante saper usare la libreria asyncio


async def asyncdef1():

    print("Sto facendo multitasking...")

    await asyncio.sleep(10) # Aspetta dieci secondi senza bloccare tutto 

    print("Ho finito :)")

    # Per chiamare il modulo che aspetta bisognia usare "await", nonostante non ci servira molto è bene menzionarlo


# -- Class


# Cosa sono: Le classi sono molto simili ai def tuttavia le classi a differenza dei def possono contenere piu informazioni che possono essere chiamate separatamente

class class1():

    VarClass1_1 = "ciao" # Cosi stai definendo una variabile stringa
    VarClass1_2 = 1234 

    def def4(): # Nelle classi puoi creare def per eseguire informazioni inerenti alla classe (Esempio: la classe può essere usata per rappresentare il teorema di pitagora, tiene tutte le informazioni sui triangoli, il def serve per creare la funzione che calcola la lunghezza dell'ipotenusa)

        print("ciaoooo")

print(class1.VarClass1_2) # Cosi printa la seconda variabile della classe
print(class1.VarClass1_1) # Cosi printa la prima variabile della classe
print(class1.def4()) # Cosi esegue il def presente nella classe


# -- Try


# Cosa è: Il try è una funzione che viene usata per fare dei test al codice per fare sistemi di rilevo errori
# Il try è una funzione che "verifica" il codice prima di runnarlo, se trova errori possiamo dargli una risposta anticipata in modo da non far crishare il programma


try:

    pint() # Nel caso io commetto un errore (adesso ovvio) il codice me lo riportera

except Exception as error: # Qui abbiamo definito come singola variabile TUTTI gli errori

    print(error) # Qui abbiamo detto al software che nel caso trova un errore lo scrive


# Volendo per rendere più preciso il sistema di errori si può specificare a quale errore il software deve rispondere


try:

    pint() # Nel caso io commetto un errore (adesso ovvio) il codice me lo riportera

except TypeError: # Qui abbiamo detto al software che se trova un type error (errore di scritture) scrive un messaggio personalizzato

    print("Hai sbagliato a scrivere")

except TabError: # Gli errori si possono mettere un sopra l'altro per creare sistemi di gestione errori più precisi

    print("Tab error")


# -- While True:


# Cosa è: Il while True: è un loop, in sostanza stai dicendo al software di ripetere un azione fino a quando non viene fermato 


while True:

    var9 = input("Scrivi 'stop' per far scrivere una sola volta")
    var9.upper()

    if var9 == "STOP": 

        print("Questo messaggio verra scritto all infinito")
        break 

    else:

        print("Questo messaggio verra scritto all infinito")

# -- Import 


# Cosa sono: L'import è una funzione che viene utilizzata per selezionare quali librerie usare
# Librerie: Una libreria è un file python (.py) che contiene delle funzioni (def) o (class) che servono a semplificare la programmazione
# Come abilitarle: Per abilitare una libreria ti basta digitare "import nome_libreria"
# Importante: Non tutte le librerie sono gia installate nel tuo pc per installarne altre apri il cmd (prompt dei comandi) della cartella dove si trova il file pyton e digita "pip install nome_libreria"

# Librerie importanti da conoscere

import time # Libreria che ti permette di far fermare il codice per fare una cosa alla volta
import asyncio # Libreria che ti permette di fare più cose mentre aspetta
import string # Libreria che aggiunge funzioni utili per le stringe (str)
import math # Libreria sulla matematica
import random # Libreria che ti permette di estrarre cose casuali
import colorama # Libreria che ti permette di scrivere a colori
import tkinter # Libreria usata per le ui
import sys # Libreria usata per ricevere informazioni sul programma che si sta runnando o sul pc


# Per abilitare alcune funzioni di una libreria devi fare:


from colorama import Fore, Style, init # Questo perchè in alcune librerie le funzioni non sono tutte inportate di default 
from colorama import * # Questo ti permette di importare TUTTE le funzioni fa una libreria


# -- Time


print("ciao tra 5 secondi ti diro addio")
time.sleep(5) # Aspetta 5 secondi e scrive addio
print("addio")
 

# -- string


def contiene_solo_lettere(testo):
  
    for carattere in testo:

        if carattere not in string.ascii_letters: # Se il carattere non è nella lista delle lettere ASCII (caratteri printabili) dice che l'input contiene un carattere non ammesso
            return False
    
    return True # Nel caso tutti i caratteri siano ammessi ritorna il valore True

parola1 = "Ciao"
parola2 = "Ciao123"

print(f"'{parola1}' contiene solo lettere? {contiene_solo_lettere(parola1)}")
print(f"'{parola2}' contiene solo lettere? {contiene_solo_lettere(parola2)}")

# -- Math

def calcola_area_cerchio(raggio):

    area = math.pi * (raggio ** 2) # Chiamiamo la funzione math.pi e gli diamo tutti i campi richiesti
    return area # Si usa per far ritornare il valore alla funzioe che lo ha chiamato

raggio_cerchio = 5
area = calcola_area_cerchio(raggio_cerchio)

print(f"L'area di un cerchio con raggio {raggio_cerchio} è: {area}")


# -- Random


def dici_parola_random():

    lista = ["cia", "bella", "come stai?", "oggi usciamo?"]

    choice = random.choice(lista) # Chiamiamo il modulo random.choice e gli diamo la lista come punto di riferimento
    return choice

scelta_finale = dici_parola_random()

print(f"La parola selezionata è {scelta_finale}")


# -- colorama

init() # Serve per far si che windows faccia vedere i colori nel terminale di avvio del codice

print(Fore.GREEN + "Questo testo è verde") # Chiamiamo la funzione Fore e selezioniamo il colore che più ci preferisce tra quelli gli esistenti o mettiamo il codice html del colore
print(Fore.RED + "Questo testo è rosso")


# -- Sys

# Questa libreria puo essere utilizzata per fai chiudere il programma dopo un esecuzione

inputa = input("A per chiudere B per far scrivere ciao")

inputa.upper()

if inputa == "A":

    sys.exit() # Chiude il software

elif inputa == "B":

    print("ciaooooo tra 5 secondi chiudo il software")
    time.sleep(5)
    sys.exit()

else:

    sys.exit()


# -- Consigli


# 1) leggi la documentazione di python e delle librerie che usi (per trovarle cerca su google "nome_libreria docs") SARANNO IN INGLESE
# 2) Crea un account di github.com, è un sito web dove molti developers mettono codici gratuiti che puoi usare per espandere la tua conoscenza
# 3) Prendi codici gia fatti smontali e cerca di capire come funzionano per replicarli
# 4) Fai progetti / giochini con amici per divertirti ma anche per imparare


# - Crediti


# Gentilmente offerto da Fiocco Riccardo :)


# -- Fine