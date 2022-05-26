# Text-Editor


## Overview
Simple text editor that only consist of writing, cuting, coping and pasting text. Used tkinter for simple user interface. For creating cut and copy functions used stack logic(last in first out). Now let's look out how functions code works(not the tkinter part).


About the 'INSERT' imported from tkinter we will talk about later, first, created value named data. Date will store cutted or copied data and as you guess when we execute paste function it will search a text inside this value


### Cut function
First calling our data value that will store or already stored selected text. After this, trying store our selected text. If it's not possible, we will face with warning. But if everything is okay, cutted text will store in data(if already some text stored here, new text will store in place of old text, and old text will delete). Next step we clear everything between first selected charecter(sel.first) and last selected charecter(sel.last).

### Copy function
Almost everything likes cut function. But insted of delete highlighted part, we keep highlighted part. As the name request.

### Paste function
Like copy and cut functions, first we call our global data that will store or already stored some data. Next step we use INSERT keyword for make understand python where it will copy the text. Once find right location it simply pasting stored data to the appropriate place. And you can paste as much as you want since you already cut or paste some text. Other way, it will show warning
