import tkinter as tk
import Functions as functions
from PIL import Image, ImageTk, ImageFilter

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.configure(background='black')# Windows background is black
window.title("Image Editor")
IconPhoto = tk.PhotoImage(file="VenusaurIcon.png")# Icon Image uploaded
window.iconphoto(False, IconPhoto)# Icon Image changed
window_width=800 # Window width
window_height=600 # Window height
window.geometry(f'{window_width}x{window_height}') # Window screen

photoimage = IconPhoto.subsample(2, 3)
editor_image = tk.Label(image=photoimage)
editor_image.place(x=30, y=0)

editor_name = tk.Label(window, text="Venusaur Image Editor",bg='black',fg='white',font = "Verdana 20 bold")
editor_name.place(x=250,y=0)

selectImage_Button = tk.Button(window,text ="Select",padx=20,pady=10,bg='black',fg='white',command=lambda:functions.selected_image(image_Canvas))
selectImage_Button.place(x=713, y=48) # Select Image Button

saveImage_Button = tk.Button(window,text ="Save",padx=20,pady=10,bg='black',fg='white',command=lambda : functions.save(image_Canvas))
saveImage_Button.place(x=713, y=110)# Save Image Button

saveAsImage_Button = tk.Button(window,text ="Save As",padx=15,pady=7,bg='black',fg='white',command=lambda :functions.save_As(image_Canvas))
saveAsImage_Button.place(x=713, y=176)# Save Image Button

exit_Button = tk.Button(window,text ="Exit",padx=20,pady=10,bg='black',fg='white',command=lambda: functions.exit_Button_Script(window))
exit_Button.place(x=713, y=310) # Exit Image Editor

cancel_Button = tk.Button(window,text ="Cancel",padx=20,pady=10,bg='black',fg='white',command=lambda: functions.cancel_Changing(image_Canvas))
cancel_Button.place(x=713, y=240) # Exit Image Editor

Transform_Button = tk.Button(window,text ="Transform",padx=10,pady=5,bg='black',fg='white',activebackground='white',command=lambda: Transform_Buttons())
Transform_Button.place(x=5, y=100) # Transform Image Editor

Tone_Button = tk.Button(window,text ="Tone",padx=10,pady=5,bg='black',fg='white',command=lambda:Tone_Buttons())
Tone_Button.place(x=5, y=170) # Tone Image Editor

Enhancement_Button = tk.Button(window,text ="Automatic\nEnhancement",padx=0,pady=0,bg='black',fg='white',command=lambda :functions.Auto_Enchancement(image_Canvas))
Enhancement_Button.place(x=5, y=240) # Automatic Enhancement Image Editor

Filter_Button = tk.Button(window,text ="Filter",padx=10,pady=5,bg='black',fg='white',command=lambda:Filter_Buttons())
Filter_Button.place(x=5, y=320) # Filter Image Editor

Effect_Button = tk.Button(window,text ="Effect",padx=10,pady=5,bg='black',fg='white',command=lambda:Effect_Buttons())
Effect_Button.place(x=5, y=390) # Effect Image Editor


Rotate_Button = tk.Button(window, text="Rotate", padx=10, pady=5, bg='black', fg='white',command=lambda:functions.Rotate(image_Canvas))#Transform Buttons
Mirror_Button = tk.Button(window, text="Mirror", padx=10, pady=5, bg='black', fg='white',command=lambda :functions.Flip(image_Canvas))
Crop_Button = tk.Button(window, text="Crop", padx=10, pady=5, bg='black', fg='white',command=lambda:functions.Crop(image_Canvas))

Brightness_Button = tk.Button(window, text="Brightness", padx=6, pady=3, bg='black', fg='white',command=lambda :Brightness_Scale())#Tone Buttons
brightnessScale = tk.Scale(window, from_=-1, to=8, orient=tk.HORIZONTAL,
                               length=400, resolution=0.1, bg='black', fg='white', command=functions.Brightness)
Contrast_Button = tk.Button(window, text="Contrast", padx=6, pady=3, bg='black', fg='white',command=lambda :Contrast_Scale())
contrastScale = tk.Scale(window, from_=-1, to=8, orient=tk.HORIZONTAL,
                        length=400, resolution=0.1, bg='black', fg='white', command=functions.Contrast)
