from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Yeni font dosyasının yolu {yourUserName} kısmına kendi kullanıcı adınızı yazınız.
font_path = r"C:\Users\{yourUserName}\Desktop\fonts\CaviarDreams_Bold.ttf"


def create_pdf(create_pages):
    # Yeni fontu kaydet
    pdfmetrics.registerFont(TTFont("CaviarDreamsBold", font_path))

    for page_content in create_pages:
        # PDF dosyasını oluştur
        c = canvas.Canvas(f"{page_content}.pdf", pagesize=A4)

        # Sayfanın orta noktasını al
        width, height = letter
        middle_x = width / 2
        middle_y = height / 1.25

        # Yazının boyutunu ve fontunu ayarla
        font_name = "CaviarDreamsBold"  # Artık "CaviarDreamsBold" kullanıyoruz
        font_size = 18
        text = page_content

        # Yazıyı sayfanın ortasına yerleştir
        c.setFont(font_name, font_size)
        c.drawCentredString(middle_x, middle_y, text)

        # PDF'i kaydet
        c.save()


if __name__ == "__main__":
    create_pages = [
        "1.Aşama Hesapları",
        "Deprem Hesapları",
        "Orta Ayak Hesapları",
        "P1 Aksı Başlık Kirişi Hesapları",
        "Orta Ayak Kolon Tesirleri",
        "Orta Ayak Kesit Tahkikleri",
        "Bağlantı Plağı Hesapları",
        "Orta Ayak Temel Hesapları",
        "Orta Ayak Temel Yükleri",
        "Orta Ayak Temel Kesit Tahkikleri",
        "Orta Ayak P1 Aksı Temel Kesit Tahkikleri",
        "Orta Ayak Kazık Hesapları",
        "Orta Ayak Kazık Servis Yükleri",
        "Orta Ayak Deprem TakozuMesnetKaidesiveSabitEnlemeHesabı",
        "Kenar Ayak Hesapları",
        "A1 - A2 Kenar Ayak Hesapları",
    ]
    create_pdf(create_pages)
