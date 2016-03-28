#~ #This is yet to begin.
import os

def data_downloader(readIn = "FALSE", readOut = "FALSE", intraday = "FALSE", symbol = None, 
					startDate = None, endDate = None, outputPath = None,
					inputPathName = None, outputPathName = None, 
					outputSymbol = None, inputFileName = None, 
					outputFileName = None, message = "FALSE"):
						
	# read_in: if set to "TRUE" the code will use the given text file 
	# to read in symbols from that file. Note that the user MUST provide
	# a path (i.e. inputPathName) so the machine can find the file. Note that
	# if user sets the readIN option to "FALSE" a list of symbols MUST be
	# provided for the symbol argument (see below).
	# inputPathName: is the path to the text file that this code will use to 
	# read in the symbols from the file (see above).
	# symbol: a list of symbols.
	# start_Date, end_Date: a date of the 'yyyy-mm-dd' format with 
	# quotation marks. Note if dates are not available ... the nearest before the inserted ...
	# outputPath: a path to tell the machine where to save the output. 
	# The default is the current directory.
	# file_name: User can set a name for the output file.
	# intraday: if it is set to "TRUE" the code will download the intr
	# day information of the symbols and ignores the given dates. The de
	# fault is "FALSE" and it downloads the data based on the given dates.
	# message: if set to "TRUE" it prints out some information a long 
	# the procedure such as the data of what symbol is downloading. The 
	# default is "FALSE" so it does NOT print out anything.
	# outputSymbol: is a list.
	# outputFileName: is a file name.
	
	# The output of this code is a file with the following format:
	# datetime (if interval is given) and timestamps (is intrady), open, ...
	
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
	
	# Things to do tomorrow:
	# work on the sphinx.
	# keep coding the second function (i.e. conversion from datetime string to 
	# numbers and the other way around).
	
#	type(datetime.datetime.strftime(datetime.datetime.fromtimestamp(1457706672), "%Y-%m-%d"))
#	<type 'str'>
	
	import os
	import sys
	import time
	import urllib2

	if outputPath is None:
		outputPath = os.getcwd()
	elif outputPath is not None:
		outputPath = os.path.expanduser(outputPath)
	if inputPathName is None:
		inputPathName = os.getcwd()
		
	if readIn == "TRUE":
		if inputPathName is None:
			file = os.path.join(os.getcwd(),inputFileName)
		elif inputPathName is not None:
			file = os.path.join(os.path.expanduser(inputPathName),inputFileName)
		symbolToRead = open(file,'r')
		symbol = []
		for line in symbolToRead:
			symbol.append(line.strip()) # The strip command removes 
		symbolToRead.close()			# unwanted empty space of each
										# line when it is reading the file.

	if readOut == "TRUE":
		if outputPathName is None:
			file = os.path.join(os.getcwd(), outputFileName)
		elif outputPathName is not None:
			file = os.path.join(os.path.expanduser(outputPathName), outputFileName)
		outName = open(file, "r")
		outputSymbol = []
		for outline in outName:
			outputSymbol.append(outline.strip())
		outName.close()
		
	if readIn == "TRUE" and readOut == "FALSE":
		outputSymbol = symbol
	if readIn == "FALSE" and readOut == "FALSE":
		outputSymbol = symbol
	
	if intraday == "FALSE":
		outPath = os.path.join(outputPath)
		sDate = startDate.split("-")
		a = str(int(sDate[1]) - 1)	# month (I added a -1 so it matched the yahoo format)
		b = sDate[2]	# day
		c = sDate[0]	# year
		eDate = endDate.split("-")
		d = str(int(eDate[1]) - 1)	# month (same as above)
		e = eDate[2]	# day
		f = eDate[0]	# year
		counter = 0
		for sym in symbol:
			file = os.path.join(outputPath, outputSymbol[counter] + ".csv")
			downloadFile = open(file, "w") # if you use "a" (i.e. append) instead of "w" every time user runs the code the new 
											# data will be added to the file without removing the old one.
			urlToRead = "http://real-chart.finance.yahoo.com/table.csv?s="+sym+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g=d&ignore=.csv"
			sourceCode = urllib2.urlopen(urlToRead).readlines()	# The readline(), read() or readlines() command open the file
			# object generated by the urllib2.urlopen() and that is why we use one of those command to open the file and then 
			# write the file into another file (the one user intends to be filled).
			#for line in sourceCode
			del sourceCode[0]
			sourceCodeTwo = sourceCode
			for element in sourceCodeTwo:
				downloadFile.write(element)
			downloadFile.close()
			if message == "TRUE":
				print
				print(sym + ".csv ---> downloaded")
				print
			time.sleep(2)
			counter += 1
	if intraday == "TRUE":
		counter = 0
		for sym in symbol:
			file = os.path.join(outputPath, outputSymbol[counter] + ".csv")
			downloadFile = open(file, "w")
			urlToRead = "http://chartapi.finance.yahoo.com/instrument/1.0/"+sym+"/chartdata;type=quote;range=1d/csv"
			sourceCode = urllib2.urlopen(urlToRead).read()
			splitSource = sourceCode.split('\n')
			for eachLine in splitSource:
				if len(eachLine.split(',')) == 6:
					if 'values' not in eachLine:
						downloadFile.write(eachLine+'\n')
			downloadFile.close()
			
			if message == "TRUE":
				print(sym + ".csv", " ---> downloaded ")
				#print('sleeping')
				
			time.sleep(2)
			counter += 1
	
	
