
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
				outputPath = None, inputPathName = None, 
				output_format = None, outputFileName = None, 
				write = False, day = None, month = None, year = None,
				numeric = True, latin = False, latinDay = None):
		
		#	write = if "TRUE" the code will write out the result to a 
		#	file. The default is "FALSE".
		
		#	Date,Open,High,Low,Close,Volume,Adj Close
		
	import os
	import numpy
	import datetime
		
	if inputPathName is not None:
		fileName = os.path.join(os.path.expanduser(inputPathName),inputFileName)
	if inputPathName is None:
		fileName = os.path.join(os.getcwd(),inputFileName)
		
	def date_converter(tag): # tag: German word for day.
		convertedDate = datetime.datetime.strptime(tag,dateFormat)
		ordinalDate = datetime.date.toordinal(convertedDate)
		return ordinalDate		
	
#	tag = date_converter(x,dateFormat)

	#	NOTE: Do NOT use the dtype arguemtn or you will get the "Too many
	#	values to unpack". The best way is to use the "strpdate2num" function 
	#	and the "converters" argument as follows.
	
	dataArray = numpy.genfromtxt(fname = fileName, delimiter = ",", 
	dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
	('close','f3'),('volume','i4'),('adjclose','f3')],converters = {0:date_converter})
	
	date = []
	open = []
	high = []
	low = []
	close = []
	volume = []
	adjclose = []
	
	date = dataArray['date']
	open = dataArray['open']
	high = dataArray['high']
	low = dataArray['low']
	close = dataArray['close']
	volume = dataArray['volume']
	adjclose = dataArray['adjclose']
	
	for mainCounter in range(len(year)):
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
		print (datetime.date(yStart, mStart, dStart).strftime(dateFormat))
		ordinalEndDate = datetime.date.toordinal(datetime.datetime.strptime(datetime.date(yEnd, mEnd, dEnd).strftime(dateFormat), dateFormat))
		print datetime.date(yEnd, mEnd, dEnd).strftime(dateFormat)	
		print (ordinalStartDate, ordinalEndDate)
		startDateIndex = numpy.where(date == ordinalStartDate)
		endDateIndex = numpy.where(date == ordinalEndDate)
		indexLength = abs(endDateIndex[0] - startDateIndex[0])
		print (startDateIndex, endDateIndex, indexLength)
		emptyArray = numpy.empty(shape = 0, dtype = int)
		counter = 0
		for i in range(0, indexLength + 1):
			if counter < indexLength + 1:
				slicedDate = numpy.append(emptyArray, date[endDateIndex[0] + i])
			emptyArray = slicedDate
			counter += 1
		print slicedDate, slicedDate.shape, date.shape, type(slicedDate)
		if latin == True:
			latinCounter = 0
			for ll in range(len(latinDay)):
				for length in range(len(slicedDate)):
					one = datetime.date.fromordinal(slicedDate[length]).strftime('%a')
					if one == latinDay[latinCounter]:
						print latinDay[latinCounter], ' ---> ', datetime.date.fromordinal(slicedDate[length]).strftime('%Y-%m-%d')
				latinCounter += 1
	
