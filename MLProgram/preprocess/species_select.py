
#place this file in the test or Training Set folder and run it from command line from within that directory to subset data based on your chosen classes. 

import csv
import os
import shutil

#This function reads in list of the species we want, then 
#f represents 'species.csv'
def mk_species_dict(f):
	species_dict = {}
	with open(f, mode='r') as s:
		reader = csv.DictReader(s)
		line_count = 0
		for row in reader:
			if line_count == 0:
				line_count += 1
			species_dict[row["name"]] = [row["genus"], row["species"]]
			line_count += 1
	return species_dict 

def copy_files(species_dict):
	
	n_species = len(species_dict)
	#create main folder and subfolders for storing subset
	main = str(n_species) + "_" + "Species"
	os.mkdir(main)
	os.mkdir(main + "/xml")
	os.mkdir(main + "/wav")

	#Loops through each file in the directory 
	for filename in os.listdir('xml'):
		try:
			f = open("xml/" + filename, 'r', encoding='ISO-8859-1')
			f1 = f.readlines()
			for line in f1:
				#Copies the corresponding wav file(s) to folder
				for key, value in species_dict.items():
					#check if xml indicates the desired Species
					if ('<Species>' + value[1] + '</Species>' in line) and ('<Genus>' + value[0] + '</Genus>' in prev_line):
						#path of original xml file
						original = "xml/" + filename
						#target path for xml
						target = main + "/" + original
						#copy wav and xml to new folder
						shutil.copyfile(original, target)
						print("xml copy successful for " + key)

						#path of original wav file
						original = "wav/" + filename[:-3] + "wav"
						#target path for wav copy
						target = main + "/" + original
						shutil.copyfile(original, target)
						print("wav copy successful for " + key)
				prev_line = line	
			f.close()
		except FileNotFoundError as error:
			print(error)
		

species = mk_species_dict("species.csv")
copy_files(species)




