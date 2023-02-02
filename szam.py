import random

def vel_szam_generator(kezdoszam, vegszam):
    vel = random.randint(kezdoszam,vegszam)
    print(f"I/A:\n\tA generált szám: {vel}")
    return vel

def szam_oszathato_e_harommal_vagy_ottel(szam):
    if szam % 5 == 0 and szam % 3 == 0:
        kimenet = "A szám öttel és hárommal is osztható!"
    elif szam % 5 == 0:
        kimenet = "A szám öttel osztható!"
    elif szam % 3 == 0:
        kimenet = "A szám hárommal  osztható!"
    else:
        kimenet = "A szám egyikkel sem osztható..."

    print(f"I/B:\n\t{kimenet}")