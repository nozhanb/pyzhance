#~ #This is yet to begin.
import os

def symbol_data_catcher(symbol, start_Date, end_Date, output_path = os.getcwd(), 
						file_name = None, message = "FALSE"):

	#doc string
	# to run this function the following modules have to be installed.
	# need to add the output path parameter.
	# need to make a new directory and work on each function of the module 
	# separately and in the end add them all togather.
	# write a short description for each argument.
	# Do NOT use the tilde symbol as the output path name.
	
	
	# if the start day or the end day in the downloaded files is not the exact day
	# inserted as the argumnet of the function it may be that the inserted date is
	# a holiday. The user can check the yahoo finance historic data to make sure.
	# add the "I am still alive" parameter (after a specific amount of time).
	# add name of the file argument.
	# add file extension argument.
	
	import os
	import urllib2

	out_path = os.path.join(output_path)
	#~ name = symbol.split(",")
	sDate = start_Date.split("-")
	a = str(int(sDate[1]) - 1)	# month (I added a -1 so it matched the yahoo format)
	b = sDate[2]	# day
	c = sDate[0]	# year
	eDate = end_Date.split("-")
	d = str(int(eDate[1]) - 1)	# month (same as above)
	e = eDate[2]	# day
	f = eDate[0]	# year
	storeName = []
	
	if file_name is None:
		file_name = symbol
	for sym in file_name:
		storeName.extend([sym])
		file = out_path + sym + ".csv"
		downloadFile = open(file, "w")
		url = "http://real-chart.finance.yahoo.com/table.csv?s="+sym+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g=d&ignore=.csv"
		symbolUrl = urllib2.urlopen(url)
		downloadFile.write(symbolUrl.read())
		downloadFile.close()
		if message == "TRUE":
			print
			print(sym+".csv ---> downloaded")
			print
