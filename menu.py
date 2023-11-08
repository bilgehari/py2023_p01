def menu():
    print("Menü:")
    print("1- PDF Dosya İçerik (Başlıklar) Oku")
    print("2- PDF (Başlıkları) Kaydet")
    print("3- Çıkış Yap")


def extract_titles_from_pdf(pdf_path):
    titles = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            titles.extend(text.split('\n'))

    return titles


def save_titles_to_pdf(titles):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=1, margin=15)
    pdf.set_font("Arial", size=12)