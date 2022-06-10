# By Tymek Gryszkalis 2022
# 
# Types:
# n - wiadomości studenckie
# c - kurier kulturalny
# s - wiadomości sportowe
# 
# Pronouns:
# m - male
# f - female
# o - other (x)
# 
# Pylatex version 1.4.1 

from pylatex import Document, PageStyle, Head, MiniPage, LargeText, LineBreak, Description, Command, NoEscape, Figure
from pylatex.utils import bold, italic
import os

# returns word ending based on picked pronouns
def pickPronouns(hash):
    pn = ""
    if hash["pronouns"] == "f":
        pn = "a"
    elif hash["pronouns"] == "o":
        pn = "x"
    return pn

# returns hash of strings with essential componenets for news generating
def pickElements(hash, type):
    pn = pickPronouns(hash)
    toret = {}
    if type == "n":
        toret["title"] = "Wiadomości studenckie " + hash["date"]
        toret["intro"] = "Minęła godzina " + hash["time"] + " więc czas na wiadomości studenckie, a w nich:"
        toret["outro"] = "Wiadomości przygotował" + pn + " " + hash["author"] + "."
        toret["filetit"] = "Wiadomości Studenckie"
    elif type == "s":
        toret["title"] = "Wiadomości sportowe " + hash["date"]
        toret["intro"] = ""
        toret["outro"] = "Wiadomości sportowe przygotował" + pn + " " + hash["author"] + "."
        toret["filetit"] = "Wiadomości Sportowe"
    elif type == "c":
        toret["title"] = "Kurier kulturalny " + hash["date"]
        toret["intro"] = ""
        toret["outro"] = "Kuriera kulturalnego przygotował" + pn + " " + hash["author"] + "."
        toret["filetit"] = "Kurier Kulturalny"
    return toret

# generates a 5 line break in document
def latexBigBreak(doc):
    doc.append(Command('phantom', 'bruh'))
    for i in range(5):
        doc.append(LineBreak())

# generating beginning of the document
def latexBegGen(title):
    # creating document
    geometry = {"margin" : "1in"}
    doc = Document(geometry_options = geometry)
    Command('documentclass', '10pt', 'doc')

    # creating header (for logo purposes only)
    with doc.create(Figure(position='h')) as logo:
        logo.add_image("./resources/logo.png", width = '50px', placement = "")

    # centralized minipage for title
    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold(title)))
    latexBigBreak(doc)
    return doc

# generating paragraphs of the document
def latexNewsGen(doc, hash):
    with doc.create(Description()) as desc:
        for i in range(len(hash["news"])):
            desc.add_item(str(i + 1) + ".", Command('texttt', (hash["news"][i])))

# generating news headers
def latexHeadersGen(doc, intro, hash):
    doc.append(italic(intro))
    doc.append("\n\n")
    for i in range(len(hash["headers"])):
        hd = hash["headers"][i].upper()
        doc.append(bold(str(i + 1) + ". " + hd + "\n"))
    doc.append(italic("\nWiadomości przedstawi: [Osoba]"))

# generating ending of the document
def latexEndingGen(doc, outro, hash, filetit):
    doc.append(italic(outro))
    dt = "" if hash["date"] == '' else hash["date"] + " - "
    doc.generate_pdf(dt + filetit, clean_tex=True)

# main pdf generator
def genPdf(main_hash):
    # prepare strings
    res = pickElements(main_hash, main_hash["type"])
    title = res["title"]
    intro = res["intro"]
    outro = res["outro"]
    filetit = res["filetit"]
    try:
        # main latex code generating
        doc = latexBegGen(title)
        if main_hash["type"] == "n":
            latexHeadersGen(doc, intro, main_hash)
        latexNewsGen(doc, main_hash)
        latexEndingGen(doc, outro, main_hash, filetit)
    except UnicodeDecodeError:
        return 0
    return 1

testhash = {
    "headers" : ["Nagłówek A", "Nagłówek B", "Nagłówek C"],
    "news" : [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sollicitudin mattis magna. In et luctus quam. Morbi scelerisque eu massa in sagittis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec porttitor felis. Mauris sit amet purus est. Curabitur augue sapien, mollis vel risus venenatis, egestas tristique urna. Vestibulum tristique sollicitudin mi ut luctus.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sollicitudin mattis magna. In et luctus quam. Morbi scelerisque eu massa in sagittis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec porttitor felis. Mauris sit amet purus est. Curabitur augue sapien, mollis vel risus venenatis, egestas tristique urna. Vestibulum tristique sollicitudin mi ut luctus.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sollicitudin mattis magna. In et luctus quam. Morbi scelerisque eu massa in sagittis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean nec porttitor felis. Mauris sit amet purus est. Curabitur augue sapien, mollis vel risus venenatis, egestas tristique urna. Vestibulum tristique sollicitudin mi ut luctus."],
    "author" : "Tymi Gryszkalis",
    "time" : "19:30",
    "pronouns" : "m",
    "date" : "04.20"
}