Sharpness_Button = tk.Button(window, text="Sharpness", padx=6, pady=3, bg='black', fg='white',command=lambda:Sharpness_Scale() )
sharpnessScale = tk.Scale(window, from_=-10, to=10, orient=tk.HORIZONTAL,
                               length=400, resolution=0.1, bg='black', fg='white', command=functions.Sharpness)

Filter1_Button = tk.Button(window, text="Sepia", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.sepia(image_Canvas))#Filter Buttons
Filter2_Button = tk.Button(window, text="Vintage", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.vintage(image_Canvas))
Filter3_Button = tk.Button(window, text="Griffin", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.griffin(image_Canvas))
Filter4_Button = tk.Button(window, text="Pinkypie", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.pinkypie(image_Canvas))
Filter5_Button = tk.Button(window, text="Harpy", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.harpy(image_Canvas))
Filter6_Button = tk.Button(window, text="Kitsune", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.kitsune(image_Canvas))
Filter7_Button = tk.Button(window, text="Lemontree", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.lemontree(image_Canvas))
Filter8_Button = tk.Button(window, text="Chimera", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.chimera(image_Canvas))
Filter9_Button = tk.Button(window, text="Bergman", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.bergman(image_Canvas))
Filter10_Button = tk.Button(window, text="Bean", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.bean(image_Canvas))

Effect1_Button = tk.Button(window, text="Rainbow", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.rainbow(image_Canvas))
Effect2_Button = tk.Button(window, text="Warhol", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.warhol(image_Canvas))
Effect3_Button = tk.Button(window, text="Phoenix", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.phoenix(image_Canvas))
Effect4_Button = tk.Button(window, text="Popart", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.popart(image_Canvas))
Effect5_Button = tk.Button(window, text="Hippogriff", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.hippogriff(image_Canvas))
Effect6_Button = tk.Button(window, text="Posterize", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.posterize(image_Canvas))
Effect7_Button = tk.Button(window, text="Bug", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.bug(image_Canvas))
Effect8_Button = tk.Button(window, text="Ocean", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.ocean(image_Canvas))
Effect9_Button = tk.Button(window, text="Shine", padx=6, pady=3, bg='black', fg='white',command=lambda :functions.Shine(image_Canvas))
Effect10_Button = tk.Button(window, text="Nostalgic",padx=6, pady=3, bg='black', fg='white',command=lambda :functions.Nostalgic(image_Canvas))


def Transform_Buttons():
    Crop_Button.place(x=120, y=240)  # Crop Image Editor
    Mirror_Button.place(x=120, y=170)  # Mirror Image Editor
    Rotate_Button.place(x=120, y=100)  # Rotate Image Editor
    Brightness_Button.place_forget()
    Contrast_Button.place_forget()
    Sharpness_Button.place_forget()
    Filter1_Button.place_forget()
    Filter2_Button.place_forget()
    Filter3_Button.place_forget()
    Filter4_Button.place_forget()
    Filter5_Button.place_forget()
    Filter6_Button.place_forget()
    Filter7_Button.place_forget()
    Filter8_Button.place_forget()
    Filter9_Button.place_forget()
    Filter10_Button.place_forget()

    Effect1_Button.place_forget()
    Effect2_Button.place_forget()
    Effect3_Button.place_forget()
    Effect4_Button.place_forget()
    Effect5_Button.place_forget()
    Effect6_Button.place_forget()
    Effect7_Button.place_forget()
    Effect8_Button.place_forget()
    Effect9_Button.place_forget()
    Effect10_Button.place_forget()
    brightnessScale.place_forget()
    contrastScale.place_forget()
    sharpnessScale.place_forget()
