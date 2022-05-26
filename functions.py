from tkinter import INSERT

global data


# Cut function
def cut_text(txt, root):
    global data
    if txt.selection_get():
        data = txt.selection_get()
        txt.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(data)


# Copy function
def copy_text(txt, root):
    global data
    if txt.selection_get():
        data = txt.selection_get()
        root.clipboard_clear()
        root.clipboard_append(data)


# Paste function
def paste_text(txt):
    global data
    if data:
        position = txt.index(INSERT)
        txt.insert(position, data)
