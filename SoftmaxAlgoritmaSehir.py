# -*- coding: utf-8 -*-
"""

import numpy as np
import folium

# Mahalleler ve kriterler
mahalleler = ["Cumhuriyet Mahallesi", "İstasyon Mahallesi", "Bağdemlik Mahallesi"]
kriterler = ["Nüfus Yoğunluğu", "Ulaşım Altyapısı", "Maliyet Analizi", "Çevresel Etki", "Sosyal Fayda"]

# Kriter değerleri
veriler = np.array([
    [80, 70, 60, 50, 90],  # Cumhuriyet Mahallesi
    [60, 85, 75, 65, 80],  # İstasyon Mahallesi
    [90, 60, 50, 70, 60],  # Bağdemlik Mahallesi
])

# Softmax fonksiyonu
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Numerik stabilite için
    return exp_x / np.sum(exp_x, axis=0)

# Kriter ağırlıkları
kriter_agirliklari = np.array([0.3, 0.2, 0.2, 0.15, 0.15])

# Softmax ile normalizasyon
normalize_veriler = softmax(veriler)

# Ağırlıklı puan hesaplama
agirlikli_puanlar = np.sum(normalize_veriler * kriter_agirliklari, axis=1)

# Sonuçlar
for i, mahalle in enumerate(mahalleler):
    print(f"{mahalle} Toplam Puan: {agirlikli_puanlar[i]:.2f}")

# En uygun güzergah
en_uygun_mahalle = mahalleler[np.argmax(agirlikli_puanlar)]
print(f"\nEn uygun güzergah: {en_uygun_mahalle}")

# Kırklareli koordinatları
kirklareli_merkez = [41.7358, 27.2243]

# Mahallelerin koordinatları
mahalle_koordinatlari = {
    "Cumhuriyet Mahallesi": [41.7400, 27.2300],  # Örnek koordinat
    "İstasyon Mahallesi": [41.7300, 27.2200],    # Örnek koordinat
    "Bağdemlik Mahallesi": [41.7250, 27.2100],  # Örnek koordinat
}

# Harita oluşturma
harita = folium.Map(location=kirklareli_merkez, zoom_start=14)

# Mahalleleri haritaya ekleme
for mahalle, koordinat in mahalle_koordinatlari.items():
    folium.Marker(
        location=koordinat,
        popup=f"{mahalle}\nPuan: {agirlikli_puanlar[mahalleler.index(mahalle)]:.2f}",
        icon=folium.Icon(color="green" if mahalle == en_uygun_mahalle else "blue")
    ).add_to(harita)

# En uygun güzergahı çizme
guzergah_noktalari = [
    mahalle_koordinatlari["Cumhuriyet Mahallesi"],
    mahalle_koordinatlari["İstasyon Mahallesi"],
    mahalle_koordinatlari["Bağdemlik Mahallesi"],
]
folium.PolyLine(guzergah_noktalari, color="red", weight=2.5, opacity=1).add_to(harita)

# Haritayı kaydetme
harita.save("kirklareli_toplu_tasima_hatti.html")

print("\nHarita 'kirklareli_toplu_tasima_hatti.html' olarak kaydedildi. Tarayıcıdan açabilirsiniz.")
