from tkinter import *


def req_window():

    """
    Basic GUI window that takes the Link for the Image / Audio request
    :returns:
    A Tuple with the Image Source and Name, respectively
    """

    window = Tk()
    window.title('Image and Audio File Requests')
    window.geometry('220x100+600+250')
    window.iconbitmap('picture_file_image_photo_gallery_icon_219497.ico')
    # Input Field for the Image / Audio Link.
    label1 = Label(text='Image Link: ')
    label1.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
    link_input = Entry(window)
    link_input.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')
    # Input Field for the File name.
    label2 = Label(text='File Name: ')
    label2.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
    image_input = Entry(window)
    image_input.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')
    # Submit Button closes the application and continues the program with the user input.
    button = Button(window, text='Submit', command=window.quit())
    button.grid(row=2, column=1, padx=5, pady=5, sticky='nswe')
    window.mainloop()
    return link_input.get(), image_input.get()


def error_window(error):

    """
    If the request fails, displays the Error Code to the user.
    :param error:
    Takes the Error Code given in the failed request.

    """
    window = Tk()
    window.geometry('250x100+600+250')
    window.title(f'Error {error}')
    window.iconbitmap('picture_file_image_photo_gallery_icon_219497.ico')
    label = Label(window,
                  text = f'Image Request Error {error}',
                  font = ('Arial', 15),
                  fg = '#000000',
                  relief = RAISED,
                  bd = 3,)
    label.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
    label.place(relx=.5, rely=.5, anchor="center")
    window.mainloop()
