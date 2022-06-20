import tkinter as tk
import sqlite3
from PIL import ImageTk
from numpy import random

BG_COLOR = '#3d6466'


def fetch_db():
    conn = sqlite3.connect('./data/recipes.db')
    cursor = conn.cursor()
    # fetch all table names
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    all_tables = cursor.fetchall()

    # choose a random recipe
    idx = random.randint(0, len(all_tables) - 1)

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute(f"SELECT * FROM {table_name};")
    records = cursor.fetchall()

    conn.close()
    return table_name, records


def pre_process(recipe_name, ingredients):
    title = recipe_name[:-6]
    title = ''.join([char if char.islower() else f" {char}" for char in title])
    print(title)

    ingredients = [f'{i[2]} {i[3]} of {i[1]}' for i in ingredients]
    print(ingredients[0])

    return title, ingredients


# initialize the app
root = tk.Tk()
root.title("Random Recipe Picker")
# root.eval('tk::PlaceWindow . center')
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry(f'500x600+{str(x)}+{str(y)}')


def load_frame1():
    frame1.pack_propagate(False)

    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file='./assets/RRecipe_logo.png')
    logo_widget = tk.Label(frame1, image=logo_img, bg=BG_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text='ready for you random recipe?',
             bg=BG_COLOR,
             fg='white',
             font=('TKMenuFont', 14)
             ).pack()
    # button widget
    tk.Button(
        frame1,
        text='SHUFFLE',
        font=('TKHeadingFont', 20),
        bg='#28393a',
        fg='white',
        cursor='hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=lambda: load_frame2()
    ).pack(pady=20)


def load_frame2():
    table_name, records = fetch_db()
    title, records = pre_process(table_name, records)


# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=BG_COLOR)
frame2 = tk.Frame(root, bg=BG_COLOR)

for frame in (frame1, frame2,):
    frame.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()
