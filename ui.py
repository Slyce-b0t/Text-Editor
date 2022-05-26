# Create simple UI using tkinter framework
from tkinter import *
from functions import *

root = Tk()
root.title('binary text editor')
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
binary_text = Text(frame, width=75, height=25, font=("Minion Pro", 16), selectbackground="blue",
               selectforeground="black", undo=True, yscrollcommand=ver_scroll.set, wrap="none",
               xscrollcommand=hor_scroll.set)
binary_text.pack()

# Configure our scrollbars
ver_scroll.config(command=binary_text.yview)
hor_scroll.config(command=binary_text.xview)

# Create menu
binary_menu = Menu(root)
root.config(menu=binary_menu)

# Add edit menu
edit_menu = Menu(binary_menu, tearoff=False)
binary_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(binary_text, root))
edit_menu.add_command(label="Copy", command=lambda: copy_text(binary_text, root))
edit_menu.add_command(label="Paste", command=lambda: paste_text(binary_text))

root.mainloop()
