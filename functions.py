from tkinter import INSERT


global selected
selected = False


def cut_text(e, txt, root):
    global selected
    # Check to see if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if txt.selection_get():
            selected = txt.selection_get()
            txt.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


# Copy Text
def copy_text(e, txt, root):
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()

    if txt.selection_get():
        # Grab selected text from text box
        selected = txt.selection_get()
        # Clear the clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected)


# Paste Text
def paste_text(e, txt, root):
    global selected
    # Check to see if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = txt.index(INSERT)
            txt.insert(position, selected)
