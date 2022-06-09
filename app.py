# By Tymek Gryszkalis 2022
#
# Tkinter version 8.6.12
from tkinter import *
import pdf_generator

ENTRY_FONT = "Arial 12"
SMALL_WIDTH = 30
BIG_WIDTH = 100
BIG_HEIGHT = 6

option = "n"
hour = "19:00"
pronouns = "m"

def selectOption(choice):
    global option
    if choice == "Wiadomości Studenckie":
        option = "n"
    elif choice == "Kurier Kulturalny":
        option = "c"
    elif choice == "Wiadomości Sportowe":
        option = "s"
    newsField()

def hourOption(choice):
    global hour
    hour = choice

def clearFrame(frame):
    for widget in frame.winfo_children():
            widget.destroy()

def generate():
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
        "pronouns" : pronouns,
        "date" : data_date
    }

    if option == "n":
        data_title1 = inp_title1.get()
        data_title2 = inp_title2.get()
        data_title3 = inp_title3.get()
        hash["headers"] = [data_title1, data_title2, data_title3]
        hash["time"] = hour
    
    success = Label(com, text = "Wygenerowano!")
    if pdf_generator.genPdf(hash):
        success.pack()

def newsField():
    clearFrame(frame)
    clearFrame(com)

    label_text = Label(frame, text = "Autor:", font = "Arial 12")
    label_text.pack()
    global author_window
    author_window = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
    author_window.pack()

    label_text = Label(frame, text = "Data:", font = "Arial 12")
    label_text.pack()
    global date_window
    date_window = Entry(frame, width = SMALL_WIDTH, font = ENTRY_FONT)
    date_window.pack()

    if option == "n":
        label_text = Label(frame, text = "Godzina", font = "Arial 12")
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

root = Tk()
root.geometry("1280x720")
root.iconbitmap('icon.ico')
root.title("Newseser")

header = Label(root, text = "Generator newsów", font = "Arial 12 bold")
header.pack()

news_options = ["Wiadomości Studenckie", "Kurier Kulturalny", "Wiadomości Sportowe"]
options_var = StringVar()
options_var.set(news_options[0])
options_widget = OptionMenu(root, options_var, *news_options, command = selectOption)
options_widget.pack()

frame = Frame(root)
frame.pack()

com = Frame(root)

newsField()

generate_button = Button(root, text = "Generuj", command = generate)
generate_button.pack()

com.pack()

root.mainloop()