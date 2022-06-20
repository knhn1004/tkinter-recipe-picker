import tkinter as tk
from PIL import ImageTk

BG_COLOR = '#3d6466'

# initialize the app
root = tk.Tk()
root.title("Random Recipe Picker")
#root.eval('tk::PlaceWindow . center')
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry(f'500x600+{str(x)}+{str(y)}')

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=BG_COLOR)
frame1.grid(row=0, column=0)
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


def load_frame2():
    print('load frame2')


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
    command=load_frame2
).pack(pady=20)


# run app
root.mainloop()
