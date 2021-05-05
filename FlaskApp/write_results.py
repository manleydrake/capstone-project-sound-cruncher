##Returns 6 character code
def extract():
	with open('/Users/michael/desktop/capstone-project-team-6-sound-cruncher/mlprogram/predict/test_2015_model-AlexNet.py_2021-04-26-18-06.csv') as f:
	        
	        f1 = f.readlines()	        
	        for line in f1:
	        	array = line.split(';')
	        	if array[2] == '1.0000000000000000\n':
	        		return array[1]

##Returns name,genus,species of bird in an array
def translate(code):
	f = open ('/Users/michael/desktop/capstone-project-team-6-sound-cruncher/flaskapp/classes.csv', 'r')
	f1 = f.readlines()
	for line in f1:
		arr = line.split(',')
		if arr[0] == code:
			return [arr[1], arr[2],arr[3].strip('\n')]



##writes to result.csv
def transfer():
	results = open("/Users/michael/desktop/capstone-project-team-6-sound-cruncher/flaskapp/result.csv", "w+")
	lines = results.readlines()[1:]
	results.write("Name,Genus,Species\n")
	array = translate(extract())
	results.write(array[0] + ',' +  array[1] + ',' + array[2])
	results.close()	
	return 0


transfer()


#todo change output file format