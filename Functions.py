import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageOps
from PIL import ImageEnhance
from tkinter import filedialog
import  cv2
import numpy as np

angle=0

def exit_Button_Script(window):
    window.destroy()

def Contrast(contrast_pos):
    global image
    global saving_Image
    contrast = ImageEnhance.Contrast(image)
    Contrast_Image = contrast.enhance(float(contrast_pos) + 1)
    saving_Image=Contrast_Image
    left_right_space, up_down_space = image_Center(Contrast_Image)
    render = ImageTk.PhotoImage(Contrast_Image)
    global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor="nw")
    global_Canvas.image = render

def Brightness(brightness_pos):
    global image
    global saving_Image
    bright = ImageEnhance.Brightness(image)
    Bright_Image = bright.enhance(float(brightness_pos)+1)
    saving_Image=Bright_Image
    left_right_space, up_down_space = image_Center(Bright_Image)
    render = ImageTk.PhotoImage(Bright_Image)
    global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor="nw")
    global_Canvas.image = render

def Sharpness(sharpness_pos):
    global image
    global saving_Image
    sharp = ImageEnhance.Sharpness(image)
    Sharp_Image = sharp.enhance(float(sharpness_pos)+1)
    saving_Image =Sharp_Image
    left_right_space, up_down_space = image_Center(Sharp_Image)
    render = ImageTk.PhotoImage(Sharp_Image)
    global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor="nw")
    global_Canvas.image = render

def resize(image):
    width, height = image.size
    ratio1 = 500 / width
    ratio2 = 500 / height
    if ratio1 < ratio2:
        resized_height = int(ratio1 * height)
        resized_width = int(ratio1 * width)
        image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        return image
    else:
        resized_width = int(ratio2 * width)
        resized_height = int(ratio2 * height)
        image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        return image

