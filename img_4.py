import os
import glob
from PIL import Image , ImageOps
import pyprind
import numpy as np
from numpy import asarray


data_list = []
tagrt_list = []
width_img, height_img = 200,200

# Seve Image
def save(object_img,name,tagrt):
    object_img.save(name)
    o = object_img.resize((width_img, height_img), Image.ANTIALIAS)
    data_list.append(asarray(o))
    tagrt_list.append(list_path.index(tagrt))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Image Translations
def Image_Original(img):
    Imag = img.copy()
    Imag.filename = img.filename.split('.')[0]+"_Original."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_left_top(img):
    width, height = img.size

    left = 0
    right = width *(6/8)
    top = 0
    bottom = height *(6/8)
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_left_top."+img.filename.split('.')[-1]
    return Imag
    

def Image_Translations_left_bottom(img):
    width, height = img.size

    left = 0
    right = width *(6/8)
    top = height*(2/8)
    bottom = height 
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_left_bottom."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_right_top(img):
    width, height = img.size

    left = width*(2/8)
    right = width 
    top = 0
    bottom = height *(6/8)
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_right_top."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_right_bottom(img):
    width, height = img.size

    left = width*(2/8)
    right = width 
    top = height*(2/8)
    bottom = height 
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_right_bottom."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_top(img):
    width, height = img.size

    left = width *(1/8)
    right = width *(7/8)
    top = 0
    bottom = height *(6/8)
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_top."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_bottom(img):
    width, height = img.size

    left = width *(1/8)
    right = width *(7/8)
    top = height *(2/8)
    bottom = height
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_bottom."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_left(img):
    width, height = img.size

    left = 0
    right = width *(6/8)
    top = height *(1/8)
    bottom = height *(7/8)
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_left."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_right(img):
    width, height = img.size

    left = width *(2/8)
    right = width 
    top = height *(1/8)
    bottom = height *(7/8)
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_right."+img.filename.split('.')[-1]
    return Imag

def Image_Translations_center(img):
    width, height = img.size

    left = width *(1/8)
    right = width *(7/8)
    top = height *(1/8)
    bottom = height *(7/8)
    Imag = img.crop((left, top, right, bottom))
    Imag.filename = img.filename.split('.')[0]+"_Translations_center."+img.filename.split('.')[-1]
    return Imag

