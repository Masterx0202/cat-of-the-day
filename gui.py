from PIL import Image, ImageTk
import tkinter as tk
import os
import getimg as img

img.get_titles_and_images("cats", 10)

root = tk.Tk()
root.title("Cat of the Day")
root.geometry("400x900")

images = []

y_position = 100
count = 0

tk.Label(root, text="Cat of the Day", font=("arial", 40)).pack()

def closing():
    count = 1
    while count < 11:
        os.remove("cutecat" + str(count) + ".jpg")
        count += 1
    root.destroy()
    
root.protocol("WM_DELETE_WINDOW", closing)

for i in range(10):

    xcount = 10
    swich = False
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 :
        xcount = 200
    image_path = f"cutecat{i + 1}.jpg"
    image = Image.open(image_path)
    max_width, max_height = 190, 140
    image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)

    label.place(x=xcount, y=y_position)
    if count == 1 or count == 3 or count == 5 or count == 7 or count == 9:
        y_position += 150

    images.append(photo)
    count += 1
    print("cutecat" + str(i + 1), "x =" + str(xcount), "y=" + str(y_position))

root.mainloop()
