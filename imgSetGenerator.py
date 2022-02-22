#!/usr/bin/env python3 

import os 
from glob import glob
import pandas as pd
import shutil

path = './'
types = ["negative","nuclear","cytoplasmic","mitotic"]
for typename in types:
	label_file = path + typename + '_labels.txt'
	img_dir = path + typename + '_img/'
	labels = pd.read_table(label_file,sep='	')
	for i in range(len(labels)):
		img_num = labels.values[i,0]
		if labels.values[i,1] == 1 :
			class_dir = img_dir + typename +'/'
			for filename in glob(path+'all-figs/'+str(img_num)+'[!0-9]*.jpg'):
				name = filename.replace('\\',"/").split('/')[-1]
				new_des = class_dir + name
				shutil.copy2(filename,new_des)
		elif labels.values[i,1] == 0 :
			class_dir = img_dir + 'non-' + typename +'/'
			for filename in glob(path+'all-figs/'+str(img_num)+'[!0-9]*.jpg'):
				name = filename.replace('\\',"/").split('/')[-1]
				new_des = class_dir + name
				shutil.copyfile(filename, new_des)






