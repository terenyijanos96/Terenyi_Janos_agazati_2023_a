import szam
import korok
import gombak

vel_szam = szam.vel_szam_generator(1, 50)
szam.szam_oszathato_e_harommal_vagy_ottel(vel_szam)

kor_lista = korok.kor_bekero()
korok.kor_lista_kiirato(kor_lista)

elso = korok.elso_idos(kor_lista)

korok.konzolra_ir(elso)
korok.fajl_ir(elso)

gomba_lista = gombak.fajl_beolvas_es_eltarol()
gombak.gombak_szama(gomba_lista)

gombak.papsapka(gomba_lista)

gombak.tinoru(gomba_lista)