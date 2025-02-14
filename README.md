#  Softmax Algoritması ile İdeal Ulaşım Hesaplama  

##  Kırklareli Toplu Taşıma Hattı Planlaması  

Bu proje, **Kırklareli'nin Cumhuriyet Mahallesi, İstasyon Mahallesi ve Bağdemlik Mahallesi** için toplu taşıma hattı planlamasını yapmak amacıyla geliştirilmiştir.  
Proje, **Softmax algoritması** kullanarak kriter tabanlı bir değerlendirme yapar ve en uygun güzergahı belirler. Ayrıca, **Folium** kütüphanesi ile harita üzerinde güzergah görselleştirilir.  

---

##  Proje Açıklaması  
### Proje, aşağıdaki adımlardan oluşmaktadır:  
1. **Kriterlerin Belirlenmesi**: Her mahalle için nüfus yoğunluğu, ulaşım altyapısı, maliyet analizi, çevresel etki ve sosyal fayda kriterleri değerlendirilir.  
2. **Softmax Algoritması**: Kriterlerin ağırlıkları Softmax algoritması ile hesaplanır.  
3. **Maliyet-Fayda Analizi**: Her mahalle için toplam puan hesaplanır ve en uygun güzergah belirlenir.  
4. **Harita Görselleştirmesi**: **Folium** kütüphanesi ile mahalleler ve güzergah harita üzerinde işaretlenir.  

---

##  Kullanılan Teknolojiler  
- **Python**: Programlama dili  
- **NumPy**: Matematiksel hesaplamalar  
- **Folium**: Harita görselleştirmesi  

---

##  Kullanım  
Projeyi yerel makinenizde çalıştırmak için şu adımları izleyin:  

### 1. Python'u Yükleyin  
Python’u [python.org](https://www.python.org) adresinden indirip yükleyin.  

### 2. Gerekli Kütüphaneleri Yükleyin  
Terminal veya komut istemcisinde aşağıdaki komutları çalıştırın:  
```bash
pip install numpy folium
