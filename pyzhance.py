#~ #This is yet to begin.

def symboldatacacher(symbol, startDate, endDate, message = "FALSE"):

	#doc string
	# to run this function the following modules have to be installed.
	# need to add the output path parameter.
	# need to make a new directory and work on each function of the module 
	# separately and in the end add them all togather.
	
	# if the start day or the end day in the downloaded files is not the exact day
	# inserted as the argumnet of the function it may be that the inserted date is
	# a holiday. The user can check the yahoo finance historic data to make sure.
	# add the "I am still alive" parameter (after a specific amount of time).
	
	import urllib2

	name = symbol.split(",")
	sDate = startDate.split("-")
	a = str(int(sDate[1]) - 1)	# month
	b = sDate[2]	# day
	c = sDate[0]	# year
	eDate = endDate.split("-")
	d = str(int(eDate[1]) - 1)	# month
	e = eDate[2]	# day
	f = eDate[0]	# year
	storeName = []
	for i in name:
		storeName.extend([i])
		file = i + ".csv"
		downloadFile = open(file, "w")
		url = "http://real-chart.finance.yahoo.com/table.csv?s="+i+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g=d&ignore=.csv"
		symbolUrl = urllib2.urlopen(url)
		downloadFile.write(symbolUrl.read())
		downloadFile.close()
		if message == "TRUE":
			print
			print(i+".csv ---> downloaded")
			print
