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
        arp_istek_paketi=scapy.ARP(pdst=ip) #paket oluşturduk.
        

        arp_yayinlayici=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#bütün iplere default olarak bu mac adresini gönderdik.
        

        paket_birlestirici=arp_yayinlayici/arp_istek_paketi

        (cevap_gelen_liste,cevap_gelmeyen_liste)=scapy.srp(paket_birlestirici,timeout=1)
        cevap_gelen_liste.summary()

kullanici_ipsi = kullanicidan() #Kullanıcıdan tarama yapmak istediğimiz ip aralığını (10.0.2.0/24) aldık ve ag tarayici fonksiyonumuza gönderdik.  

ag_tarayici(kullanici_ipsi)

