#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:25:33 2022

@author: solveig
"""

#importerer biblioteker
import csv
import matplotlib.pyplot as plt
import numpy as np

#lager tomme lister som senere skal fylles
atomMasse = []
navn = []
symbol = []
elektronegativitet = []
atomRadius = []
atomNummer = []


#åpner csv fila for lesing med utf8
with open("kjemi.csv", "r", encoding="utf-8-sig") as f:
    
    #henter ut innhold delt av kolon
    innhold = csv.reader(f, delimiter=",")
    
    overskrift = next(innhold)
    
    #for hver rad i fila skal det kegges til info i listene
    for rad in innhold:
        atomMasse.append(float(rad[3]))
        atomRadius.append(None if rad[16] == "" else float(rad[16]))
        navn.append(str(rad[1]))
        atomNummer.append(int(rad[0]))
        symbol.append(str(rad[2]))
        elektronegativitet.append(None if rad[17]=="" else float(rad[17])) #inline if-test fordi jeg slet med at det var mange hull i datasettet
        
        

        








#funksjon som finner symboler fra input, deler opp og legger til i en liste
# inn CaSO4
# ut [Ca,S,O,4]    
def finn_symboler(x):
    symboler = []
    
    #for hvert av tegnene i x
    for i in x:
        
        #Hvis c er en liten bokstav
        if i.islower() == True:
            
            #Erstatter siste element i lista med siste element + c
            symboler[-1] += i
        
        #Hvis c er et tall og siste element i lista symboler er et tall
        elif i.isnumeric() == True and symboler[-1].isnumeric() == True:
            
            #Erstatter siste element i lista med siste element + c
            symboler[-1] += i
        
        else:
            #legger til c i lista symboler
            symboler.append(i)
            
    
    return symboler

#funksjon som bruker funksjonen finn_symboler(), finner alle grunnstoffer og legger de etter hverandre i en liste
# inn [Ca,S,O,4]
# ut [Ca,S,O,O,O,O]    
def finn_grunnstoffer(x):
    symboler = finn_symboler(x)
    grunnstoffer = []
    
    #for hvert element i lista
    for s in symboler:
        
        #hvis elementet er et tall, legger til forrige element ganger tallet-1
        if s.isnumeric() == True:
            a = grunnstoffer[-1]
            n = int(s)
            for i in range(n-1):
                grunnstoffer.append(a)
        
        else:
            grunnstoffer.append(s)
            
    return grunnstoffer





    
#Lager en klasse  
class Grunnstoffer:
    """
    Parametere:
        navn(str) = Grunnstoffets navn
        symbol(str) = Grunnstoffets symbol
        atmMasse(float) = massen til atomene i u
        elektronegativitet(float) = elektronegativiteten til grunnstoffene
        
    """
    
    
    def __init__(self, navn, symbol, atomMasse, elektronegativitet):
        self.navn = navn
        self.symbol = symbol
        self.atomMasse = atomMasse
        self.elektronegativitet = elektronegativitet
     
    #en metode i klassen
    def visInfo(self):
        
        #Printer infoen i en string
        print(self.navn, 'har symbol', self.symbol, 'molarmasse', self.atomMasse, 'og elektronegativiteten', self.elektronegativitet)
        

        
        
#Lager en tom dictionary
grunnstoffer = {}

#legger til objekter i dictionaryen
for i in range(len(atomMasse)):
    grunnstoffer[symbol[i]] = Grunnstoffer(navn[i], symbol[i], atomMasse[i], elektronegativitet[i])






#Funksjon som finner molar masse
def molarMasse(glist):
    Mmasse = 0
    
    #for hvert av elementene i grunnstoff-lista hentes atommassen ut og og 
    #legges sammen med de andre atommassene for å få den molare massen
    for g in glist:
        Mmasse = Mmasse + grunnstoffer[g].atomMasse
        
    return Mmasse



#funksjon som regner ut konsentrasjonen ved å ta inn den molare massen, massen i gram, og volumet i L
def regn_ut_konsentrasjon(m, V, Mm):
    
    #formelen for konsentrasjon
    c = (Mm/m)/V 
    return c


    
#Definerer funksjonen plotElektroN
def plotElektronegativitet():
    
    #En liste med anntall atomer per periode i periodesystemet
    perioder =[2,8,8,18,18,32,32]
    
    #setter startpunktet der periodene starter til 0
    startpkt = [0]
    
    for p in perioder:
        startpkt.append(startpkt[-1]+p)
     
    #lager et subplot med to plot
    fig, (plot1, plot2) = plt.subplots(2,1,figsize=(8,12)) #skriv 1, 2 inne i parentesen for å få plottene ved siden av hverandre
    
    #tittel til subplottet
    fig.suptitle('Elektronegativitet i perioder i periodesystemet')
    serier=[] #Tom liste
    for i in range(len(perioder)):
        e = np.array(elektronegativitet[startpkt[i]:startpkt[i+1]])
        x2 = np.linspace(0,1,perioder[i])
        
        #Legger til string i den tomme lista serier
        serier.append(f"Atomnr. fra {startpkt[i]} til {startpkt[i+1]}")
        
        plot2.plot(x2,e,'-o')
        plt.legend(serier)
        
        x1 = np.array(atomNummer[startpkt[i]:startpkt[i+1]])
        plot1.plot(x1,e, '-o', markersize=3)
    
    #setter egne aksetitler for hvert av de to plottene    
    plot2.set_xlabel('Fra høyre til venstre i periodesystemet')
    plot2.set_ylabel('Elektronegativitet')
    plot1.set_xlabel('Atomnummer')
    plot1.set_ylabel('Elektronegativitet')
    
    plt.show() #viser grafene
    
  
          

plt.plot(atomNummer, atomRadius,'-o', markersize = 3) # I periodesystemet avtar atomradius mot høyre og øker nedover i hver gruppe
plt.xlabel('Atomnummer') #Navn på x-akse 
plt.ylabel('Atomradius') #Navn på y-akse
plt.show() #viser grafen


#Kaller funksjon som plotter elektronegativitet
plotElektronegativitet() #elektronegativiteten øker mot høyre i periodesystemet, og avtar nedover
    
    
# ber om et stoff fta bruker
stoff = input('skriv inn molekylet du vil finne den molare massen og konsentrasjonen av ')  


Mm = molarMasse(finn_grunnstoffer(stoff))

print(f'Den molare massen av {stoff} er {Mm} g/mol')

# Ber bruker skrive inn volumet av stoffet i liter
volum = float(input('Hva er volumet av stoffet i L? ')) 

# Ber bruker skrive inn massen til stoffet i gram
masse = float(input('Hvor mange gram har du av stoffet? ')) 


c = regn_ut_konsentrasjon(masse, volum, Mm) # Bruker funksjonen regn_ut_Konsentrasjon til å finne konsentrasjonen

print(f'Konstentrasjonen av {stoff} er {c} mol/L')


info_symbol = input('Vil du ha litt info om et grunnstoff? skriv inn et symbol ')
print(grunnstoffer[info_symbol].visInfo())

        
    

