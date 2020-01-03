"""
This is my very first project, a fully functional calculator app.
"""

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.screen_input = ""
        self.answer = ""
        self.grid(padx=20, pady=20)
        self.create_widgets()

    def create_widgets(self):
        line = 0
        self.screen = Entry(self, width=20, font=("Verdana", 30, "bold"))
        self.screen.bind("<Key>", lambda e: "break")
        self.screen.insert(0, "0")
        self.screen.grid(row=line, columnspan=5, column=0)

        self.scrollbar = Scrollbar(orient="horizontal", width=20)

        self.screen.config(xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.screen.xview)
        self.scrollbar.grid(row= 0, column=0, sticky=N)

        line += 1
        self.b1 = Button(
            self, text="1", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("1", "1"))
        self.b1.grid(row=line, column=0, sticky="W", pady=20)

        self.b2 = Button(
            self, text="2", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("2", "2"))
        self.b2.grid(row=line, column=1, sticky="W")

        self.b3 = Button(
            self, text="3", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("3", "3"))
        self.b3.grid(row=line, column=2, sticky="W")

        self.bplus = Button(
            self, text="+", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("+"))
        self.bplus.grid(row=line, column=3, sticky="W")

        self.bce = Button(
            self, text="CE", width=5, font=("Verdana", 15, "bold"), command=self.clear)
        self.bce.grid(row=line, column=4, sticky="W")

        line += 1
        self.b4 = Button(
            self, text="4", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("4", "4"))
        self.b4.grid(row=line, column=0, sticky="W", pady=20)

        self.b5 = Button(
            self, text="5", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("5", "5"))
        self.b5.grid(row=line, column=1, sticky="W")

        self.b6 = Button(
            self, text="6", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("6", "6"))
        self.b6.grid(row=line, column=2, sticky="W")

        self.bsub = Button(
            self, text="-", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("-"))
        self.bsub.grid(row=line, column=3, sticky="W")

        self.bdot = Button(
            self, text=".", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen(".", "."))
        self.bdot.grid(row=line, column=4, sticky="W")

        line += 1
        self.b7 = Button(
            self, text="7", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("7", "7"))
        self.b7.grid(row=line, column=0, sticky="W", pady=20)

        self.b8 = Button(
            self, text="8", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("8", "8"))
        self.b8.grid(row=line, column=1, sticky="W")

        self.b9 = Button(
            self, text="9", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("9", "9"))
        self.b9.grid(row=line, column=2, sticky="w")

        self.bmul = Button(
            self, text="*", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen("*"))
        self.bmul.grid(row=line, column=3, sticky="W")

        self.bans = Button(
            self, text="ANS", width=5, font=("Verdana", 15, "bold"), command=self.retrieve_answer)
        self.bans.grid(row=line, column=4, sticky="W")

        line += 1
        self.bdel = Button(
            self, text="DEL", width=5, font=("Verdana", 15, "bold"), command=self.delete)
        self.bdel.grid(row=line, column=0, sticky="W", pady=20)

        self.bzero = Button(
            self, text="0", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen('0', '0'))
        self.bzero.grid(row=line, column=1, sticky="W")

        self.beq = Button(
            self, text="=", width=5, font=("Verdana", 15, "bold"), command=self.equals)
        self.beq.grid(row=line, column=2, sticky="W")

        self.bdiv = Button(
            self, text="/", width=5, font=("Verdana", 15, "bold"), command=lambda: self.insert_to_screen(x="/"))
        self.bdiv.grid(row=line, column=3, sticky="W")

        self.bsq = Button(
            self, text="sq", width=5, font=("Verdana", 15, "bold"), command=self.square)
        self.bsq.grid(row=line, column=4, sticky="W")

    def clear(self):
        self.screen_input = ""
        self.answer = 0
        self.screen.delete(0, END)
        self.screen.insert(END, 0)

    def insert_to_screen(self, x, y=None):
        if self.screen.get() == 0:
            self.screen.delete(0, END)

        if self.screen_input == "":
            self.screen.delete(0, END)

        if len(self.screen.get()) >= 1:
            if (self.screen.get()) == self.answer:
                self.screen.delete(0, END)
                if y is None:
                    self.screen_input = self.answer
                else:
                    self.screen_input = ""

        if self.screen.get == "Error":
            self.screen.delete(0, END)
            self.screen_input = ""

        if y is None:
            self.screen.delete(0, END)

        x = str(x)

        try:
            self.screen_input += x
            self.screen.insert(END, y)

        except:
            pass

    def equals(self):
        answer = self.screen_input
        try:
            ans = eval(answer)
        except:
            self.screen.delete(0, END)
            self.screen_input = ""
            self.screen.insert(END, "Error")

        else:
            ans = str(ans)
            self.screen_input = ans
            self.answer = ans
            self.screen.delete(0, END)
            self.screen.insert(END, ans)

    def retrieve_answer(self):
        self.screen.delete(0, END)
        self.screen_input += str(self.answer)
        self.screen.insert(END, self.answer)

    def square(self):
        value = self.screen_input
        try:
            num = float(value)
        except:
            self.screen.delete(0, END)
            self.screen_input = ""
            self.screen.insert(END, "Error")
        else:
            ans = num * num
            ans = str(ans)
            self.screen_input = ans
            self.answer = ans
            self.screen.delete(0, END)
            self.screen.insert(END, ans)

    def delete(self):
        self.screen_input = self.screen_input[:-1]
        x = (len(self.screen.get())) - 1
        self.screen.delete(x, END)

        if len(self.screen.get()) == 0:
            self.screen.insert(0, "0")

if __name__ == "__main__":
    window = Tk()
    window.geometry("")
    window.resizable(width=False, height=False)
    window.title("Chizzy's Calculator")
    app = Application(window)
    app.mainloop()
