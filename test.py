from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from os import listdir
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
import cv2
import pytesseract as tess
from os.path import isfile, join

# dimensions of our images
img_width, img_height = 150, 150

# load the model we saved
model = load_model('./Brain_tumor_model.h5')

model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

top = tk.Tk()
top.geometry('900x700')
top.title('Brain Tumor Detector')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 35, 'bold'))
sign_image = Label(top, bd=10)

yes_counter = 0
no_counter = 0
def classify(file_path):
    yes_counter = 0
    no_counter = 0
    img = image.load_img(file_path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size=10)

    p1 = Entry(top)
    p1.place(x=600, y=270, width=120, height=50)
    p1.configure(font=("Calibri 20"))

    if classes == 0:
        p1.insert(0, "No")
    else:
        p1.insert(0, "Yes")

def show_classify_button(file_path):
    classify_b = Button(top, text="Check Report", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 15, 'bold'))
    classify_b.place(x=490, y=550)
    # classify_b.pack(side=,pady=60)

def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
    im = ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    label.configure(text='')
    show_classify_button(file_path)

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