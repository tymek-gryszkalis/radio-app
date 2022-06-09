from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, Figure, LineBreak, Description, simple_page_number, Command
from pylatex.utils import bold, italic

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
    # pick right pronouns
    pn = ""
    if main_hash["pronouns"] == "f":
        pn = "a"
    elif main_hash["pronouns"] == "o":
        pn = "x"

    # prepare strings
    title = "Wiadomości studenckie " + main_hash["date"]
    intro = "Minęła godzina " + main_hash["time"] + " więc czas na wiadomości studenckie, a w nich:\n\n"
    outro = "\nA wiadomości przygotował" + pn + " " + main_hash["author"] + "."

    # main latex code generating
    if __name__ == '__main__':
        # creating document
        geometry = {"margin" : "1in"}
        doc = Document(geometry_options = geometry)
        Command('documentclass', '10pt', 'doc')

        # creating header (for logo purposes only)
        header = PageStyle("header")
        with header.create(Head("R")):
            header.append(bold("Radio Aktywne"))
        doc.preamble.append(header)
        doc.change_document_style("header")

        # centralized minipage for title
        with doc.create(MiniPage(align='c')):
            doc.append(LargeText(bold(title)))

        # generate headers
        for i in range(5):
            doc.append(LineBreak())
        doc.append(italic(intro))
        for i in range(len(main_hash["headers"])):
            doc.append(bold(str(i + 1) + ". " + main_hash["headers"][i] + "\n"))
        doc.append(italic("\nWiadomości przedstawi: [Osoba]"))

        # generate news
        with doc.create(Description()) as desc:
            for i in range(len(main_hash["news"])):
                desc.add_item(str(i + 1) + ".", Command('texttt', (main_hash["news"][i])))

        doc.append(italic(outro))

        doc.generate_pdf('full', clean_tex=False)

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

genPdf(testhash)