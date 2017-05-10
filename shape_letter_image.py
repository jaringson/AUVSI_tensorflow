from PIL import Image
from random import randint
import os
import numpy as np
from scipy.misc import imread, imresize, imsave, imshow

alpha  = ['a','b','c','d','e','f','g','h','i','j',
         'k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z',
         '0','1','2','3','4','5','6','7','8','9']
pre = 'shapes/'
post = '.png'

red = (255, 0, 0, 255)
green = (0, 204, 0, 255)
blue = (0, 0, 255, 255)
yellow = (255, 255, 0, 255)
orange = (255, 128, 0, 255)
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
purple = (204, 0, 204, 255)

colors = [red, green, blue, yellow, orange, white, black, purple]
shapes = ['star','cross','triangle','square','circle','halfcircle','dimond','rectangle']


def get_image():
    letter_ind = randint(0, len(alpha) - 1)
    letter = alpha[letter_ind]

    image = pre + letter + post

    shape_color_ind = randint(0, len(colors) - 1)
    shape_color = colors[shape_color_ind]
    letter_color_ind = shape_color_ind
    letter_color = shape_color
    while letter_color == shape_color:
        letter_color_ind = randint(0, len(colors) - 1)
        letter_color = colors[letter_color_ind]

    shape_ind = randint(0,len(shapes)-1)
    shape = shapes[shape_ind]
    target = Image.open(pre + shape + post)

    width, height = target.size

    target = target.convert("RGBA")
    datas = target.getdata()

    newData = []
    for item in datas:
        if item[3] <= 3:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(shape_color)

    target.putdata(newData)

    img = Image.open(image)
    w,h = img.size
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[3] <= 3:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(letter_color)

    img.putdata(newData)

    foregrounds = []
    foregrounds.append(img)
    
    for foreground in foregrounds:
        target.paste(foreground, (width//2 - w//2, height//2 - h//2), foreground)

    # target.show()
    shape_c_one_hot = np.zeros(8)
    shape_c_one_hot.put(shape_color_ind,1)

    letter_c_one_hot = np.zeros(8)
    letter_c_one_hot.put(letter_color_ind,1)

    shape_one_hot = np.zeros(8)
    shape_one_hot.put(shape_ind,1)

    letter_one_hot = np.zeros(36)
    letter_one_hot.put(letter_ind,1)

    return target, shape_c_one_hot, letter_c_one_hot, shape_one_hot, letter_one_hot

def next_target_batch(size):

    output = []
    output.append([])
    output.append([])
    output.append([])
    output.append([])
    output.append([])
    for i in range(size):
        img, shape_color, letter_color, shape, letter = get_image()
        img = img.resize((24, 24), Image.ANTIALIAS)
        img = np.array(img)[:,:,0:3] + 30*np.random.rand(24,24,3)
        # imshow(img)
        img = img.flatten()

        list_of_lists = img.tolist()

        output[0].append(list_of_lists)
        output[1].append(letter)
        output[2].append(shape)
        output[3].append(letter_color)
        output[4].append(shape_color)

    return output
