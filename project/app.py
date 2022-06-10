# By Tymek Gryszkalis 2022
#
# Tkinter version 8.6.12

from tkinter import *
import pdf_generator

# Visual constants (feel the css vibe)
ENTRY_FONT = "Courier 12"
LABEL_FONT = "Arial 12"
HEADER_FONT = "Arial 24 bold"
SMALL_WIDTH = 30
BIG_WIDTH = 100
BIG_HEIGHT = 6

# Vars to pass on
option = "n"
hour = "19:00"
pronoun = "m"

# fuction for type optionbox
def typeOption(choice):
    global option
    if choice == "Wiadomości Studenckie":
        option = "n"
    elif choice == "Kurier Kulturalny":
        option = "c"
    elif choice == "Wiadomości Sportowe":
        option = "s"
    newsField()

# function for hour optionbox
def hourOption(choice):
    global hour
    hour = choice

# function for pronouns optionbox
def pronounOption(choice):
    global pronoun
    if choice == "\"Przygotował\"":
        pronoun = "m"
    elif choice == "\"Przygotowała\"":
        pronoun = "f"
    elif choice == "\"Przygotowałx\"":
        pronoun = "o"

# quick frame clear
def clearFrame(frame):
    for widget in frame.winfo_children():
            widget.destroy()

# pdf generating
def generate():
    # making hash
    clearFrame(com)
    data_author = author_window.get()
    data_date = date_window.get()
    data_news1 = inp_news1.get("1.0", END)
    data_news2 = inp_news2.get("1.0", END)
    data_news3 = inp_news3.get("1.0", END)

    hash = {
        "type" : option,
        "news" : [data_news1, data_news2, data_news3],
        "author" : data_author,
        "pronouns" : pronoun,
        "date" : data_date
    }

    if option == "n":
        data_title1 = inp_title1.get()
        data_title2 = inp_title2.get()
        data_title3 = inp_title3.get()
        hash["headers"] = [data_title1, data_title2, data_title3]
        hash["time"] = hour
    
    # generating and catching success or failure
    success = Label(com, text = "Wygenerowano!")
    failure = Label(com, text = "Błąd! Zamknij PDF-y z wiadomościami przed generowaniem kolejnych!")
    if pdf_generator.genPdf(hash):
        success.pack()
    else:
        failure.pack()

# generating fields for news (depending on the type)
def newsField():
    clearFrame(frame)
    clearFrame(com)

    label_text = Label(frame, text = "Autor:", font = LABEL_FONT)
    label_text.pack()
    global author_window
    author_window = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
    author_window.pack()

    label_text = Label(frame, text = "Data:", font = LABEL_FONT)
    label_text.pack()
    global date_window
    date_window = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
    date_window.pack()

    label_text = Label(frame, text = "Zaimek:", font = LABEL_FONT)
    label_text.pack()
    pronoun_options = ["\"Przygotował\"", "\"Przygotowała\"", "\"Przygotowałx\""]
    pronoun_var = StringVar()
    pronoun_var.set(pronoun_options[0])
    pronoun_widget = OptionMenu(frame, pronoun_var, *pronoun_options, command = pronounOption)
    pronoun_widget.pack()

    # Ugly as heck, but what can you do (seiously if someone knows what can you do please let me know I hate this piece of code)
    if option == "n":
        label_text = Label(frame, text = "Godzina:", font = LABEL_FONT)
        label_text.pack()
        hour_options = ["19:00", "19:30"]
        hour_var = StringVar()
        hour_var.set(hour_options[0])
        hour_widget = OptionMenu(frame, hour_var, *hour_options, command = hourOption)
        hour_widget.pack()

    if option == "n":
        global inp_title1
        inp_title1 = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
        inp_title1.pack()
    global inp_news1
    inp_news1 = Text(frame, width = BIG_WIDTH, height = BIG_HEIGHT, font = ENTRY_FONT)
    inp_news1.pack()
    
    if option == "n":
        global inp_title2
        inp_title2 = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
        inp_title2.pack()
    global inp_news2
    inp_news2 = Text(frame, width = BIG_WIDTH, height = BIG_HEIGHT, font = ENTRY_FONT)
    inp_news2.pack()
    
    if option == "n":
        global inp_title3
        inp_title3 = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
        inp_title3.pack()
    global inp_news3
    inp_news3 = Text(frame, width = BIG_WIDTH, height = BIG_HEIGHT, font = ENTRY_FONT)
    inp_news3.pack()

# setting up the 
root = Tk()
root.geometry("1280x720")
root.iconbitmap('./resources/icon.ico')
root.title("Newseser")

header = Label(root, text = "Generator newsów", font = HEADER_FONT)
header.pack()

news_options = ["Wiadomości Studenckie", "Kurier Kulturalny", "Wiadomości Sportowe"]
options_var = StringVar()
options_var.set(news_options[0])
options_widget = OptionMenu(root, options_var, *news_options, command = typeOption)
options_widget.pack()

frame = Frame(root)
frame.pack()

com = Frame(root)

newsField()

generate_button = Button(root, text = "Generuj", command = generate)
generate_button.pack()

com.pack()

root.mainloop()