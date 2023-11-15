import os  # işletim sistemi etkileşimi için dizin yolları vs.
import pdfplumber  # PDF okumak için
from fpdf import FPDF  # PDF oluşturmak için.
import pdftitle
print(pdftitle.get_title_from_file(pdfler/bilgi2.pdf))


#Grid Sistemi
from tkinter import *

pencere = Tk()
pencere.title("Grid Uygulaması")

baslik = Label(pencere, text="Bilge Hari'nin Projesi")
etiket1 = Label(pencere, text="[ Birinci satır, birinci sütun ]")
etiket2 = Label(pencere, text="[ Birinci satır, ikinci sütun ]")
etiket3 = Label(pencere, text="[ İkinci satır, birinci sütun ]")
etiket4 = Label(pencere, text="[ İkinci satır, ikinci sütun ]")
buton1 = Button(pencere, text="<<< Oku >>>", fg="red", bg="green")
buton2 = Button(pencere, text="<<< Kaydet >>>", fg="black", bg="green")
buton3 = Button(pencere, text="<<< Çıkış >>>", fg="black", bg="red", command=pencere.quit)

baslik.grid(row=0, columnspan=2, padx=50, pady=25)
baslik.config(font=("Times New Roman", 30))
etiket1.grid(row=1, column=0, padx= 10, pady=20)
etiket2.grid(row=1, column=1, padx= 10, pady=20)
etiket3.grid(row=2, column=0, padx= 10, pady=20)
etiket4.grid(row=2, column=1, padx= 10, pady=20)
buton1.grid(row=3, column=0, padx=50, pady=10)
buton2.grid(row=3, column=1, padx=50, pady=10)
buton3.grid(row=4, columnspan=2, padx=5, pady=10)

pencere.mainloop()



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

    for title in titles:
        pdf.cell(200, 10, txt=title.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    pdf.output("newfile.pdf", 'F')

while True:
    menu()
    choice = input("Seçiminizi girin (1/2/3): ")

    if choice == "1":
        print("PDF Dosyalarını Oku seçildi:")
        pdf_folder = "pdfler"
        pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
        titles = []
        for pdf_file in pdf_files:
            titles.extend(extract_titles_from_pdf(pdf_file))
        for title in titles:
            print(title)
    elif choice == "2":
        print("PDF Dosyalarını Kaydet seçildi:")
        pdf_folder = "pdfler"
        pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
        titles = []
        for pdf_file in pdf_files:
            titles.extend(extract_titles_from_pdf(pdf_file))
        save_titles_to_pdf(titles)
        print("Başlıklar yeni PDF dosyasına kaydedildi: newfile.pdf")
    elif choice == "3":
        print("Çıkış Yapılıyor.")
        break
    else:
        print("Geçersiz seçenek! Lütfen 1, 2 veya 3 girin.")