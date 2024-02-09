# importing tkinter module
from tkinter import *
from tkinter import ttk

from PIL import ImageTk,Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("800x500")

        Label(self.listWindow, text="Liste over indbetalinger", font=("calibri", 15)).pack()

        # todone: create column
        # todone: sorter liste AKA prioritise mest betalt
        # https://www.tutorialspoint.com/how-to-add-a-column-to-a-tkinter-treeview-widget
        style = ttk.Style()
        style.theme_use('clam')
        tree = ttk.Treeview(self.listWindow, column=(1, 2, 3), show='headings')
        tree.column(1, anchor=CENTER)
        tree.heading(1, text="Navn")
        tree.column(2, anchor=CENTER)
        tree.heading(2, text="Betalt")
        tree.column(3, anchor=CENTER)
        tree.heading(3, text="Mangler")

        # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        sorted_footballers_by_goals = sorted(master.fodboldtur.items(), key=lambda x: x[1], reverse=True)
        converted_dict = dict(sorted_footballers_by_goals)

        for key, value in converted_dict.items():
            tree.insert(
                '',
                'end',
                text=f'1',
                values=(key, f'{int(value)} kr', f'{master.target - int(value)} kr'))

        tree.pack()

