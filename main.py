import tkinter as tk
from PIL import ImageTk

# initialize the app
root = tk.Tk()
root.title("Recipe Picker")
#root.eval('tk::PlaceWindow . center')
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry(f'500x600+{str(x)}+{str(y)}')

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg='#3d6466')
frame1.grid(row=0, column=0)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file='./assets/RRecipe_logo.png')
logo_widget = tk.Label(frame1, image=logo_img, bg='#3d6466')
logo_widget.image = logo_img
logo_widget.pack()

# run app
root.mainloop()
