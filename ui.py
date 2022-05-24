# Create simple UI using tkinter framework
from tkinter import *
from functions import *

root = Tk()
root.title('My cool text editor')
root.geometry("900x700")

# Create main frame
frame = Frame(root)
frame.pack(pady=5)

# Create vertical scrollbar
ver_scroll = Scrollbar(frame)
ver_scroll.pack(side=RIGHT, fill=Y)

# Create horizontal scrollbar
hor_scroll = Scrollbar(frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create text box
my_text = Text(frame, width=75, height=25, font=("Minion Pro", 16), selectbackground="blue",
               selectforeground="black", undo=True, yscrollcommand=ver_scroll.set, wrap="none",
               xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure our scrollbar
ver_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False, my_text, root), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False, my_text, root), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False, my_text, root), accelerator="(Ctrl+v)")

root.mainloop()
