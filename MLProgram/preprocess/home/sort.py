import os
import shutil

#List of the sub categories we want
list = ['Amazonian Antshrike', 'Tufted Antshrike']

#Creates a directpry for each species
for list_index in range(len(list)):
	os.mkdir(list[list_index])


#Loops through each file in the directory 
for filename in os.listdir('xml'):
	#os.system("echo " + filename)
	f = open(filename, 'r', encoding='ISO-8859-1')
	f1 = f.readlines()
	for x in f1:

		#Copies the corresponding wav file(s) to folder
		for y in range(len(list)):
			if '<VernacularNames>' + list[y] + '</VernacularNames>' in x:#sorting by vernacular name
				print(1)
				filename2 = filename[:-3]
				filename2 = filename2 + 'wav'#Gets corresponding wav file
				original = r'/Users/michael/desktop/home/wav/' + filename2
				target = r'/Users/michael/desktop/home/' + list[y] + '/' + filename2
				shutil.copyfile(original, target)#copy file

	f.close()