def Tone_Buttons():
    Brightness_Button.place(x=110, y=100)
    Contrast_Button.place(x=110, y=170)
    Sharpness_Button.place(x=110, y=240)
    Crop_Button.place_forget()
    Mirror_Button.place_forget()
    Rotate_Button.place_forget()
    Filter1_Button.place_forget()
    Filter2_Button.place_forget()
    Filter3_Button.place_forget()
    Filter4_Button.place_forget()
    Filter5_Button.place_forget()
    Filter6_Button.place_forget()
    Filter7_Button.place_forget()
    Filter8_Button.place_forget()
    Filter9_Button.place_forget()
    Filter10_Button.place_forget()
    Effect1_Button.place_forget()
    Effect2_Button.place_forget()
    Effect3_Button.place_forget()
    Effect4_Button.place_forget()
    Effect5_Button.place_forget()
    Effect6_Button.place_forget()
    Effect7_Button.place_forget()
    Effect8_Button.place_forget()
    Effect9_Button.place_forget()
    Effect10_Button.place_forget()

    brightnessScale.place_forget()
    contrastScale.place_forget()
    sharpnessScale.place_forget()

def Filter_Buttons():
    Filter1_Button.place(x=110, y=100)
    Filter2_Button.place(x=110, y=148)
    Filter3_Button.place(x=110, y=197)
    Filter4_Button.place(x=110, y=245)
    Filter5_Button.place(x=110, y=294)
    Filter6_Button.place(x=110, y=342)
    Filter7_Button.place(x=110, y=391)
    Filter8_Button.place(x=110, y=439)
    Filter9_Button.place(x=110, y=487)
    Filter10_Button.place(x=110, y=535)
    Crop_Button.place_forget()
    Mirror_Button.place_forget()
    Rotate_Button.place_forget()
    Brightness_Button.place_forget()
    Contrast_Button.place_forget()
    Sharpness_Button.place_forget()
    Effect1_Button.place_forget()
    Effect2_Button.place_forget()
    Effect3_Button.place_forget()
    Effect4_Button.place_forget()
    Effect5_Button.place_forget()
    Effect6_Button.place_forget()
    Effect7_Button.place_forget()
    Effect8_Button.place_forget()
    Effect9_Button.place_forget()
    Effect10_Button.place_forget()
    brightnessScale.place_forget()
    contrastScale.place_forget()
    sharpnessScale.place_forget()

def Effect_Buttons():
    Effect1_Button.place(x=110, y=100)
    Effect2_Button.place(x=110, y=148)
    Effect3_Button.place(x=110, y=197)
    Effect4_Button.place(x=110, y=245)
    Effect5_Button.place(x=110, y=294)
    Effect6_Button.place(x=110, y=342)
    Effect7_Button.place(x=110, y=391)
    Effect8_Button.place(x=110, y=439)
    Effect9_Button.place(x=110, y=487)
    Effect10_Button.place(x=110, y=535)
    Crop_Button.place_forget()
    Mirror_Button.place_forget()
    Rotate_Button.place_forget()
    Brightness_Button.place_forget()
    Contrast_Button.place_forget()
    Sharpness_Button.place_forget()
    Filter1_Button.place_forget()
    Filter2_Button.place_forget()
    Filter3_Button.place_forget()
    Filter4_Button.place_forget()
    Filter5_Button.place_forget()
    Filter6_Button.place_forget()
    Filter7_Button.place_forget()
    Filter8_Button.place_forget()
    Filter9_Button.place_forget()
    Filter10_Button.place_forget()
    brightnessScale.place_forget()
    contrastScale.place_forget()
    sharpnessScale.place_forget()

def Brightness_Scale():
    brightnessScale.place(x=189, y=557)
    contrastScale.place_forget()
    sharpnessScale.place_forget()

def Contrast_Scale():
    contrastScale.place(x=189, y=557)
    brightnessScale.place_forget()
    sharpnessScale.place_forget()

def Sharpness_Scale():
    sharpnessScale.place(x=189, y=557)
    brightnessScale.place_forget()
    contrastScale.place_forget()

#label = tk.Label(window, text="\u2192",bg='black',fg='white')
#label.config(font=("Courier", 27))
#label.place(x=87,y=80)

image_Canvas = tk.Canvas(width=500, height=500,bg='black')
image_Canvas.place(x=190,y=50)

#original_Image = functions.keep()

#Brightness(Frame2)
#Contrast(Frame2)

tk.mainloop()