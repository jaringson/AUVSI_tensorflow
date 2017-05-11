#!/usr/bin/env python
'''from tensorflow.python.platform import gfile
from tensorflow.python.util import compat

import re
import hashlib'''


from numpy import array
from PIL import Image
#import cv2
import os
import random
#import tensorflow as tf
import insert_onto_image
import math

#image_dir = '/tf_files/spatial-transformer-tensorflow/targets/'
# image_dir = './targets/'

LABELS = {}
IMAGES = {}


# sub_dirs = os.listdir(image_dir)

# idx = 0
# for r in sub_dirs:
# 	#print os.listdir(os.path.join(image_dir, r))
# 	temp = [0] * (len(sub_dirs) -1)
# 	#temp = [0] * 9
# 	temp.insert(idx, 1)
# 	LABELS[r] = {}
# 	LABELS[r]['id'] = temp
# 	LABELS[r]['tot_num'] = len([name for name in os.listdir(os.path.join(image_dir, r)) ]) - 1
# 	idx = idx + 1

#print LABELS



def next_batch(size):
	#size = 10
	output = []
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	output.append([])
	for _ in range(size):
		# label_num = random.randrange(len(LABELS))
		# label = list(LABELS.keys())[label_num]
		# image_num = random.randrange(LABELS[label]['tot_num'])
		# image = image_dir + label + "/" + label + '_' + str(random.randint(0,2)) + ".jpg"
		#image = '/tf_files/spatial-transformer-tensorflow/black_square.jpg'
		#image = './black_square.jpg'


		img, p_deg, p_h, p_w, p_scale, shape_color, letter_color, shape, letter = insert_onto_image.run()

		#img = img.convert('L')
		img = img.resize((256, 143), Image.ANTIALIAS)
		img = array(img).flatten()

		list_of_lists = img.tolist()
		#output[0].append(re_image)
		#output[1].append(LABELS[label]['id'])


		try:
			#flattened = [val for sublist in list_of_lists for val in sublist]
			#flattened = [val for sublist in flattened for val in sublist]

			#print flattened


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
			output[5].append([three, six, p_deg])
			#output[1].append([one,two,three,four,five,six])
			#output[1].append(LABELS[label]['id'])
		except:
			x = 1




	#print output[1]
	return output
