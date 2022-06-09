from tkinter import *

option = "n"

def selectOption(choice):
    global option
    if choice == "Wiadomości Studenckie":
        option = "n"
    elif choice == "Kurier Kulturalny":
        option = "c"
    elif choice == "Wiadomości Sportowe":
        option = "s"
    newsField()

def newsField():
    for widget in frame.winfo_children():
            widget.destroy()

    author_text = Label(frame, text = "Autorstwa:", font = "Arial 12")
    author_text.pack()
    author_window = Entry(frame, width = "10", font = "Arial 12")
    author_window.pack()

    if option == "n":
        hour_text = Label(frame, text = "Godzina", font = "Arial 12")
        hour_text.pack()
        hour_options = ["19:00", "19:30"]
        hour_var = StringVar()
        hour_var.set(hour_options[0])
        hour_widget = OptionMenu(frame, hour_var, *hour_options)
        hour_widget.pack()

    for i in range(3):
        inp_news = Text(frame, width = "100", height = "5", font = "Arial 12")
        if option == "n":
            inp_title = Entry(frame, width = "10", font = "Arial 12")
            inp_title.pack()
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