import csv
import re
def data_in_dict():
	with open('C:\\Users\\admin\\Desktop\\Development\\trydjango\\src\\Automatic_Classification\\user_profile\\test.csv', mode='r') as infile:
	    reader = csv.reader(infile)
	    mydict = {rows[0]:rows[1:] for rows in reader}

	mydict1 = {}
	for k in mydict:
		l=[]
		for string in mydict[k]:
			s1 = re.sub(r'(\s\')|(\'$)','',string)
			if len(s1)!=0:
				l.append(s1)
		mydict1.update({k:l})

	return mydict1