import scapy.all as scapy #Ağ tarayıcıyı yapmamız için gerekli olan paket.
import optparse

'''Ağ tarayıcı yapma adımları: 
1-)Arp paketi oluştur
2-)OLuşturduğun paketi yayınla
3-)Cevapları al
 '''
def kullanicidan():

    parse_nesnesi=optparse.OptionParser()
    parse_nesnesi.add_option("-i","--ip",dest="kullanici_ip",help="Tarama yapmak istedeiğiniz ip adresinizi giriniz.")
    (kullanici_verisi,veri)=parse_nesnesi.parse_args()

    if not kullanici_verisi.kullanici_ip:
        print("İp adresi girmelisiniz.")

    ip=kullanici_verisi.kullanici_ip
    return ip

def ag_tarayici(ip):
        arp_istek_paketi=scapy.ARP(pdst=ip)
        #scapy.ls(scapy.ARP()) #scapy.ls yardım komutudur.Bu fonksiyonun içine yardım almak istediğiniz fonksiyonu girince ekrana yardımı basar.

        arp_yayinlayici=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#bütün iplere default olarak bu mac adresini gönderdik.
        #scapy.ls(scapy.Ether())

        paket_birlestirici=arp_yayinlayici/arp_istek_paketi

        (cevap_gelen_liste,cevap_gelmeyen_liste)=scapy.srp(paket_birlestirici,timeout=1)
        cevap_gelen_liste.summary() #summary özeti gösterir.

kullanici_ipsi = kullanicidan()

ag_tarayici(kullanici_ipsi)

