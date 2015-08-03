# -*- coding: utf-8 -*-
# Importation des bibliothèques
import matplotlib.pyplot as plt
import numpy as np

# Charger fichier renvoie liste des lignes du fichier
def ChargerFichier(nomFichier):
    lu=[]
    f = open(nomFichier, 'r')
    for line in f:
        lu.append(line)
    f.close()
    return lu

# Supression commentaires et conversion en nombres
def EraseNotes(liste):
    s=[]
    for ligne in liste:
        if ligne[0]!='#':
            s.append(map(float,ligne.split()))
    return s

# GetTime
def GetTime(liste):
    s=[]
    for ligne in liste:
        s.append(ligne[0])
    return s

# GetStress
def GetStress(liste,coeff=1):
    s=[]
    for ligne in liste:
        s.append(ligne[1]*coeff)
    return s

# GetStrain
def GetStrain(liste):
    s=[]
    for ligne in liste:
        s.append(ligne[2])
    return s
# GetInfo
def GetInfo(liste):
    return GetTime(liste), GetStress(liste,10**(-6)), GetStrain(liste)

# Lecture du fichier TCD
def LireFichierTCD(nomFichier):
    t,s,S = GetInfo(EraseNotes(ChargerFichier(nomFichier)))
    return t,s,S

# Tracer les graphe des données du fichier TCD
def TracerTCD(data, name=None):
    Time=data[0]
    Stress=data[1]
    Strain=data[2]
    if name==None:
        plt.figure()
        plt.subplot(211)
        plt.subplots_adjust(hspace=0.5)
        plt.title("Stress, strain versus time")
        plt.grid(True)
        plt.xlabel('Time [s]')
        plt.ylabel('Stress [MPa]', color ='b')
        plt.xlim(0.,2.3)
        plt.ylim(0.,50)
        plt.plot(Time,Stress,'x-b')
        
        plt.twinx()
        plt.ylim(0.,10.e-3)
        plt.xlim(0.,2.3)
        plt.ylabel('strain',color='r')
        plt.plot(Time,Strain,'x-r')
        
        # Graphe stress versus strain
        plt.subplot(212)
        plt.title("Stress vs. strain", color='g')
        plt.grid(True)
        plt.xlabel('Strain')
        plt.ylabel('Stress [MPa]', color ='b')
        plt.xlim(0.,6.e-3)
        plt.ylim(0.,50)
        plt.plot(Strain,Stress,'x-b')
        
        plt.show()
    else:
        plt.figure()
        plt.subplot(211)
        plt.subplots_adjust(hspace=0.5)
        plt.title("Stress, strain versus time")
        plt.grid(True)
        plt.xlabel('Time [s]')
        plt.ylabel('Stress [MPa]', color ='b')
        plt.xlim(0.,2.3)
        plt.ylim(0.,50)
        plt.plot(Time,Stress,'x-b')
        
        plt.twinx()
        plt.ylim(0.,10.e-3)
        plt.xlim(0.,2.3)
        plt.ylabel('strain',color='r')
        plt.plot(Time,Strain,'x-r')
        
        # Graphe stress versus strain
        plt.subplot(212)
        plt.title("Stress vs. strain", color='g')
        plt.grid(True)
        plt.xlabel('Strain')
        plt.ylabel('Stress [MPa]', color ='b')
        plt.xlim(0.,6.e-3)
        plt.ylim(0.,50)
        plt.plot(Strain,Stress,'x-b')
        
        plt.savefig(name)

# Main
if __name__ == '__main__':
    dataFile="data001.txt"
    #
    # Lecture du fichier ligne par ligne
    #
    
    
    TracerTCD(LireFichierTCD(dataFile))