#
def sum_function_of_Translations(img,list_Translations):
    if len(list_Translations) != 10:
        raise Exception("Sorry, len of list_Translations must be equal to 10")
    arr_Translations =[]
    num = 0
    if list_Translations[num]:
        arr_Translations.append(Image_Original(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_left_top(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_left_bottom(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_right_top(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_right_bottom(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_top(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_bottom(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_left(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_right(img))
    num+=1
    if list_Translations[num]:
        arr_Translations.append(Image_Translations_center(img))
        
    return arr_Translations

#----------------------------------------------------------------------

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Image Original


def Original_Flip_Image(img,tagrt,name):
    global path_output
    i_1 = path_output+"\\"+tagrt+"\\"+str(name).split('.')[0]+"_Original_Image."+str(name).split('.')[1]

    i_2 = path_output+"\\"+tagrt+"\\"+str(name).split('.')[0]+"_Flip_Original_Image."+str(name).split('.')[1]
    Flip     = ImageOps.mirror(img)
    save(object_img=Flip,name=i_2,tagrt=tagrt)
    save(object_img=img,name=i_1,tagrt=tagrt)
#----------------------------------------------------------------------

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Image Rotation


def Rotate_Flip_Image(img,tagrt,name,degrees):
    global path_output
    i_1 = path_output+"\\"+tagrt+"\\"+str(name).split('.')[0]+"_Rotate_Image_"+str(degrees)+'_degrees.'+str(name).split('.')[1]
    i_2 = path_output+"\\"+tagrt+"\\"+str(name).split('.')[0]+"_Flip_Rotate_Image_"+str(degrees)+'_degrees.'+str(name).split('.')[1]
    
    Rotate      = img.rotate(degrees, expand=True)
    Flip_Rotate = ImageOps.mirror(img.rotate(degrees, expand=True))
    save(object_img=Rotate,name=i_1,tagrt=tagrt)
    save(object_img=Flip_Rotate,name=i_2,tagrt=tagrt)
#----------------------------------------------------------------------


path_input = r"C:\Users\PON\Documents\Tensorflow_and_Keras\DATA\pp"
path_output = r"C:\Users\PON\Documents\Tensorflow_and_Keras\DATA"
path_output_numpy = path_output+"\\numpy_"+path_input.split("\\")[-1]
path_output += "\\new_"+path_input.split("\\")[-1]

path = "/*"
list_path = os.listdir(path_input)
try:
    os.mkdir(path_output)
except:
    print("path image builded")
try:
    os.mkdir(path_output_numpy)
except:
    print("path numpy builded")

"""
mote = input("Rotate s = std | m = mannul | a = all :")
if ('s' in mote) or ('S' in mote):
    list_degrees = [10,20,30,45,60,70,80,90,100,120,135,150,170,180,190,200,225,240,250,260,270,280,290,315,330,340,350]
    print("std = " ,list_degrees )
elif ('a' in mote) or ('A' in mote):
    list_degrees = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358]
    print("all = " ,list_degrees )
else:
    print("Ex degrees Rotate : 2,2.3,0.25,3 ")
    k = input("input degrees Rotate : ")
    list_degrees =k.split(',')
"""
# degrees Rotation
list_degrees = [10,20,30,45,60,70,80,90,100,120,135,150,170,180,190,200,225,240,250,260,270,280,290,315,330,340,350]
list_Translations = (1,1,1,1,1,1,1,1,1,1) 
    
if len(list_Translations) != 10:
    raise Exception("Sorry, len of list_Translations must be equal to 10")
for i in range(len( list_Translations )):
    j = list_Translations[i]
    if not(j == 0 or j == 1):
        
        s ="Sorry, valu of list_Translations must be equal to 1 or 0 , index %d == %s"%(i,j)
        raise Exception(s)    

img_len_taget=[]
img_total=0
for i in list_path :
    j = len(glob.glob(path_input+"\\"+i+path))
    img_total+=j
    img_len_taget.append(j)
    print("Data in ",i,j)

limit_img = (min(img_len_taget))*(2*((len(list_degrees)*sum(list_Translations))+sum(list_Translations)))

print('limit img = ' ,limit_img)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Image dir mk
try:
    os.mkdir(path_output)
except:
    print("Folder not building")
if not os.listdir(path_output):
    for i in list_path:
        os.mkdir(path_output+"\\"+i)
else:
    print("Folder not making dir in size")
#----------------------------------------------------------------------
dict_img = {}
bar = pyprind.ProgBar(img_total)
# Load Image
for i in list_path:
    arr_img = []
    j = path_input+"\\"+i+path
    
    for filename in glob.glob(j):
        bar.update()
        myImage = Image.open(filename)
        arr_img.extend(sum_function_of_Translations(img=myImage,list_Translations=list_Translations))
    
    dict_img[i]=arr_img


count = {}
for i in list_path:
    count[i]=0
    bar = pyprind.ProgBar(limit_img)
    for img in dict_img[i]:
        bar.update()
        bar.update()
        name = img.filename.split("\\")[-1]
        Original_Flip_Image(img=img,tagrt=i,name=name)
        count[i]+=2
        
    for degrees in list_degrees:
        if not (count[i] >= limit_img):
            for img in dict_img[i]:
                if not (count[i] >= limit_img):
                    name = img.filename.split("\\")[-1]
                    Rotate_Flip_Image(img=img,tagrt=i,name=name,degrees=degrees)
                    count[i]+=2
                bar.update()
                bar.update()

# Seve Data as numpy
np.save(path_output_numpy+'/data.npy', np.array(data_list))
np.save(path_output_numpy+'/tagrt.npy', np.array(tagrt_list))
np.save(path_output_numpy+'/tagrt_name.npy', np.array(list_path))