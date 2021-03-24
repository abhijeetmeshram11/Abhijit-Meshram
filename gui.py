import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
import numpy as np
import cv2
import pytesseract as tess
from keras.models import load_model
from keras.preprocessing import image
from os import listdir
from os.path import isfile, join

# dimensions of our images
img_width, img_height = 150, 150

# load the model we saved
# model = load_model('./Brain_tumor_model.h5')
# model.compile(loss='binary_crossentropy',
#               optimizer='rmsprop',
#               metrics=['accuracy'])

top = tk.Tk()
top.geometry('900x700')
top.title('Brain Tumor Detector')

top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 35, 'bold'))
# label.grid(row=0,column=1)
sign_image = Label(top, bd=10)


def classify(file_path):
    #######################################################
    res_text = [0]
    res_img = [0]
    img = cv2.imread(file_path)
    # cv2.imshow("input",img)

    # if cv2.waitKey(0) & 0xff == ord('q'):
    #     pass
    img2 = cv2.GaussianBlur(img, (3, 3), 0)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    img2 = cv2.Sobel(img2, cv2.CV_8U, 1, 0, ksize=3)
    _, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(17, 3))
    morph_img_threshold = img2.copy()
    cv2.morphologyEx(src=img2, op=cv2.MORPH_CLOSE, kernel=element, dst=morph_img_threshold)
    num_contours, hierarchy = cv2.findContours(morph_img_threshold, mode=cv2.RETR_EXTERNAL,
                                               method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img2, num_contours, -1, (0, 255, 0), 1)

    for i, cnt in enumerate(num_contours):

        min_rect = cv2.minAreaRect(cnt)

    #######################################################


def show_classify_button(file_path):
    classify_b = Button(top, text="Check Report", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 15, 'bold'))
    classify_b.place(x=490, y=550)
    # classify_b.pack(side=,pady=60)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 15, 'bold'))
upload.pack()
upload.place(x=210, y=550)
# sign_image.pack(side=BOTTOM,expand=True)
sign_image.pack()
sign_image.place(x=70, y=200)

# label.pack(side=BOTTOM,expand=True)
label.pack()
label.place(x=500, y=220)
heading = Label(top)
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()