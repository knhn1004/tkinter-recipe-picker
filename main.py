import pyglet
import tkinter as tk
import sqlite3
from PIL import ImageTk
from numpy import random

BG_COLOR = '#3d6466'

# load custom fonts
pyglet.font.add_file('./fonts/Ubuntu-Bold.ttf')
pyglet.font.add_file('./fonts/Shanti-Regular.ttf')


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


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
    cursor.execute("SELECT * FROM " + table_name + ";")
    records = cursor.fetchall()

    conn.close()

    return table_name, records


def pre_process(table_name, records):
    title = table_name[:-6]
    title = ''.join([char if char.islower() else f" {char}" for char in title])
    print(title)

    ingredients = []
    for r in records:
        name = r[1]
        qty = r[2]
        unit = r[3]
        ingredients.append(qty + " " + unit + " " + name)

    print(records[0])

    return title, records


# initialize the app
root = tk.Tk()
root.title("Random Recipe Picker")
#root.eval('tk::PlaceWindow . center')

# place app in the center of the screen
#x = root.winfo_screenwidth() // 2
#y = int(root.winfo_screenheight() * 0.1)
# root.geometry(f'500x600+{str(x)}+{str(y)}')


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    # frame1.pack_propagate(False)

    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file='./assets/RRecipe_logo.png')
    logo_widget = tk.Label(frame1, image=logo_img, bg=BG_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text='ready for you random recipe?',
             bg=BG_COLOR,
             fg='white',
             font=('Ubuntu', 14)
             ).pack()
    # button widget
    tk.Button(
        frame1,
        text='SHUFFLE',
        font=('Ubuntu', 20),
        bg='#28393a',
        fg='white',
        cursor='hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=load_frame2
    ).pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    # frame2.pack_propagate(False)

    table_name, records = fetch_db()
    title, ingredients = pre_process(table_name, records)

    # logo widget
    logo_img = ImageTk.PhotoImage(file='./assets/RRecipe_logo.png')
    logo_widget = tk.Label(frame2, image=logo_img, bg=BG_COLOR)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(
        frame2,
        text=title,
        bg=BG_COLOR,
        fg='white',
        font=('Ubuntu', 20)
    ).pack(pady=25)

    for i in ingredients:
        tk.Label(
            frame2,
            text=i,
            bg='#28393a',
            fg='white',
            font=('Ubuntu', 12)
        ).pack(fill='both')

    tk.Button(
        frame2,
        text='BACK',
        font=('Ubuntu', 18),
        bg='#28393a',
        fg='white',
        cursor='hand2',
        activebackground='#badee2',
        activeforeground='black',
        command=load_frame1
    ).pack(pady=20)


# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=BG_COLOR)
frame2 = tk.Frame(root, bg=BG_COLOR)

for frame in (frame1, frame2,):
    frame.grid(row=0, column=0)

load_frame1()


if __name__ == '__main__':
    root.mainloop()
