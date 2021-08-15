import qrcode
from PIL import Image
from tkinter import *
import tkinter as tk




def qrmaker(data, file_name, front, back):
    qr = qrcode.QRCode(
        version=2,
        box_size=15,
        border=2
    )
    if data == '':
        pass
    if file_name == '':
        file_name = "alpha.png"
    if front == '':
        front = 'black'
    if back == '':
        back = 'white'

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=front, back_color=back)
    img.save(f"{file_name}.png")

def window():
    window = tk.Tk()
    window.title("QR Maker")
    window.geometry('800x500')
    window.iconbitmap(".//qrmaker.ico")
    window.configure(background="black")
    window.resizable(0, 0)
    # window.overrideredirect(0)
    log_pass_code = StringVar()
    filenamer = StringVar()
    fcolor = StringVar()
    bgcolor = StringVar()

    w = Label(window, text="QR Maker ", cursor="dotbox", font=('Calibri', 30, "bold"), fg="white", bg="black")
    w.place(x=100, y=20)
    w = Label(window, text="By MUHAMMAD TALHA TARIQ ", cursor="dotbox", font=('Calibri', 12, "bold"), fg="#e01f3d", bg="black")
    w.place(x=100, y=70)


    w = Label(window, text="Enter Text for Conversion", cursor="dotbox", font=('Calibri', 12, "normal"), fg="white", bg="black")
    w.place(x=100, y=190)
    passEntered = Entry(window, width=30, cursor="dotbox", highlightthickness=0, fg="white", relief="flat",
                        bg="#505050", font=('Calibri', 12, "normal"), textvariable=log_pass_code)
    passEntered.place(x=300, y=190)


    w = Label(window, text="Enter Custom Filename ", cursor="dotbox", font=('Calibri', 12, "normal"), fg="white", bg="black")
    w.place(x=100, y=220)
    passEntered = Entry(window, width=30, cursor="dotbox", highlightthickness=0,fg="white", relief="flat",
                        bg="#505050", font=('Calibri', 12, "normal"), textvariable=filenamer)
    passEntered.place(x=300, y=220)


    w = Label(window, text="Enter Foreground Color", cursor="dotbox", font=('Calibri', 12, "normal"), fg="white", bg="black")
    w.place(x=100, y=250)
    passEntered = Entry(window, width=30, cursor="dotbox", highlightthickness=0,fg="white", relief="flat",
                        bg="#505050", font=('Calibri', 12, "normal"), textvariable=fcolor)
    passEntered.place(x=300, y=250)


    w = Label(window, text="Enter Background Color", cursor="dotbox", font=('Calibri', 12, "normal"), fg="white", bg="black")
    w.place(x=100, y=280)
    passEntered = Entry(window, width=30, cursor="dotbox", highlightthickness=0,fg="white", relief="flat",
                        bg="#505050", font=('Calibri', 12, "normal"), textvariable=bgcolor)
    passEntered.place(x=300, y=280)


    submit = Button(window, text="Convert Text to QR", relief=FLAT, width=20, font=('Calibri', 12, "bold"), background="#e01f3d",
                    foreground="white", cursor="dotbox", command=lambda: qrmaker(data=log_pass_code.get(), file_name=filenamer.get(), front=fcolor.get(), back=bgcolor.get()))
    submit.place(x=330, y=320)

    window.mainloop()

window()
