sort.py executable

Right now, this creates folders for each subtype-searched for (lines 5-9).
Then reads xml files and if criteria matches, copies corresponding wav file to newly created folder.

Not sure if this is exactly what we want, but it is a start. 
Add your own paths at lines 25-26

Directory structure is unusual;
home directory has sort.py, all wav files, all xml files, plus xml directory and wav directory. THis is also where new sorted folders will be created. 
wav directory has all wav files (same files that are in home)
xml directory has xml files

The reason for this structure is because line 13 affects all files in a directory that is contained in your current directory, while line 15 opens a file in current directory, so there must be a copy of all the files in both home and wav/xml directories.
