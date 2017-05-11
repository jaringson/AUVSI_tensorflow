from PIL import Image
from random import randint
from scipy.misc import imrotate
import os, random
import shape_letter_image as sli


#grass_dir = '/tf_files/spatial-transformer-tensorflow/grass/'
grass_dir = './grass/'



def run():

	img,sc,lc,s,l = sli.get_image()

	all_back = ['s_grass_0.jpg','s_grass_1.jpg','s_grass_2.jpg','s_grass_3.jpg']
	all_back = ['comp_field_1.jpg']
	#pre = '/tf_files/spatial-transformer-tensorflow/'
	pre = './'

	#background = Image.open(pre + all_back[randint(0,len(all_back)-1)])
	#background = Image.open(pre+'white.jpg')

	num = random.randint(1,84)
	pre = ''
	if num <= 9:
		pre = '00'
	else:
		pre = '0'

	background = Image.open(grass_dir + pre + str(num) + '.png')

	width, height = background.size
	#print width, height


	#image = pre + 'e.jpg'
	# img = Image.open(image)
	#p_scale = randint(5,10) * 4
	p_scale = 120
	#print p_scale
	img = img.resize((p_scale,p_scale), Image.ANTIALIAS)
	p_scale = p_scale / 40.
	#print p_scale
	#w,h = img.size
	#print w,h
	img = img.convert("RGBA")
	datas = img.getdata()

	newData = []
	for item in datas:
	    if item[3] == 0:
	        newData.append((255, 255, 255, 0))
	    else:
	        newData.append(item)

	img.putdata(newData)

	foregrounds = []

	# for i in range(0,5, 1):
	#     foregrounds.append(image.rotate(randint(0,360)))

	p_deg = randint(0,360)
	#p_deg = 0
	img = img.rotate(p_deg, expand=True)
	w,h = img.size
	foregrounds.append(img)


	for foreground in foregrounds:
		p_w = randint(20,width-w)//4
		p_h = randint(20,height-h)//4
		#p_w = 30
		#p_h = 20
		background.paste(foreground, (p_w,p_h), foreground)


	# background.show()
	#print p_w, p_h
	return background, p_deg, p_h, p_w, p_scale, sc, lc, s, l

	# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
