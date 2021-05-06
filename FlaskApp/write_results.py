##Returns 6 character code
def extract():
	with open('../MLProgram/predict/test.csv') as f:
	        max = 0
	        ret_value = ''
	        f1 = f.readlines()	        
	        for line in f1:
	        	array = line.split(';')
	        	val = array[2].strip('\n')
	        	val = float(val)
	        	if val >= max:
	        		ret_value = array[1]
	        		ret2 = val
	        		max = val
	        return [ret_value,ret2]

##Returns name,genus,species of bird in an array
def translate(code):
	f = open ('classes.csv', 'r')
	f1 = f.readlines()
	for line in f1:
		arr = line.split(',')
		if arr[0] == code:
			return [arr[1], arr[2],arr[3].strip('\n')]



##writes to result.csv
def transfer():
	results = open("result.csv", "w+")
	lines = results.readlines()[1:]
	results.write("Name,Genus,Species,Accuracy\n")
	array = translate(extract()[0])
	results.write(array[0] + ',' +  array[1] + ',' + array[2] + ',' + str(extract()[1]))
	results.close()	
	return 0


transfer()


#todo change output file format