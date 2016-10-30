#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import shutil
import string
import random

i = 0
# Set here the number of records you need
j = 1000
# Set here the wiche file name's length
length = 30

while i < j :
	newFileName=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) 
	for _ in range(length))
	shutil.copyfile('sample_documents/document', 'generated_documents/'+newFileName)
	recordNumber = str(i)
	print ('Record '+recordNumber+' - file ' +newFileName+' generated')
	i = i+1