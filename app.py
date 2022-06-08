from tkinter import *

root = Tk()
root.geometry("1280x720")
root.iconbitmap("icon.ico")

header = Label(root, text = "Generator newsów", font = "Arial 12 bold")
header.pack()
check_st = Checkbutton(root, text = "Studenckie")
check_sp = Checkbutton(root, text = "Sportowe")
check_k = Checkbutton(root, text = "Kurier")
check_st.pack()
check_sp.pack()
check_k.pack()
for i in range(3):
    inp_title = Entry(root, width = "10", font = "Arial 12")
    inp_news = Text(root, width = "100", height = "5", font = "Arial 12")
    inp_title.pack()
    inp_news.pack()
but_generate = Button(root, text = "Generuj")
but_generate.pack()

root.mainloop()
