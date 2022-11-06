import requests
from tkinter import *

def format_check(link): #Checks the image format for
    if '.png/' in link:
        return '.png'
    elif '.jpg/' in link:
        return '.jpg'
    elif '.jpeg/' in link:
        return '.jpeg'
    elif '.gif/' in link:
        return '.gif'

window = Tk()
label1 = Label(text = 'Image Link: ')
label1.grid(row = 0 , column = 0)
link_input = Entry(window)
link_input.grid(row = 0, column = 1)
label2 = Label(text = 'File Name: ')
label2.grid(row = 1, column = 0)
image_input = Entry(window)
image_input.grid(row = 1, column = 1)
def close_button():
    window.quit()
button = Button(window, text = 'Submit', command = close_button)
button.grid(row = 2, column = 1)
window.mainloop()
link = link_input.get()
image_name = image_input.get()
pic_req = requests.get(link)
if pic_req.status_code == 200:
    with open(f"{image_name}{format_check(link)}", 'wb') as f:
        f.write(pic_req.content)