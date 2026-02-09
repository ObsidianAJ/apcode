from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFilter
import random
import os

root = Tk()
root.title("Photoshoppe")
root.geometry("830x420")
root.config(bg="teal")
loaded_image = None
start_x,start_y = None,None
pixelate_mode = False
crop_mode = False
rect = None


''' MODEL - Functions and Data'''
def load_image():
    global loaded_image
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
   
    if file_path:
        img = Image.open(file_path)
        img = img.resize((600, 400), Image.Resampling.LANCZOS)
        loaded_image = img  
        display_image(loaded_image)

def display_image(image):
    global loaded_image
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)

def apply_contrast():
    global loaded_image
    image = loaded_image
    pixels = image.load()
    for y in range(loaded_image.height):
        for x in range(loaded_image.width):
            r,g,b=pixels[x,y]
            r/=255;g/=255;b/=255
            r=0.5+1.5*(r-0.5)
            g=0.5+1.5*(g-0.5)
            b=0.5+1.5*(b-0.5)
            r=int(max(0,min(1,r))*255)
            g=int(max(0,min(1,g))*255)
            b=int(max(0,min(1,b))*255)
            pixels[x,y]=(r,g,b)
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)


# Save the modified image
def save_image():
    global loaded_image
    if loaded_image:
        # Ask user where to save the file
        save_path = filedialog.asksaveasfilename(
            title="Save Image As",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg;*.jpeg"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*")
            ]
        )
        if save_path:
            try:
                loaded_image.save(save_path)
                print(f"Image successfully saved to: {save_path}")
            except Exception as e:
                print(f"Error saving image: {e}")
        else:
            print("Save cancelled.")
    else:
        print("No image loaded to save.")

def dotted_art_thing():
    global loaded_image
    image = loaded_image
    pixels = image.load()
    canvas1 = Image.new("RGB",(image.size[0],image.size[1]), "white")
    for c in range(5000000):
        x = random.randint(1,image.width-5)  
        y = random.randint(1,image.height-5)  
        size = random.randint(3,5)
        ellipsebox=[(x,y),(x+size,y+size)]
        draw = ImageDraw.Draw(canvas1)
        draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
        del draw
    image = canvas1
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)

def sepia():
    global loaded_image
    image = loaded_image
    pixels = image.load()   
    for y in range(image.height):
        for x in range(image.width):
            red = pixels[x,y][0]*.393 + pixels[x,y][1]*.769+ pixels[x,y][0]*.189
            green = pixels[x,y][0]*.349 + pixels[x,y][1]*.686+ pixels[x,y][0]*.168
            blue = pixels[x,y][0]*.272 + pixels[x,y][1]*.534+ pixels[x,y][0]*.131
            pixels[x,y] = (round(red),round(green),round(blue))
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)

def invert_image():
    global loaded_image
    image = loaded_image
    pixels = image.load()   
    for y in range(image.height):
        for x in range(image.width):
            delta1 = 255 - pixels[x,y][0]
            delta3 = 255 - pixels[x,y][2]
            delta2 = 255 - pixels[x,y][1]
            pixels[x,y] = (delta1, delta2,delta3)
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)

def more_buttons():
    for num in range(1000):
        x = random.randint(root.width)
        y = random.randint(root.height)

def on_click(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def on_drag(event):
    global start_x, start_y, rect
    canvas.delete(rect)
    rect = canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="white", width=5)

def on_release(event):
    global start_x, start_y, rect
    canvas.delete(rect)
    if pixelate_mode:
        pixelate(start_x, start_y, event.x - start_x, event.y - start_y)
    
def activate_pixelate():
    global pixelate_mode
    pixelate_mode = True
    print("pixel mode on")

def pixelate(startx, starty, width, hieght):
    global loaded_image
    image = loaded_image
    pixels = image.load()
    for x in range(startx, startx+width, 10):
        for y in range(starty, starty+hieght, 10):
            color = (pixels[x,y][0],pixels[x,y][1],pixels[x,y][2])
            for x1 in range (x, x+10):
                for y1 in range (y, y+10):
                    if startx <= x1 <= startx+width and starty <= y1 <= starty+hieght:
                        pixels[x1,y1] = (color)
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(300, 200, image=root.photo_image)

''' CONTROLLERS - Widgets That Users Interact With'''
pick_image = Button(root, text="upload Image", fg="purple", bg="teal", font=("Times New Roman", 15), command=load_image)
invert = Button(root, text="invert", fg="purple", bg="teal", font=("Times New Roman", 15), command=invert_image)
pointalism = Button(root, text="pointalism", fg="purple", bg="teal", font=("Times New Roman", 15), command= dotted_art_thing)
pixelate_button= Button(root, text="pixelate", fg="purple", bg="teal", font=("Times New Roman", 15), command = activate_pixelate)
crop= Button(root, text="crop", fg="purple", bg="teal", font=("Times New Roman", 15))
sepia_button = Button(root, text="sepia", fg="purple", bg="teal", font=("Times New Roman", 15), command=sepia)
contrast = Button(root, text="contrast increase", fg="purple", bg="teal", font=("Times New Roman", 15), command=apply_contrast)
save = Button(root, text="save image", fg="purple", bg="teal", font=("Times New Roman", 15),command=save_image)
xtra_cred = Button(root, text="xtra cred farmer", fg="purple", bg="teal", font=("Times New Roman", 5),command=save_image)
pick_image.place(x=10,y=10, width=200, height=20)
contrast.place(x=10,y=35, width=200, height=20)
invert.place(x=10,y=60, width=200, height=20)
pointalism.place(x=10,y=85, width=200, height=20)
crop.place(x=10,y=110, width=200, height=20)
pixelate_button.place(x=10,y=135, width=200, height=20)
sepia_button.place(x=10,y=160, width=200, height=20)
save.place(x=10,y=185, width=200, height=20)
xtra_cred.place(x=830,y=410, width=50, height=10)



''' VIEW - Widgets That Display Visuals'''
canvas = Canvas(root)
canvas.place(x=220,y=10,  width=600, height=400)
canvas.bind("<Button-1>",on_click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)


root.mainloop()