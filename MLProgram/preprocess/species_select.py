


# define a function that will search the xml for MediaID, 
# Genus, and Species and return them as a tuple "s_tuple"


# define a function that compares that the genus and species against the
# list of selected classes and returns True if there is a match


# Loop through the xml directory and grab all xmls that have one of the 
# selected genus and species. Place in separate directory. 
# The MediaID, Genus, and Species should also be stored in a dictionary, "s_dict". 

# Loop through the wav directory and grab all wav files with the 
# MediaID's contained in the dictionary. Place in a separate dictionary 

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


n_species = len(species_dict)
#Creates a directory for each species
for index in range(n_species):
	os.mkdir(list[index])

#Loops through each file in the directory 
for filename in os.listdir('xml'):
	#os.system("echo " + filename)
	f = open(filename, 'r', encoding='ISO-8859-1')
	f1 = f.readlines()
	for line in f1:
		#Copies the corresponding wav file(s) to folder
		for key, value in species_dict:
			#change Vernacular Names to Genus and Species
			if ('<Genus>' + value[0] + '</Genus>' in line) and ('<Species>' + value[1] + '</Species>' in line) :#sorting by vernacular name
				file_found = True
				filename2 = filename[:-3]
				filename2 = filename2 + 'wav'#Gets corresponding wav file
				original = r'/wav/' + filename2
				target = r'' + list[value[0]] + list(value[1]) + '/' + filename2
				shutil.copyfile(original, target)#copy file


	f.close()

# TODO:
# Make sure selected XML's and WAV's are placed into their own directories (make these directories)
# Rearrange so that outer loop is iterating on species dict, rather than other way around
# Modularize. 



