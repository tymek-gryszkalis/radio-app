from tkinter import *

option = "n"

def selectOption(choice):
    if choice == "Wiadomości Studenckie":
        option = "n"
        newsField()
    elif choice == "Kurier Kulturalny":
        option = "c"
        notNewsField()
    elif choice == "Wiadomości Sportowe":
        option = "s"
        notNewsField()

def newsField():
    for widget in frame.winfo_children():
            widget.destroy()
    for i in range(3):
        inp_title = Entry(frame, width = "10", font = "Arial 12")
        inp_news = Text(frame, width = "100", height = "5", font = "Arial 12")
        inp_title.pack()
        inp_news.pack()

def notNewsField():
    for widget in frame.winfo_children():
            widget.destroy()
    for i in range(3):
        inp_news = Text(frame, width = "100", height = "5", font = "Arial 12")
        inp_news.pack()

root = Tk()
root.geometry("1280x720")
root.iconbitmap('icon.ico')

header = Label(root, text = "Generator newsów", font = "Arial 12 bold")
header.pack()

news_options = ["Wiadomości Studenckie", "Kurier Kulturalny", "Wiadomości Sportowe"]
options_var = StringVar()
options_var.set(news_options[0])
options_widget = OptionMenu(root, options_var, *news_options, command = selectOption)
options_widget.pack()

frame = Frame(root)
frame.pack()

newsField()

root.mainloop()