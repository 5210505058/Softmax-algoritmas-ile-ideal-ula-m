# Softmax algoritmas ile ideal ulasım hesaplama

## Kırklareli Toplu Taşıma Hattı Planlaması

Bu proje, Kırklareli'nin Cumhuriyet Mahallesi, İstasyon Mahallesi ve Bağdemlik Mahallesi için toplu taşıma hattı planlamasını yapmak amacıyla geliştirilmiştir. Proje, Softmax algoritması kullanılarak kriter tabanlı bir değerlendirme yapar ve en uygun güzergahı belirler. Ayrıca, folium kütüphanesi kullanılarak harita üzerinde görselleştirme sağlanır.

##Proje Açıklaması

Proje, aşağıdaki adımları içerir:

Kriterlerin Belirlenmesi: Her mahalle için nüfus yoğunluğu, ulaşım altyapısı, maliyet analizi, çevresel etki ve sosyal fayda kriterleri değerlendirilir.

Softmax Algoritması: Kriterlerin ağırlıkları Softmax algoritması ile hesaplanır.

Maliyet-Fayda Analizi: Her mahalle için toplam puan hesaplanır ve en uygun güzergah belirlenir.

Harita Görselleştirmesi: folium kütüphanesi kullanılarak mahalleler ve güzergah harita üzerinde işaretlenir.

## Kullanılan Teknolojiler

Python: Programlama dili olarak Python kullanılmıştır.

NumPy: Matematiksel hesaplamalar için NumPy kütüphanesi kullanılmıştır.

Folium: Harita görselleştirmesi için Folium kütüphanesi kullanılmıştır.

## Kullanım

Proje, aşağıdaki adımlarla çalışır:

Mahalleler ve Kriterler:

mahalleler listesinde mahalleler tanımlanmıştır.

veriler dizisinde her mahalle için kriter değerleri belirlenmiştir.

Softmax Algoritması:

Softmax fonksiyonu ile kriterlerin ağırlıkları hesaplanır.

Harita Görselleştirmesi:

folium kütüphanesi kullanılarak mahalleler harita üzerinde işaretlenir.

En uygun güzergah kırmızı çizgi ile gösterilir.

## Örnek Çıktı

Cumhuriyet Mahallesi Toplam Puan: 0.32
İstasyon Mahallesi Toplam Puan: 0.35
Bağdemlik Mahallesi Toplam Puan: 0.33

En uygun güzergah: İstasyon Mahallesi

## Harita Çıktısı

Harita Çıktısı:
kirklareli_toplu_tasima_hatti.html dosyası oluşturulur.

Harita üzerinde mahalleler ve güzergah görselleştirilir.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

Python'u Yükleyin:

Python'u python.org adresinden indirip yükleyin.

Gerekli Kütüphaneleri Yükleyin:

Terminal veya komut istemcisinde aşağıdaki komutları çalıştırın:

pip install numpy folium


Kodu Çalıştırın:

Proje dosyasını indirin ve terminalde aşağıdaki komutu çalıştırın:

python kirklareli_toplu_tasima.py


Haritayı Görüntüleyin:

Kod çalıştıktan sonra ''kirklareli_toplu_tasima_hatti.html'' dosyası oluşturulacaktır. Bu dosyayı tarayıcınızda açarak haritayı görüntüleyebilirsiniz.

