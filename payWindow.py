# importing tkinter module
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,
              text="Indbetal").pack()

        # todone: add dropdown
        root = self.payWindow
        clicked = StringVar()
        clicked.set("Choose")
        names = list(master.fodboldtur.keys())
        OptionMenu(root, clicked, *names, command=self.clicked.get()).pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        # Tilføj og fjern "X" af penge
        self.payButton = Button(self.payWindow, text="betal", command=self.addMoney)
        self.payButton.pack(padx=30, pady=10, side=LEFT)
        self.goneButton = Button(self.payWindow, text="Fjern", command=self.removeMoney)
        self.goneButton.pack(padx=30, pady=10, side=LEFT)

    # todo: Add view selected payers money paid amount
    # todo: View payers in dropdown menu

    def addMoney(self):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
        self.master.gemFilen()

    # todo: Add remove money option
    def removeMoney(self):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return
        self.master.total -= amount
        self.master.progressLabelText.set(f"Fjernet: {self.master.total} af {self.master.target} kroner:")
        print(f"Fjernet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
        self.master.gemFilen()
