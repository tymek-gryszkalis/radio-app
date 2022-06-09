from pylatex import Document, Section, Subsection, Tabular
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os

def getInput():
    heads = []
    news = []
    author = ""
    hour = ""
    pronouns = ""
    for i in range(3):
        print("Podaj nagłówek nr " + str(i + 1) + ": ")
        heads.append(input())
    for i in range(3):
        print("Podaj newsa nr " + str(i + 1) + ": ")
        news.append(input())
    print("Podaj autora: ")
    author = input()
    print("Podaj godzinę: ")
    hour = input()
    print("Podaj zaimek")
    pronouns = input()
    main_hash = {"headers" : heads, "news" : news, "author" : author, "time" : hour, "pronouns" : pronouns}

def genPdf(main_hash):
    pn = ""
    if main_hash["pronouns"] == "f":
        pn = "a"
    elif main_hash["pronouns"] == "o":
        pn = "x"

    intro = "Minęła godzina " + main_hash["time"] + " więc czas na wiadomości studenckie, a w nich:\n\n"
    outro = "\nA wiadomości przygotował" + pn + " " + main_hash["author"] + "."

    if __name__ == '__main__':
        geometry = {"tmargin" : "1cm", "lmargin" : "1cm", "bmargin" : "1cm", "rmargin" : "1cm"}
        doc = Document(geometry_options = geometry)

        doc.append(intro)
        for i in range(len(main_hash["headers"])):
            doc.append(main_hash["headers"][i] + "\n")
        doc.append("\nWiadomości przedstawi:\n\n")
        for i in range(len(main_hash["news"])):
            doc.append(main_hash["news"][i] + "\n")
        doc.append(outro)

        doc.generate_pdf('full', clean_tex=False)

testhash = {
    "headers" : ["header a", "header b", "header c"],
    "news" : ["news one abcdefghijklmnopqrstuvwxyz", "news two abcdefghijklmnopqrstuvwxyz", "news three abcdefghijklmnopqrstuvwxyz"],
    "author" : "Tymi Gryszkalis",
    "time" : "19:30",
    "pronouns" : "m"
}

genPdf(testhash)