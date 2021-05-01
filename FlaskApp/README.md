# CSCapstone

!!Need to modify paths in following lines:

flaskapp.py-

14

22?


write_results.py-

4 (this will have to be changed to whatever our prediction output file is)

15

26

_____________________________________________________________________

Changes:
write_results added - reads output file and translates it to relevant strings. Writes (overwrites) the results to result.csv

run write results in line 24 of flaskapp.py (right after prediction)

/results in flaskapp will now display picture of bird based on what result.csv has for name (Lines 51-79)


