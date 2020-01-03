from tkinter import *
import socket
import json




class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        self.topping = list()
        self.prices = {"medium": 0, "large": 0, "xlarge": 0, "med_topping": 0, "large_topping": 0, "xl_topping": 0}

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname('localhost')

        port = 8000
        s.connect((host, port))
        data = s.recv(1024)

        message = "prices"
        s.send(str.encode(message))
        data = s.recv(1024)
        self.prices = json.loads(bytes.decode(data))

        message = "topping"
        s.send(str.encode(message))
        data = s.recv(1024)
        self.topping = json.loads(bytes.decode(data))

        message = "exit"
        s.send(str.encode(message))

        s.close()

        self.toppingVar = list(self.topping)
        self.chk_toppings = list(self.topping)
        self.create_widget()

    def create_widget(self):

        self.lbl_ss = Label(self, text="Select Size: ")
        self.lbl_ss.grid(row=0, column=0, sticky=W)

        self.size = StringVar()
        self.rad_medium = Radiobutton(self, text='Medium', variable=self.size, value="medium")
        self.rad_medium.grid(row=1, column=0, sticky=W)

        self.rad_large = Radiobutton(self, text="Large", variable=self.size, value="large")
        self.rad_large.grid(row=1, column=1, sticky=W)

        self.rad_xlarge = Radiobutton(self, text="Extra Large", variable=self.size, value="xLarge")
        self.rad_xlarge.grid(row=1, column=2, sticky=W)

        self.rad_medium.select()

        self.lbl_empty = Label(self, text="").grid(row=2, column=0)

        self.lbl_st = Label(self, text="Select Toppings: ")
        self.lbl_st.grid(row=3, column=0, sticky=W)

        line = 3

        for i in range(len(self.topping)):
            line += 1
            self.toppingVar[i] = BooleanVar()
            self.chk_toppings[i] = Checkbutton(self, text=self.topping[i], variable=self.toppingVar[i])
            self.chk_toppings[i].grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.btn_calc = Button(self, text="Calculate Price", width=12, command=self.calculate)
        self.btn_calc.grid(row=line, column=0)

        self.btn_reset = Button(self, text="Reset", width=12, command=lambda: self.reset())
        self.btn_reset.grid(row=line, column=1)

        line += 1
        self.lbl_total = Label(self, text="Total: ")
        self.lbl_total.grid(row=line, column=0, sticky=E)
        self.result = Entry(self, width=10)
        self.result.grid(row=line, column=1, sticky=W)

    def reset(self):
        self.rad_medium.select()

        for i in range(len(self.topping)):
            self.chk_toppings[i].deselect()

        self.result.delete(0, END)

    def calculate(self):
        self.result.delete(0, END)
        self.totalTopping = 0

        for x in range(len(self.topping)):
            if self.toppingVar[x].get():
                self.totalTopping += 1

        if self.size.get() == "medium":
            self.totalprice = self.prices['medium'] + self.totalTopping * self.prices['med_topping']

        elif self.size.get() == "large":
            self.totalprice = self.prices['large'] + self.totalTopping * self.prices['large_topping']

        elif self.size.get() == "xlarge":
            self.totalprice = self.prices['xlarge'] + self.totalTopping * self.prices['xl_topping']

        # strprice = "{}"
        self.result.insert(END, "${}".format(self.totalprice))


window = Tk()
window.title("Python Pizza Calculator")
window.geometry('290x400')
app = Application(window)
app.mainloop()
