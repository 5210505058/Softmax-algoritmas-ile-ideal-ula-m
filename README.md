# Kırklareli Toplu Taşıma Hattı Planlaması

Bu proje, Kırklareli'nin **Cumhuriyet Mahallesi**, **İstasyon Mahallesi** ve **Bağdemlik Mahallesi** için toplu taşıma hattı planlamasını yapmak amacıyla geliştirilmiştir. Proje, Softmax algoritması kullanılarak kriter tabanlı bir değerlendirme yapar ve en uygun güzergahı belirler. Ayrıca, `folium` kütüphanesi kullanılarak harita üzerinde görselleştirme sağlanır.

---

## Proje Açıklaması

Proje, aşağıdaki adımları içerir:
1. **Kriterlerin Belirlenmesi**: Her mahalle için nüfus yoğunluğu, ulaşım altyapısı, maliyet analizi, çevresel etki ve sosyal fayda kriterleri değerlendirilir.
2. **Softmax Algoritması**: Kriterlerin ağırlıkları Softmax algoritması ile hesaplanır.
3. **Maliyet-Fayda Analizi**: Her mahalle için toplam puan hesaplanır ve en uygun güzergah belirlenir.
4. **Harita Görselleştirmesi**: `folium` kütüphanesi kullanılarak mahalleler ve güzergah harita üzerinde işaretlenir.

---

## Kullanılan Teknolojiler

- **Python**: Programlama dili olarak Python kullanılmıştır.
- **NumPy**: Matematiksel hesaplamalar için NumPy kütüphanesi kullanılmıştır.
- **Folium**: Harita görselleştirmesi için Folium kütüphanesi kullanılmıştır.

---

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. **Python'u Yükleyin**:
   - Python'u [python.org](https://www.python.org/) adresinden indirip yükleyin.

2. **Gerekli Kütüphaneleri Yükleyin**:
   - Terminal veya komut istemcisinde aşağıdaki komutları çalıştırın:
     ```bash
     pip install numpy folium
     ```

3. **Kodu Çalıştırın**:
   - Proje dosyasını indirin ve terminalde aşağıdaki komutu çalıştırın:
     ```bash
     python kirklareli_toplu_tasima.py
     ```

4. **Haritayı Görüntüleyin**:
   - Kod çalıştıktan sonra `kirklareli_toplu_tasima_hatti.html` dosyası oluşturulacaktır. Bu dosyayı tarayıcınızda açarak haritayı görüntüleyebilirsiniz.

---

## Kullanım

Proje, aşağıdaki adımlarla çalışır:

1. **Mahalleler ve Kriterler**:
   - `mahalleler` listesinde mahalleler tanımlanmıştır.
   - `veriler` dizisinde her mahalle için kriter değerleri belirlenmiştir.

2. **Softmax Algoritması**:
   - Softmax fonksiyonu ile kriterlerin ağırlıkları hesaplanır.

3. **Harita Görselleştirmesi**:
   - `folium` kütüphanesi kullanılarak mahalleler harita üzerinde işaretlenir.
   - En uygun güzergah kırmızı çizgi ile gösterilir.

---

## Örnek Çıktı

### Konsol Çıktısı:
```bash
Cumhuriyet Mahallesi Toplam Puan: 0.32
İstasyon Mahallesi Toplam Puan: 0.35
Bağdemlik Mahallesi Toplam Puan: 0.33

En uygun güzergah: İstasyon Mahallesi
```

### Harita Çıktısı:
- `kirklareli_toplu_tasima_hatti.html` dosyası oluşturulur.
- Harita üzerinde mahalleler ve güzergah görselleştirilir.

---



