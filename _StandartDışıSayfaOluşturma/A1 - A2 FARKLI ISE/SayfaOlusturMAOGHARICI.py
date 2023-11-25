# RapportLab kütüphanesinden gerekli modülleri içe aktarıyoruz
from reportlab.lib.pagesizes import A4  # A4 sayfa boyutunu ekliyoruz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Yeni font dosyasının yolu
font_path = r"C:\Users\PC\Desktop\ÇALIŞMA DOSYALARI\CaviarDreams_Bold.ttf"

# PDF oluşturacak fonksiyonu tanımlıyoruz


def create_pdf(create_pages):
    # Yeni fontu kaydediyoruz
    pdfmetrics.registerFont(TTFont('CaviarDreamsBold', font_path))

    # Her sayfa içeriği için döngü oluşturuyoruz
    for idx, page_content in enumerate(create_pages):
        # PDF dosyasını oluşturuyoruz
        pdf_name = f"0{idx + 1} - {page_content}.pdf"
        # A4 sayfa boyutunu kullanıyoruz
        c = canvas.Canvas(pdf_name, pagesize=A4)

        # Sayfanın orta noktasını alıyoruz
        width, height = A4
        middle_x = width / 2
        middle_y = height / 2

        # Yazının boyutunu ve fontunu ayarlıyoruz
        font_name = "CaviarDreamsBold"  # Artık "CaviarDreamsBold" kullanıyoruz
        font_size = 18
        text = page_content

        # Yazıyı sayfanın ortasına yerleştiriyoruz
        c.setFont(font_name, font_size)
        c.drawCentredString(middle_x, middle_y, text)

        # PDF'i kaydediyoruz
        c.save()


# Ana program başlangıcı
if __name__ == "__main__":
    # Oluşturulacak sayfaların içeriğini belirliyoruz
    create_pages = ["Alt Yapi Hesapları", "Deprem Hesabı", "A1 Kenar Ayak Hesapları", "A2 Kenar Ayak Hesapları", "Orta Ayak Hesapları", "Orta Ayak Temel Hesapları",
                    "P1 Aksı Orta Ayak Temel Hesapları", "Kenar Ayak Hesapları", "A1 Kenar Ayak Hesapları", "A2 Kenar Ayak Hesapları",
                    "Döşeme Hesapları", "Başlık Kirişi Kesit Tesirleri"]

    # PDF oluşturma fonksiyonunu çağırıyoruz
    create_pdf(create_pages)


# import ifadeleri: Gerekli kütüphane ve modülleri içeri aktarıyoruz.

# font_path: Kullanılacak özel fontun dosya yolu.

# create_pdf fonksiyonu: PDF dosyalarını oluşturmak için kullanılacak fonksiyon. Parametre olarak bir sayfa içeriği listesi alır.

# pdfmetrics.registerFont: Yeni fontu kaydetmek için kullanılır.

# for döngüsü: Her sayfa içeriği için döngü oluşturulur.

# canvas.Canvas(pdf_name, pagesize=letter): PDF dosyasını oluşturmak için bir canvas nesnesi oluşturulur.

# width, height = letter: Sayfanın genişlik ve yüksekliği alınır.

# middle_x, middle_y: Sayfanın orta noktasını bulmak için kullanılır.

# font_name, font_size, text: Yazının boyutu, fontu ve içeriği belirlenir.

# c.setFont(font_name, font_size): Yazı fontu ve boyutu ayarlanır.

# c.drawCentredString(middle_x, middle_y, text): Yazıyı sayfanın ortasına yerleştirir.

# c.save(): PDF dosyasını kaydeder.

# if name == "main":: Programın ana başlangıç noktası.

# create_pages: Oluşturulacak sayfaların içeriğini belirten liste.

# create_pdf(create_pages): PDF oluşturma fonksiyonunu çağırır ve belirtilen sayfaları içeren PDF dosyalarını oluşturur.
