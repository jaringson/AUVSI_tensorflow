from PIL import Image
from random import randint
import os
import numpy as np
from scipy.misc import imread, imresize, imsave, imshow
import math

alpha  = ['a','b','c','d','e','f','g','h','i','j',
         'k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z',
         '0','1','2','3','4','5','6','7','8','9']
pre = 'shapes/'
post = '.png'

brown = (163, 76, 0, 255)
grey = (160, 160, 160, 255)
red = (255, 0, 0, 255)
green = (0, 204, 0, 255)
blue = (0, 0, 255, 255)
yellow = (255, 255, 0, 255)
orange = (255, 128, 0, 255)
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
purple = (204, 0, 204, 255)

colors = [brown, grey, red, green, blue, yellow, orange, white, black, purple]
shapes = ['star','cross','triangle','square','circle','halfcircle','rectangle','quarter_circle', 'trapezoid', 'pentagon','hexagon', 'heptagon', 'octagon']


def get_target():
    letter_ind = randint(0, len(alpha) - 1)
    letter = alpha[letter_ind]

    image = pre + letter + post

    shape_color_ind =  randint(0, len(colors) - 1)
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
    shape_c_one_hot = np.zeros(len(colors))
    shape_c_one_hot.put(shape_color_ind,1)

    letter_c_one_hot = np.zeros(len(colors))
    letter_c_one_hot.put(letter_color_ind,1)

    shape_one_hot = np.zeros(len(shapes))
    shape_one_hot.put(shape_ind,1)

    letter_one_hot = np.zeros(len(alpha))
    letter_one_hot.put(letter_ind,1)

    return target, shape_c_one_hot, letter_c_one_hot, shape_one_hot, letter_one_hot


def place_background(from_center, rotate, scale_rand):
    grass_dir = './grass/'
    target,sc,lc,s,l = get_target()
    num = randint(1,84)
    pre = ''
    if num <= 9:
        pre = '00'
    else:
        pre = '0'

    background = Image.open(grass_dir + pre + str(num) + '.png')

    b_w, b_h = background.size

    delta_x = randint(0,b_w-224)
    delta_y = randint(0,b_h-224)
    background = background.crop((delta_x, delta_y, delta_x + 224, delta_y + 224))

    b_w, b_h = background.size

    datas = target.getdata()

    newData = []
    for item in datas:
        if item[3] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    target.putdata(newData)

    foregrounds = []

    target_r = target
    p_deg = 0
    if rotate:
        p_deg = randint(0,360)
        target_r = target.rotate(p_deg, expand=True)

    if scale_rand:
        p_size = randint(18,24)
    else:
        p_size = 18
    p_scale = 1.0*p_size/b_w
    target_r = target_r.resize((p_size,p_size), Image.ANTIALIAS)

    t_w,t_h = target_r.size
    foregrounds.append(target_r)
    target = target.convert("RGB")

    for foreground in foregrounds:

        p_w = randint(int(from_center * (b_w//2 - t_w//2)),int((b_w-t_w) - from_center * ((b_w-t_w) - ((b_w//2) - t_w//2))))
        p_h = randint(int(from_center * (b_h//2 - t_h//2)),int((b_h-t_h) - from_center * ((b_h-t_h) - ((b_h//2) - t_h//2))))
        #p_w = 30
        #p_h = 20
        background.paste(foreground, (p_w,p_h), foreground)


    #background.show()
    #print p_w, p_h
    return background, p_deg, p_h + t_h/2 - b_h/2, p_w + t_w/2 - b_w/2, p_scale, sc, lc, s, l, target

def next_batch(size, from_center = 0, rotate = True, scale_rand = True):
	if from_center > 1:
		from_center = 1
	if from_center < 0:
		from_center = 0

	output = []
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	for _ in range(size):

		img, p_deg, p_h, p_w, p_scale, shape_color, letter_color, shape, letter, target = place_background(from_center, rotate, scale_rand)

		# target.show()

		img = np.array(img).flatten()
		list_of_lists = img.tolist()

		one = math.cos(math.radians(p_deg)) + 1 + p_scale
		two = -math.sin(math.radians(p_deg))
		three = p_w
		four = math.sin(math.radians(p_deg))
		five = math.cos(math.radians(p_deg)) + 1 + p_scale
		six = p_h

		output[0].append(list_of_lists)
		output[1].append(letter)
		output[2].append(shape)
		output[3].append(letter_color)
		output[4].append(shape_color)
		output[5].append([p_w, p_h, p_scale])
		output[6].append(target)

	#print output[1]
	return output


def next_target_batch(size):

    output = []
    output.append([])
    output.append([])
    output.append([])
    output.append([])
    output.append([])
    for i in range(size):
        target, shape_color, letter_color, shape, letter = get_target()
        target = target.resize((24, 24))

        datas = target.getdata()

        newData = []
        for item in datas:
            if item[3] <= 3:
                newData.append((randint(0,100), randint(50,150), randint(0,50), 0))
            else:
                newData.append(item)
        target.putdata(newData)

        target = np.array(target)[:,:,0:3] + 30*np.random.rand(24,24,3)
        # imshow(target)
        target = target.flatten()

        list_of_lists = target.tolist()

        output[0].append(list_of_lists)
        output[1].append(letter)
        output[2].append(shape)
        output[3].append(letter_color)
        output[4].append(shape_color)

    return output


if __name__ == '__main__':
    b = next_batch(5,1,True)
    for i in range(5):
        im = np.array(b[0][i])
        im = im.reshape([143,256,3])
        imsave('./tf_logs/'+str(i)+'.png',im)
