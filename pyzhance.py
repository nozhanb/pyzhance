#~ #This is yet to begin.
import os

def data_downloader(symbol, start_Date, end_Date, outputPath = os.getcwd(), 
						file_name = None, intraday = "FALSE", message = "FALSE"):

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
	
	# add the "I am still alive" parameter (after a specific amount of time has passed).
	# add name of the file argument. ---> if files are not downloaded soon enough the 
	# program has to be stopped. 
	# add file extension argument.X
	# find a connection between volume and up/down trend for each day. For instance,
	# if today's market volume was high and the total/genral trend of the market for
	# that day was down ward, does that mean the next day we are going to have a up trend 
	# market or not? Check if the volume of the day is correlated to the ratio of O/C.
	# See if you can find a way to tell where the money is flowing to (to what sector or market
	# country). Also, check for the time difference between indices (like S&P) and other weak or
	# strong stocks in different sectors.
	
	
	
#	type(datetime.datetime.strftime(datetime.datetime.fromtimestamp(1457706672), "%Y-%m-%d"))
#	<type 'str'>

#	http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=1d/csv
	
	import os
	import time
	import urllib2

#	outputPath = '~/nozhan/science/computation/data/finance/output/code/pyzhance/data_downloader'
	outPath = os.path.join(outputPath)
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
	if intraday == "FALSE":
		for sym in file_name:
			storeName.extend([sym])
			file = outPath + sym + ".csv"
			downloadFile = open(file, "w")
			urlToRead = "http://real-chart.finance.yahoo.com/table.csv?s="+sym+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g=d&ignore=.csv"
			symbolUrl = urllib2.urlopen(urlToRead)
			downloadFile.write(symbolUrl.read())
			downloadFile.close()
			if message == "TRUE":
				print
				print(sym+".csv ---> downloaded")
				print
	if intraday == "TRUE":
		for sym in file_name:
			storeName.append(sym)
			file = outPath + sym + ".csv"
#			downloadFile = open(file, "w")
			urlToRead = "http://chartapi.finance.yahoo.com/instrument/1.0/"+sym+"/chartdata;type=quote;range=1d/csv"
			sourceCode = urllib2.urlopen(urlToRead).read()
#			downloadfile = file.write(sourceCode.read())
			
			#######
			splitSource = sourceCode.split('\n')
			for eachLine in splitSource:
				if len(eachLine.split(',')) == 6:
					if 'values' not in eachLine:
						downloadFile = open(file, "a")
						downloadFile.write(eachLine+'\n')
			print('pulled', sym)
			print('sleeping')
			time.sleep(5)
			
				
				
				
				
				
				
				
