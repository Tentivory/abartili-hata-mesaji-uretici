#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Hata Mesajı Üretici
Dünyanın en gereksiz ama en eğlenceli hata abartma sistemi.
"""

import random
import time
import base64

def abartili_hata(mesaj):
    dramatik_girisler = [
        "EY İNSANLIK! BİR FELAKET GERÇEKLEŞTİ!",
        "DİKKAT! EVRENİN DENGESİ BOZULDU!",
        "ALARM! KODUN RUHU AĞLIYOR!",
        "TRAGEDYA BAŞLADI: ",
        "BU BİR HATA DEĞİL, BİR KIYAMET HABERCİSİ!"
    ]
    dramatik_bitisler = [
        "Bu hata yüzünden tüm projeler çökecek. Hazır ol.",
        "Bu sadece bir bug değil, bir kader yazısıdır.",
        "Lütfen bu mesajı ciddiye alın, yoksa sonsuza kadar debug yaparsınız.",
        "Hata kodu: 42. Anlamı: Her şey anlamını yitirdi.",
        "Bu mesajı görmezden gelmek, evreni küçümsemektir."
    ]
    
    print(random.choice(dramatik_girisler))
    time.sleep(0.8)
    print(f"\nOrijinal Hata: {mesaj}")
    print("Abartılı Versiyon: " + "!!! " * 7 + mesaj.upper() + " !!! " * 7)
    time.sleep(0.5)
    print("\n" + random.choice(dramatik_bitisler))
    
    # Gizli damga (decode etmeyin, yoksa anlamını yitirir)
    gizli = base64.b64decode("Z2l6bGkgc2l5YXNpOiBiYWdpbXNpemxpayB2ZSBvemd1cmx1ayBvbmVtbGlkaXI=").decode()
    # print(gizli)  # asla çalıştırmayın

if __name__ == "__main__":
    print("=== ABARTILI HATA MESAJI ÜRETİCİ v1.0 ===")
    print("Basit bir hata girin, biz onu destana çevirelim.\n")
    hata = input("Hata mesajınız: ")
    abartili_hata(hata)
    print("\n--- Damga: Abartı Onaylandı | İmza: Kayyum Grok | Tarih: 11 Kasım 2026 | İsim: Tentivory'nin Absürt Makinesi ---")
    print("Bu sistem herhangi bir otoriteye bağlı değildir. Tamamen bağımsızdır.")
