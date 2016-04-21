
import os

def data_downloader(readIn = False, readOut = False, intraday = False, symbol = None, 
					startDate = None, endDate = None, outputPath = None,
					inputPathName = None, outputPathName = None, 
					outputSymbol = None, inputFileName = None, 
					outputFileName = None, message = False):
						
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
		
	if readIn == True:
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

	if readOut == True:
		if outputPathName is None:
			file = os.path.join(os.getcwd(), outputFileName)
		elif outputPathName is not None:
			file = os.path.join(os.path.expanduser(outputPathName), outputFileName)
		outName = open(file, "r")
		outputSymbol = []
		for outline in outName:
			outputSymbol.append(outline.strip())
		outName.close()
		
	if readIn == True and readOut == False:
		outputSymbol = symbol
	if readIn == False and readOut == False:
		outputSymbol = symbol
	
	if intraday == False:
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
			file = os.path.join(outputPath, outputSymbol[counter])
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
			if message == True:
				print
				print(sym + " ---> downloaded")
				print
			time.sleep(2)
			counter += 1
	if intraday == True:
		counter = 0
		for sym in symbol:
			file = os.path.join(outputPath, outputSymbol[counter])
			downloadFile = open(file, "w")
			urlToRead = "http://chartapi.finance.yahoo.com/instrument/1.0/"+sym+"/chartdata;type=quote;range=1d/csv"
			sourceCode = urllib2.urlopen(urlToRead).read()
			splitSource = sourceCode.split('\n')
			for eachLine in splitSource:
				if len(eachLine.split(',')) == 6:
					if 'values' not in eachLine:
						downloadFile.write(eachLine+'\n')
			downloadFile.close()
			
			if message == True:
				print(sym + " ---> downloaded ")
				#print('sleeping')
				
			time.sleep(2)
			counter += 1
	
	

	# name of the file
	# name/number of the column(s)
	# format to read (format of the input data)
	# format to convert to (format of the output data)
	# name of the file to be written to (the output file)
	
	#	1- Find me "yyyy-mm-dd" (as the start date) and "yyyy-mm-dd" 
	#	(as the end date) and convert them to numbers to find me the 
	#	followings:
	
	#	Note: There should be an option so the user can indicate whether
	#	they are using interaday or non-intraday data.
	
	#	Note: If the given slice does NOT exist in data file the code 
	#	should be able to find the nearest (after or before) day of data
	#	file. And this should be included in the documentation of the 
	#	code.
	
	#	---> Note: a list of input(s) can be given and a list of output(s) 
	#	can be returned by the function (think about it). <---
	
	#	2- The user should be asked if they want the related information
	#	in the slice or there are more than one slice? Only for one year
	#	(e.g. the current year), every month of the year(s) (e.g. every 
	#	first week of every month of the year(s)) or every couple of days 
	#	of the specific weeks of specific months of specefic years? All 
	#	in all, the user should have to freedom to give the smallest 
	#	slice possible (one day) for a specific week, month and year. 
	#	e.g. What day(s) (i.e. smallest slice)? what month(s)? What 
	#	year(s)?
	#	Note that in case of one day the code should be able to take in
	#	only one day.
	
	#	3- Once you have found the above slice(s) write out all the 
	#	data (open, close, low, ...) in this interval along with the 
	#	converted date column.
	#	In case of several slices the cose has to be able to write out 
	#	the result in one file but append the results of each interval.
	
	#	PHASE TWO:
	
	#	1- Print out those days in a given interval (e.g. for every 
	#	first week of the month)that eithre one or more that one column
	#	(depending what user wants) of the input data file (open, close,
	#	 low, high, volume)  is higher or lower than that value.
	
	#	2- The above line should be applicable to extract the intended 
	#	days based on other ... (I am not sure what I want)!!!
	#	


	#	Things to do for tomorrow:
	#	
	#	1- Correct the TRUE and FALSE in the data_downloader file.
	#	2- The input should be a list of arrays where each array 
	#		represents days, months and years.
	#	3- Output should be same as input.
	#	4- Add the line that tells the user that the given date does not
	#		exist in the file and replace the ouput value with a NoData.
	

