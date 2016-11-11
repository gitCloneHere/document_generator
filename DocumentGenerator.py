#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import shutil
import string
import random

i = 0
# Set here the number of records you need
j = int(input('How much documents do you want to create?'))
# Set here the wiche file name's length
length = 30

docURI1 = 'sample_documents/doc1'
docURI2 = 'sample_documents/doc2'
docChoice = [docURI1, docURI2]

while i < j :
	newFileName=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) 
	for _ in range(length))
	selectedDoc = random.choice(docChoice)
	shutil.copyfile(selectedDoc, 'generated_documents/'+newFileName)
	recordNumber = str(i+1)
	print ('Record '+recordNumber+' - file ' +newFileName+' generated')
	i = i+1