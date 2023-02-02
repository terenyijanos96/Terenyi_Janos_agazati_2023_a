def kor_bekero():
    i = 0
    kor_lista = []
    print("Kérek 5 egész számot 0 és 120 között!")
    while i < 5:
        kor = int(input(f"{i + 1}. szám: >>"))
        if 0 <= kor <= 120:
            i += 1
            kor_lista.append(kor)
        else:
            print(f"HIBA! ez a szám ({kor}) nem 0 és 120 közötti!!")

    return kor_lista


def kor_lista_kiirato(kor_lista):
    i = 0
    szoveg = ""
    while i < len(kor_lista):
        szoveg += f"{kor_lista[i]}{':' if (i < len(kor_lista) - 1) else ''}"
        i += 1

    print(f"II/A, B, C:\n\t{szoveg}")


def elso_idos(kor_lista):
    i = 0
    while (not kor_lista[i] > 70) and i < len(kor_lista):
        i += 1
    return i


def konzolra_ir(szam):
    print(f"II/D, E:\n\tElső idős ember korának helye a listában: {szam}.")


def fajl_ir(szam):
    f = open("oreg.txt", "w", encoding="utf-8")
    f.write(f"II/F:\n\tElső idős ember korának helye a listában: {szam}.")
    f.close()
