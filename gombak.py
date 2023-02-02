from Gomba import *


def fajl_beolvas_es_eltarol():
    f = open("gombak_jav.txt", "r", encoding="utf-8")
    tartalom = f.readlines()
    f.close()

    gomba_lista = []

    i = 1
    while i < len(tartalom):
        sor = tartalom[i].strip().split("@")
        gomba_lista.append(Gomba(sor))
        i += 1

    return gomba_lista


def gombak_szama(gomba_lista):
    kimenet = len(gomba_lista)
    print(f"III/A, B\n\tA gombák száma: {kimenet}.")
    return kimenet


def papsapka(gomba_lista):
    i = 0
    while (not gomba_lista[i].nemzettseg == "papsapkagombák") and i < len(gomba_lista):
        i += 1

    print(f"III/C:\n\tAz első papsapkagomba neve: {gomba_lista[i].gomba_neve}")

def tinoru(gomba_lista):
    i = 0
    db = 0
    while i < len(gomba_lista):
        if gomba_lista[i].nemzettseg == "tinóru":
            db+=1
        i+=1
    print(f"III/D:\n\tA tinóru gombák száma: {db}.")