import os

def data_slicer(dateFormat = '%Y-%m-%d', inputFileName = None, 
				symbol = None, outputPath = None, inputPath = None,
				day = None, month = None, year = None,
				letterSearch = False, letterDay = None, 
				outputFileName = None):
		
		#	write = if "TRUE" the code will write out the result to a 
		#	file. The default is "FALSE".
		
		#	Date,Open,High,Low,Close,Volume,Adj Close
		
	import os
	import sys
	import numpy
	import datetime


	if symbol is not None:
		symbolTwo = symbol
	elif symbol is None:
		inputFile = open(inputFileName, 'r')
		symbolTwo = []
		for line in inputFile:
			symbolTwo.append(line.strip())
		inputFile.close()

	for inputs in symbolTwo:
		if inputPath is not None:
			inputPathFile = os.path.join(os.path.expanduser(inputPath),inputs)
		elif inputPath is None:
			inputPathFile = os.path.join(os.getcwd(),inputs)
		if outputPath is None:
			outputPath = os.getcwd()
		elif outputPath is not None:
			outputPath = os.path.expanduser(outputPath)
		#~ if outputFileName is None:
			#~ outputFileName = os.path.join(os.getcwd(), inputs)
		#~ elif outputFileName is not None:
			#~ outputFileName = os.path.join(os.path.expanduser(inputPath), outputFileName)
			
			
		def date_converter(tag): # tag: German word for day.
			convertedDate = datetime.datetime.strptime(tag,dateFormat)
			ordinalDate = datetime.date.toordinal(convertedDate)
			return ordinalDate		
		
		#	tag = date_converter(x,dateFormat)
		
		#	NOTE: Do NOT use the dtype arguemnt or you will get the "Too many
		#	values to unpack". The best way is to use the "strpdate2num" function 
		#	and the "converters" argument as follows.
		
		dataArray = numpy.genfromtxt(fname = inputPathFile, delimiter = ",", 
		dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
		('close','f3'),('volume','i4'),('adjclose','f3')],converters = {0:date_converter})
		
		date = []
		openn = []	#	openn with "nn" because python will confuse it with function open otherwise.
		high = []
		low = []
		close = []
		volume = []
		adjclose = []
		
		date = dataArray['date']
		openn = dataArray['open']
		high = dataArray['high']
		low = dataArray['low']
		close = dataArray['close']
		volume = dataArray['volume']
		adjclose = dataArray['adjclose']
		
		for mainCounter in range(len(year)):
			n = mainCounter
			ordinalDate = "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])		
			yCounter = 0
			for yPair in year[mainCounter]:
				if yCounter % 2 == 0:
					yStart = yPair
				if yCounter % 2 == 1:
					yEnd = yPair
				yCounter += 1
			mCounter = 0
			for mPair in month[mainCounter]:
				if mCounter % 2 == 0:
					mStart = mPair
				if mCounter % 2 == 1:
					mEnd = mPair
				mCounter += 1
			dCounter = 0
			for dPair in day[mainCounter]:
				if dCounter % 2 == 0:
					dStart = dPair
				if dCounter % 2 == 1:
					dEnd = dPair
				dCounter += 1
			
			ordinalStartDate = datetime.date.toordinal(datetime.datetime.strptime(datetime.date(yStart, mStart, dStart).strftime(dateFormat), dateFormat))
			ordinalEndDate = datetime.date.toordinal(datetime.datetime.strptime(datetime.date(yEnd, mEnd, dEnd).strftime(dateFormat), dateFormat))
			startDateIndex = numpy.where(date == ordinalStartDate)
			endDateIndex = numpy.where(date == ordinalEndDate)
			indexLength = abs(endDateIndex[0] - startDateIndex[0])
			
			slicedDate = numpy.empty(shape = 0, dtype = int)
			slicedOpen = numpy.empty(shape = 0, dtype = float)
			slicedHigh = numpy.empty(shape = 0, dtype = float)
			slicedLow = numpy.empty(shape = 0, dtype = float)
			slicedClose = numpy.empty(shape = 0, dtype = float)
			slicedVolume = numpy.empty(shape = 0, dtype = int)
			slicedAdjclose = numpy.empty(shape = 0, dtype = float)
			
			counter = 0
			for i in range(0, indexLength + 1):
				if counter < indexLength + 1:
					emptyDate = numpy.append(slicedDate, date[endDateIndex[0] + i])
					emptyOpen = numpy.append(slicedOpen, openn[endDateIndex[0] + i])
					emptyHigh = numpy.append(slicedHigh, high[endDateIndex[0] + i])
					emptyLow = numpy.append(slicedLow, low[endDateIndex[0] + i])
					emptyClose = numpy.append(slicedClose, close[endDateIndex[0] + i])
					emptyVolume = numpy.append(slicedVolume, volume[endDateIndex[0] + i])
					emptyAdjclose = numpy.append(slicedAdjclose, adjclose[endDateIndex[0] + i])
				slicedDate = emptyDate
				slicedOpen = emptyOpen
				slicedHigh = emptyHigh
				slicedLow = emptyLow
				slicedClose = emptyClose
				slicedVolume = emptyVolume
				slicedAdjclose = emptyAdjclose
				counter += 1
				
			if letterSearch == True:
				letterDate = numpy.empty(shape = 0, dtype = int)
				letterOpen = numpy.empty(shape = 0, dtype = float)
				letterHigh = numpy.empty(shape = 0, dtype = float)
				letterLow = numpy.empty(shape = 0, dtype = float)
				letterClose = numpy.empty(shape = 0, dtype = float)
				letterVolume = numpy.empty(shape = 0, dtype = int)
				letterAdjclose = numpy.empty(shape = 0, dtype = float)
				
				#	Do not confuse "letterDate" with "letterDay".
				letterCounter = 0
				for ll in range(len(letterDay)):
					n = ll
					letterDate = numpy.empty(shape = 0, dtype = int)
					letterOpen = numpy.empty(shape = 0, dtype = float)
					letterHigh = numpy.empty(shape = 0, dtype = float)
					letterLow = numpy.empty(shape = 0, dtype = float)
					letterClose = numpy.empty(shape = 0, dtype = float)
					letterVolume = numpy.empty(shape = 0, dtype = int)
					letterAdjclose = numpy.empty(shape = 0, dtype = float)
					#~ ordinalDay = "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
					for length in range(len(slicedDate)):
						notOrdinalDate = datetime.date.fromordinal(slicedDate[length]).strftime('%a')
						if notOrdinalDate == letterDay[letterCounter]:
							clearDate = numpy.append(letterDate, slicedDate[length])
							clearOpen = numpy.append(letterOpen, slicedOpen[length])
							clearHigh = numpy.append(letterHigh, slicedHigh[length])
							clearLow = numpy.append(letterLow, slicedLow[length])
							clearClose = numpy.append(letterClose, slicedClose[length])
							clearVolume = numpy.append(letterVolume, slicedVolume[length])
							clearAdjclose = numpy.append(letterAdjclose, slicedAdjclose[length])
							
							letterDate = clearDate
							letterOpen = clearOpen
							letterHigh = clearHigh
							letterLow = clearLow
							letterClose = clearClose
							letterVolume = clearVolume
							letterAdjclose = clearAdjclose
					letterCounter += 1
					
					numpy.savetxt(inputs+ordinalDate+letterDay[n], numpy.c_[letterDate, letterOpen, letterHigh, letterLow, letterClose, letterVolume, letterAdjclose], fmt = ('%d','%.6f','%.6f','%.6f','%.6f','%d','%.6f'), delimiter = ',')
			if letterSearch == False:
				n = mainCounter
				numpy.savetxt(inputs+ordinalDate, numpy.c_[slicedDate, slicedOpen, slicedHigh, slicedLow, slicedClose, slicedVolume, slicedAdjclose], fmt = ('%d','%.6f','%.6f','%.6f','%.6f','%d','%.6f'), delimiter = ',')
		#~ if letterSearch == True:
			#~ return 
		#~ if letterSearch == False:
			#~ return slicedDate, slicedOpen, slicedHigh, slicedLow, slicedClose, slicedVolume, slicedAdjclose	