def add_image_to_canvas(canvas,img):
    global original_image
    global image
    global saving_Image
    clear(canvas)
    resized_Image = resize(img)
    image=resized_Image
    saving_Image=resized_Image
    left_right_space,up_down_space = image_Center(resized_Image)
    original_image=resized_Image
    render = ImageTk.PhotoImage(resized_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def image_Center(image):
    width,heiht=image.size
    left_space=(500-width)/2
    up_space=(500-heiht)/2
    return left_space,up_space

def cancel_Changing(canvas):
    global image
    try:
        image = original_image
        render = ImageTk.PhotoImage(original_image)
        left_right_space, up_down_space = image_Center(original_image)
        canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
        canvas.image = render
    except:
        print("You have no image!")

def save(canvas):
    global saving_Image
    global original_image
    global image
    try:
        original_image=saving_Image
        image=saving_Image
        render = ImageTk.PhotoImage(original_image)
        left_right_space, up_down_space = image_Center(original_image)
        canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
        canvas.image = render
    except:
        print("Something is wrong!!")

def save_As(canvas):
    global saving_Image
    global original_image
    global image
    try:
        original_image = saving_Image
        image = saving_Image
        render = ImageTk.PhotoImage(original_image)
        left_right_space, up_down_space = image_Center(original_image)
        canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
        canvas.image = render

        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
            return
        original_image.save(filename)
    except:
        print("Something is wrong!!")

def selected_image(canvas):
    try:
        global global_Canvas
        filename = filedialog.askopenfilename(initialdir = "../../", title = "Select Image to Edit", filetypes = (("All files","*"),("jpeg files", "*.jpeg"), (
        "png files", "*.png"), ("jpg files", "*.jpg")))
        image = Image.open(filename)
        global_Canvas = canvas
        add_image_to_canvas(canvas,image)
    except:
        print("Please, chose a photo!")


def clear(canvas):
    canvas.delete("all")

def Rotate(canvas):
    global image
    global saving_Image
    Rotated_Image = image.rotate(90,expand = True)
    Rotated_Image = resize(Rotated_Image)
    image = Rotated_Image
    saving_Image=Rotated_Image
    left_right_space, up_down_space = image_Center(Rotated_Image)
    render = ImageTk.PhotoImage(Rotated_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor="nw")
    canvas.image = render

def Flip(canvas):
    global image
    global saving_Image
    Flipped_Image = image.transpose(Image.FLIP_LEFT_RIGHT)
    Flipped_Image = resize(Flipped_Image)
    image = Flipped_Image
    saving_Image=Flipped_Image
    left_right_space, up_down_space = image_Center(Flipped_Image)
    render = ImageTk.PhotoImage(Flipped_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

crop_area=0
crop_start_x=0
crop_start_y=0
crop_end_x=0
crop_end_y=0
def start_crop(event):
    global crop_start_x
    global crop_start_y
    crop_start_x = event.x
    crop_start_y = event.y

def end_crop(event):
    global crop_end_x
    global crop_end_y
    global Cropped_Image
    global image
    global saving_Image
    try:
        left,up= image_Center(image)
        if crop_start_x<crop_end_x and crop_start_y<crop_end_y:
            Cropped_Image = image.crop([crop_start_x-left, crop_start_y-up, crop_end_x-left, crop_end_y-up])
            image=Cropped_Image
            saving_Image=Cropped_Image
            left_right_space, up_down_space = image_Center(Cropped_Image)
            render = ImageTk.PhotoImage(Cropped_Image)
            global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
            global_Canvas.image = render
        elif crop_start_x>crop_end_x and crop_start_y<crop_end_y:
            Cropped_Image = image.crop([crop_end_x - left, crop_start_y - up, crop_start_x-left , crop_end_y - up])
            image = Cropped_Image
            saving_Image = Cropped_Image
            left_right_space, up_down_space = image_Center(Cropped_Image)
            render = ImageTk.PhotoImage(Cropped_Image)
            global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
            global_Canvas.image = render
        elif crop_start_x<crop_end_x and crop_start_y>crop_end_y:
            Cropped_Image = image.crop([crop_start_x - left, crop_end_y - up, crop_end_x - left, crop_start_y - up])
            image = Cropped_Image
            saving_Image = Cropped_Image
            left_right_space, up_down_space = image_Center(Cropped_Image)
            render = ImageTk.PhotoImage(Cropped_Image)
            global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
            global_Canvas.image = render
        elif crop_start_x>crop_end_x and crop_start_y>crop_end_y:
            Cropped_Image = image.crop([crop_end_x - left, crop_end_y - up, crop_start_x - left, crop_start_y - up])
            image = Cropped_Image
            saving_Image = Cropped_Image
            left_right_space, up_down_space = image_Center(Cropped_Image)
            render = ImageTk.PhotoImage(Cropped_Image)
            global_Canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
            global_Canvas.image = render
    except:
        pass

def draw_rectangle(event):
    global crop_area
    global crop_end_x
    global crop_end_y
    if crop_area:
        global_Canvas.delete(crop_area)
    crop_end_x = event.x
    crop_end_y = event.y
    #print(crop_start_x,crop_start_y,crop_end_x,crop_end_y)
    crop_area = global_Canvas.create_rectangle(crop_start_x, crop_start_y, crop_end_x, crop_end_y, width=1)

def Crop(canvas):
    canvas.bind("<Button-1>", start_crop)
    canvas.bind("<B1-Motion>",draw_rectangle)
    canvas.bind("<ButtonRelease-1>", end_crop)

def Auto_Enchancement(canvas):
    try:
        global saving_Image
        global image
        auto_Enhancement = ImageOps.equalize(image, mask = None)
        image = auto_Enhancement
        saving_Image = auto_Enhancement
        left_right_space, up_down_space = image_Center(auto_Enhancement)
        render = ImageTk.PhotoImage(auto_Enhancement)
        canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
        canvas.image = render
    except:
        print("Something is wrong!")


def sepia(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    except:
        pass
    image = cv2.transform(image, np.matrix([[0.393, 0.769, 0.189],
                                        [0.349, 0.686, 0.168],
                                        [0.272, 0.534, 0.131]]))
    image[np.where(image > 255)] = 255
    sepia_Filter = np.array(image, dtype=np.uint8)
    sepia_Filter = Image.fromarray(sepia_Filter)
    image = sepia_Filter
    saving_Image = sepia_Filter
    left_right_space, up_down_space = image_Center(sepia_Filter)
    render = ImageTk.PhotoImage(sepia_Filter)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def vintage(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    except:
        pass
    img = cv2.transform(image, np.matrix([[0.111, 0.534, 0.131],
                                        [0.349, 0.345, 0.168],
                                        [0.393, 0.111, 0.189]]))
    img[np.where(img > 255)] = 255
    vintage_Filter = np.array(img, dtype=np.uint8)
    vintage_Filter = Image.fromarray(vintage_Filter)
    image = vintage_Filter
    saving_Image = vintage_Filter
    left_right_space, up_down_space = image_Center(vintage_Filter)
    render = ImageTk.PhotoImage(vintage_Filter)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def griffin(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    col_img = cv2.bilateralFilter(image,5,255,255)
    grayscaled = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    grayscaled = cv2.medianBlur((grayscaled).astype(np.uint8),7)
    edges = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)
    griffin_Image = cv2.bitwise_and(col_img,col_img,mask=edges)
    griffin_Image = Image.fromarray((griffin_Image).astype(np.uint8))
    image = griffin_Image
    saving_Image = griffin_Image
    left_right_space, up_down_space = image_Center(griffin_Image)
    render = ImageTk.PhotoImage(griffin_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def pinkypie(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    except:
        pass
    img = cv2.transform(image, np.matrix([[0.543, 0.534, 0.123],
                                        [0.349, 0.345, 0.168],
                                        [0.645, 0.111, 0.189]]))
    img[np.where(img > 255)] = 255
    img = np.array(img, dtype=np.uint8)
    col_img = cv2.bilateralFilter(img, 5, 255, 255)
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscaled = cv2.medianBlur(grayscaled, 7)
    edges = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)
    pinkypie_Image = cv2.bitwise_and(col_img, col_img, mask=edges)
    pinkypie_Image = Image.fromarray(pinkypie_Image)
    image = pinkypie_Image
    saving_Image = pinkypie_Image
    left_right_space, up_down_space = image_Center(pinkypie_Image)
    render = ImageTk.PhotoImage(pinkypie_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def harpy(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    figure_size = 5
    gauss_image = cv2.GaussianBlur(image, (figure_size, figure_size),0)
    sobel_x=cv2.Sobel(gauss_image, cv2.CV_64F,1,0)
    sobel_x=np.uint8(np.absolute(sobel_x))

    sobel_y=cv2.Sobel(gauss_image, cv2.CV_64F,0,1)
    sobel_y=np.uint8(np.absolute(sobel_y))

    sobel_image=cv2.bitwise_or(sobel_x,sobel_y)
    sobel_image = Image.fromarray(sobel_image)
    image = sobel_image
    saving_Image = sobel_image
    left_right_space, up_down_space = image_Center(sobel_image)
    render = ImageTk.PhotoImage(sobel_image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def sobel_for_kitsune(image):
    image = np.array(image, dtype=np.float32)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    imgx= cv2.Sobel(image,cv2.CV_8U,0,1,ksize=3)
    imgy= cv2.Sobel(image,cv2.CV_8U,1,0,ksize=3)
    return cv2.bitwise_or(imgx,imgy)

def kitsune(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    frame = cv2.GaussianBlur(image, (3, 3), 0)
    negative_image = 255 - frame
    img0 = sobel_for_kitsune(frame)
    img1 = sobel_for_kitsune(negative_image)
    img2 = cv2.addWeighted(img0, 1, img1, 1, 0)  # different weights can be tried too
    # Invert the image back
    opImg = 255 - img2
    opImg = Image.fromarray(opImg)
    image = opImg
    saving_Image = opImg
    left_right_space, up_down_space = image_Center(opImg)
    render = ImageTk.PhotoImage(opImg)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def sobel_for_lemontree (image):
    image = cv2.cvtColor(np.float32(image), cv2.COLOR_RGB2HSV)
    imgx = cv2.Sobel(image, cv2.CV_8U, 0, 1, ksize=3)
    imgy = cv2.Sobel(image, cv2.CV_8U, 1, 0, ksize=3)
    return cv2.bitwise_or(imgx, imgy)

def lemontree(canvas):
    global saving_Image
    global image
    image = cv2.cvtColor(np.float32(image), cv2.COLOR_RGB2HSV)
    frame = cv2.GaussianBlur(image, (3, 3), 0)
    gray = 123 - frame

    img0= sobel_for_lemontree(frame)
    img1= sobel_for_lemontree(gray)
    img2= cv2.addWeighted(img0,1,img1,1,0)
    #Invert the image back
    opImg= 255-img2
    opImg = Image.fromarray(opImg)
    image = opImg
    saving_Image = opImg
    left_right_space, up_down_space = image_Center(opImg)
    render = ImageTk.PhotoImage(opImg)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def sobel_for_chimera (img):
    img = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2HSV)
    imgx= cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
    imgy= cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)

    return cv2.bitwise_or(imgx,imgy)

def chimera(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    frame = cv2.transform(image, np.matrix([[ 0.109,  0.286, 0.123],
                                        [ 0.349, 0.345, 0.976],
                                        [ 0.890, 0.223, 0.239]]))
    frame= cv2.GaussianBlur(frame,(3,3),0)
    gray= 123-frame

    img0= sobel_for_kitsune(frame)
    img1= sobel_for_kitsune(gray)
    img2= cv2.addWeighted(img0,1,img1,1,0)

    #Invert the image back
    opImg= 255-img2
    opImg = Image.fromarray(opImg)
    image = opImg
    saving_Image = opImg
    left_right_space, up_down_space = image_Center(opImg)
    render = ImageTk.PhotoImage(opImg)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def bergman(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    image = cv2.transform(image, np.matrix([[ 0.111,  0.111, 0.111],
                                        [ 0.111, 0.111, 0.111],
                                        [ 0.111, 0.111, 0.111]]))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
    morph = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # brighten dark regions
    bergman_Image = cv2.normalize(morph,None,20,255,cv2.NORM_MINMAX)
    bergman_Image = Image.fromarray((bergman_Image).astype(np.uint8))
    image = bergman_Image
    saving_Image = bergman_Image
    left_right_space, up_down_space = image_Center(bergman_Image)
    render = ImageTk.PhotoImage(bergman_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def bean(canvas):
    global saving_Image
    global image
    # edge detection filter
    image = np.array(image, dtype=np.float32)
    kernel = np.array([[0.0, -1.0, 0.0],
                       [-1.0, 4.0, -1.0],
                       [0.0, -1.0, 0.0]])
    kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)
    bean_Image = cv2.filter2D(image, -1, kernel)
    bean_Image = Image.fromarray((bean_Image).astype(np.uint8))
    image = bean_Image
    saving_Image = bean_Image
    left_right_space, up_down_space = image_Center(bean_Image)
    render = ImageTk.PhotoImage(bean_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def rainbow(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    lower_range = np.array([0, 0, 0])  # Set the Lower range value of color in BGR
    upper_range = np.array([140, 255, 255])  # Set the Upper range value of color in BGR

    mask = cv2.inRange(image, lower_range, upper_range)  # Create a mask with range
    img1 = cv2.bitwise_and(image, image, mask=mask)

    bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
    bw_bgr = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)  # Converting the Gray image to BGR format

    rainbow_Image = cv2.bitwise_or(bw_bgr, img1)
    rainbow_Image = Image.fromarray((rainbow_Image).astype(np.uint8))
    image = rainbow_Image
    saving_Image = rainbow_Image
    left_right_space, up_down_space = image_Center(rainbow_Image)
    render = ImageTk.PhotoImage(rainbow_Image)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def warhol(canvas,nsize=5):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    rows,cols,_ = image.shape
    dist = image.copy()
         #  , each small square is filled with random colors
    for y in range(233,rows,nsize):
        for x in range(0,cols,nsize):
            dist[y:y+nsize,x:x+nsize] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
    dist = Image.fromarray((dist).astype(np.uint8))
    image = dist
    saving_Image = dist
    left_right_space, up_down_space = image_Center(dist)
    render = ImageTk.PhotoImage(dist)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def phoenix(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    lower_range = np.array([0, 0, 0])
    upper_range = np.array([140, 255, 255])

    mask = cv2.inRange(image, lower_range, upper_range)
    img1 = cv2.bitwise_and(image, image, mask=mask)

    bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
    bw_bgr = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)  # Converting the Gray image to BGR format

    img2 = cv2.bitwise_or(bw_bgr, img1)
    blue, green, red = cv2.split(img2)
    red = red.astype(np.uint8)  # add
    zeros = np.zeros(blue.shape, np.uint8)
    redBGR = cv2.merge((red, zeros, zeros))
    #greenBGR = cv2.merge((zeros, green, zeros))
    #blueBGR = cv2.merge((zeros, zeros, blue))

    redBGR = Image.fromarray((redBGR).astype(np.uint8))
    image = redBGR
    saving_Image = redBGR
    left_right_space, up_down_space = image_Center(redBGR)
    render = ImageTk.PhotoImage(redBGR)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def popart(canvas):
    global saving_Image
    global image
    try:
        image = np.array(image, dtype=np.float32)
        grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # set colours (BGR)
        background_colour = [190, 456, 12]
        dots_colour = (153, 123, 217)

        # set the max dots (on the longest side of the image)
        max_dots = 100
        # extract dimensions
        original_image_height, original_image_width = grayscaled.shape

        # down size to number of dots
        if original_image_height == max(original_image_height, original_image_width):
            downsized_image = cv2.resize(image, (int(original_image_height * (max_dots / original_image_width)), max_dots))
        else:
            downsized_image = cv2.resize(image, (max_dots, int(original_image_height * (max_dots / original_image_width))))

        # extract dimensions of new image
        downsized_image_height, downsized_image_width,downsized_image_depth = downsized_image.shape

        # set how big we want our final image to be
        multiplier = 58

        # set the size of our blank canvas
        blank_img_height = downsized_image_height * multiplier
        blank_img_width = downsized_image_width * multiplier

        # set the padding value so the dots start in frame (rather than being off the edge
        padding = int(multiplier / 2)

        # create canvas containing just the background colour
        blank_image = np.full(((blank_img_height), (blank_img_width), 3), background_colour, dtype=np.uint8)

        # run through each pixel and draw the circle on our blank canvas
        print(downsized_image_height,downsized_image_width,"\t",downsized_image_depth)
        for y in range(0, downsized_image_height):
            for x in range(0, downsized_image_width):
                cv2.circle(blank_image, (((x * multiplier) + padding), ((y * multiplier) + padding)),int((0.6 * multiplier) * ((255 - np.vectorize(int(downsized_image[y][x]))) / 255)), dots_colour, -1)

        blank_image = Image.fromarray((blank_image).astype(np.uint8))
        image = blank_image
        saving_Image = blank_image
        left_right_space, up_down_space = image_Center(blank_image)
        render = ImageTk.PhotoImage(blank_image)
        canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
        canvas.image = render
    except:
        print("Something is wrong!")

def hsv(img, l, u):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([l,128,128]) # setting lower HSV value
    upper = np.array([u,255,255]) # setting upper HSV value
    mask = cv2.inRange(hsv, lower, upper) # generating mask
    return mask

def hippogriff(canvas):
    global saving_Image
    global image
    try:
        image = np.array(image, dtype=np.float32)
        res = np.zeros(image.shape, np.uint8) # creating blank mask for result
        l = 15 # the lower range of Hue we want
        u = 78 # the upper range of Hue we want
        mask = hsv(image, l, u)
        inv_mask = cv2.bitwise_not(mask) # inverting mask
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        res1 = cv2.bitwise_and(image, image, mask= mask) # region which has to be in color
        res2 = cv2.bitwise_and(gray, gray, mask= inv_mask) # region which has to be in grayscale
        for i in range(3):
            res[:, :, i] = res2 # storing grayscale mask to all three slices
        img = cv2.bitwise_or(res1, res) # joining grayscale and color region

        img = Image.fromarray((img).astype(np.uint8))
        image = img
        saving_Image = img
        left_right_space, up_down_space = image_Center(img)
        render = ImageTk.PhotoImage(img)
        canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
        canvas.image = render
    except:
        print("Something is wrong!")

def posterize(canvas):
    global saving_Image
    global image
    level=10
    indices = np.arange(0,256)
    divider = np.linspace(0,255,level+1)[1]
    quantiz = np.int0(np.linspace(0,255,level))
    color_levels = np.clip(np.int0(indices/divider),0,level-1)
    palette = quantiz[color_levels]
    img2 = palette[image]
    img2 = cv2.convertScaleAbs(img2)

    img2 = Image.fromarray(img2)
    image = img2
    saving_Image = img2
    left_right_space, up_down_space = image_Center(img2)
    render = ImageTk.PhotoImage(img2)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def bug(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    lower_range = np.array([0, 0, 0])
    upper_range = np.array([140, 255, 255])

    mask = cv2.inRange(image, lower_range, upper_range)
    img1 = cv2.bitwise_and(image, image, mask=mask)

    bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
    bw_bgr = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)  # Converting the Gray image to BGR format

    img2 = cv2.bitwise_or(bw_bgr, img1)
    blue, green, red = cv2.split(img2)
    green = blue.astype(np.uint8)  # add
    zeros = np.zeros(blue.shape, np.uint8)
    #redBGR = cv2.merge((red, zeros, zeros))
    greenBGR = cv2.merge((zeros, green, zeros))
    #blueBGR = cv2.merge((zeros, zeros, blue))
    greenBGR = Image.fromarray((greenBGR).astype(np.uint8))
    image = greenBGR
    saving_Image = greenBGR
    left_right_space, up_down_space = image_Center(greenBGR)
    render = ImageTk.PhotoImage(greenBGR)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render


def ocean(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    lower_range = np.array([0, 0, 0])
    upper_range = np.array([140, 255, 255])

    mask = cv2.inRange(image, lower_range, upper_range)
    img1 = cv2.bitwise_and(image, image, mask=mask)

    bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
    bw_bgr = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)  # Converting the Gray image to BGR format

    img2 = cv2.bitwise_or(bw_bgr, img1)
    blue, green, red = cv2.split(img2)
    blue = blue.astype(np.uint8)
    zeros = np.zeros(blue.shape, np.uint8)
    #redBGR = cv2.merge((red, zeros, zeros))
    #greenBGR = cv2.merge((zeros, green, zeros))
    blueBGR = cv2.merge((zeros, zeros, blue))

    blueBGR = Image.fromarray((blueBGR).astype(np.uint8))
    image = blueBGR
    saving_Image = blueBGR
    left_right_space, up_down_space = image_Center(blueBGR)
    render = ImageTk.PhotoImage(blueBGR)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def Shine(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    except:
        pass
    #image = cv2.transform(image, np.matrix([[0.393, 0.769, 0.189],[0.349, 0.686, 0.168],[0.272, 0.534, 0.131]]))
    image = cv2.transform(image, np.matrix([[0.711, 0.732, 0.198],
                                            [0.867, 0.542, 0.435],
                                            [0.453, 0.786, 0.237]]))
    image[np.where(image > 255)] = 255
    sepia_Filter = np.array(image, dtype=np.uint8)
    sepia_Filter = Image.fromarray(sepia_Filter)
    image = sepia_Filter
    saving_Image = sepia_Filter
    left_right_space, up_down_space = image_Center(sepia_Filter)
    render = ImageTk.PhotoImage(sepia_Filter)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render

def Nostalgic(canvas):
    global saving_Image
    global image
    image = np.array(image, dtype=np.float32)
    try:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    except:
        pass
    image = cv2.transform(image, np.matrix([[0.19, 0.159, 0.12],
                                        [0.421, 0.213, 0.241],
                                        [0.551, 0.245, 0.131]]))
    image[np.where(image > 255)] = 255
    sepia_Filter = np.array(image, dtype=np.uint8)
    sepia_Filter = Image.fromarray(sepia_Filter)
    image = sepia_Filter
    saving_Image = sepia_Filter
    left_right_space, up_down_space = image_Center(sepia_Filter)
    render = ImageTk.PhotoImage(sepia_Filter)
    canvas.create_image(left_right_space, up_down_space, image=render, anchor=tk.NW)
    canvas.image = render