
import os

def data_downloader(symbol, startDate, endDate, readIn = False, 
					readOut = False, intraday = False, outputPath = None,
					inputPathName = None, outputPathName = None, 
					outputSymbol = None, inputFileName = None, 
					outputFileName = None, message = False):
#~ '''
#~ This method will let the user to download data for a given symbol. The method will use the yahoo finance website. Different argumetns 
#~ of this method are as follows:
#~ 
#~ readIn: if set to "True" user must provide a file for the symbol argument and a path for the inputPathName argument. The file that
#~ is provided for the symbol argument should include the symbol of the stocks (e.g. DIS for Walt Disney). The format of the file should
#~ be in a way that each line has to contain one symbol with no quotation marks around it and all the letters have to be capital letters. 
#~ The path to this file has to be given in the inputPathName argument. The path should be in string format meaning that user has to put
#~ quotation mark around the path. If, user sets the readIn argumetn to False, the symbol argument has to be set to a list of symbols 
#~ manually (e.g. symbol = [ABC, DEF, ..., XYZ]). The defualt value is False.
#~ 
#~ ReadOut: 
#~ 
	#~ # inputPathName: is the path to the text file that this code will use to 
	#~ # read in the symbols from the file (see above).
	#~ # symbol: a list of symbols.
	#~ # start_Date, end_Date: a date of the 'yyyy-mm-dd' format with 
	#~ # quotation marks. Note if dates are not available ... the nearest before the inserted ...
	#~ # outputPath: a path to tell the machine where to save the output. 
	#~ # The default is the current directory.
	#~ # file_name: User can set a name for the output file.
	#~ # intraday: if it is set to "TRUE" the code will download the intr
	#~ # day information of the symbols and ignores the given dates. The de
	#~ # fault is "FALSE" and it downloads the data based on the given dates.
	#~ # message: if set to "TRUE" it prints out some information a long 
	#~ # the procedure such as the data of what symbol is downloading. The 
	#~ # default is "FALSE" so it does NOT print out anything.
	#~ # outputSymbol: is a list.
	#~ # outputFileName: is a file name.
	#~ 
	#~ # The output of this code is a file with the following format:
	#~ # datetime (if interval is given) and timestamps (is intrady), open, ...
	#~ 
	#~ #doc string
	#~ # to run this function the following modules have to be installed.
	#~ # need to add the output path parameter.
	#~ # need to make a new directory and work on each function of the module 
	#~ # separately and in the end add them all togather.
	#~ # write a short description for each argument.
	#~ # Do NOT use the tilde symbol as the output path name.
	#~ 
	#~ 
	#~ # if the start day or the end day in the downloaded files is not the exact day
	#~ # inserted as the argumnet of the function it may be that the inserted date is
	#~ # a holiday. The user can check the yahoo finance historic data to make sure.
	#~ 
	#~ # add the "I am still alive" parameter (after a specific amount of time has passed).
	#~ # add name of the file argument. ---> if files are not downloaded soon enough the 
	#~ # program has to be stopped. 
	#~ # add file extension argument.X
	#~ # find a connection between volume and up/down trend for each day. For instance,
	#~ # if today's market volume was high and the total/genral trend of the market for
	#~ # that day was down ward, does that mean the next day we are going to have a up trend 
	#~ # market or not? Check if the volume of the day is correlated to the ratio of O/C.
	#~ # See if you can find a way to tell where the money is flowing to (to what sector or market
	#~ # country). Also, check for the time difference between indices (like S&P) and other weak or
	#~ # strong stocks in different sectors.
#~ '''
		
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
		#~ a = sDate[1] - 1
		a = str(int(sDate[1]) - 1)	# month (I added a -1 so it matches the yahoo's format)
		b = sDate[2]	# day
		c = sDate[0]	# year
		eDate = endDate.split("-")
		#~ d = eDate[1] - 1
		d = str(int(eDate[1]) - 1)	# month (same as above)
		e = eDate[2]	# day
		f = eDate[0]	# year
		counter = 0
		for sym in symbol:
			file = os.path.join(outputPath, outputSymbol[counter])
			downloadFile = open(file, "w") # if you use "a" (i.e. append) instead of "w" every time user runs the code the new 
											# data will be added to the file without removing the old ones.
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
		
		#	NOTE: Do NOT use the dtype argument or you will get the "Too many
		#	values to unpack". The best way is to use the "strpdate2num" function 
		#	and the "converters" argument as follows.

		dataArray = numpy.genfromtxt(fname = inputPathFile, delimiter = ",", 
		dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
		('close','f3'),('volume','i4'),('adjclose','f3')],converters = {0:date_converter})
		
		date = []
		openn = []	#	openn with "nn" because python will confuse it with the function open otherwise.
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


import os
import sys
import numpy
import pyformat
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#~ plt.rc('text', usetex=True)
#~ plt.rc('font', family='serif')

#~ (symbol_wd = ['DIS0thMon','DIS0thTue','DIS0thWed','DIS0thThu','DIS0thFri', 'KO0thMon','KO0thTue','KO0thWed','KO0thThu','KO0thFri'], symbol_total = ['DIS','KO'], cTo = True, output_path = '~/nozhan/science/computation/data/finance/output/code/pyzhance/ratio_weekday')


def ratio_weekday(symbol_wd, symbol_total ,cTo = True, input_path_wd = None, 
					input_path_total = None, output_path = None):
	
	#	This function will find differeant ratios for different stocks 
	#	based on weekdays.	cMoThMl
	
	#	symbol_wd: is the list of name of files where each file contains
	#	the data of a symbol based on single week days of given interval.
	#	symbol_total: is the list of name of files where each file contains
	#	the data of a symbol for all days of a given interval.
	
	days = ['Mon','Tue','Wed','Thu','Fri']
		
	if cTo == True:	#	Then it will find the ratio of Close to Open price.
		dic_wd = []
		dic_total = []
		count = 0
		count1 = 0
		count2 = 0		
		count3 = 0
		fig1, axa = plt.subplots(2,3)
		#~ fig2, axb = plt.subplots(1,1)

		for i in symbol_wd:
			if input_path_wd is None:
				main_input_path_wd = os.path.join(os.getcwd(), i)
			elif input_path_wd is not None:
				main_input_path_wd = os.path.join(os.path.expanduser(input_path_wd), i)				
			if output_path is None:
				main_output_path = os.path.join(os.getcwd(), i)
			elif output_path is not None:
				main_output_path = os.path.join(os.path.expanduser(output_path), i)
			
			#	We creat a dictionary of different varibles.
			
			var_wd = {symbol_wd[count]+'CGO' : [], symbol_wd[count]+'CEO' : [], symbol_wd[count]+'CLO' : [],
			symbol_wd[count]+'FG' :    [], symbol_wd[count]+'FE' :    [], symbol_wd[count]+'FL' : [],
			symbol_wd[count]+'Final':  [], symbol_wd[count]+'CGOCTO': [], symbol_wd[count]+'CGOHTL' : [],
			symbol_wd[count]+'CGOO' :  [], symbol_wd[count]+'CGOC' :  [], symbol_wd[count]+'CGOH' : [],
			symbol_wd[count]+'CGOL' :  [], symbol_wd[count]+'CGOV' :  [], symbol_wd[count]+'CLOO' : [], 
			symbol_wd[count]+'CLOC' :  [], symbol_wd[count]+'CLOH' :  [], symbol_wd[count]+'CLOL' : [], 
			symbol_wd[count]+'CLOV' :  [], symbol_wd[count]+'CGOCTOTHTL': [], symbol_wd[count]+'CGOD' : [],
			symbol_wd[count]+'CLOCTO' :[], symbol_wd[count]+'CLOHTL' :  [], symbol_wd[count]+'CLOCTOTHTL' : [],
			symbol_wd[count]+'CLOD' : []}
			
			dataArrayDay = numpy.genfromtxt(fname = main_input_path_wd , delimiter = ',',
			dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
					('close','f3'),('volume','i4'),('adjclose','f3')])
			
			date = []
			openn = []	#	openn because python will confuse open with the function "open".
			high = []
			low = []
			close = []
			volume = []
			adjclose = []
			
			date = dataArrayDay['date']
			openn = dataArrayDay['open']
			high = dataArrayDay['high']
			low = dataArrayDay['low']
			close = dataArrayDay['close']
			volume = dataArrayDay['volume']
			adjclose = dataArrayDay['adjclose']
					
			#	This part is where we calculate the ratio of close to open price
			#	based on week days.
			
			for j in range(len(date)):
				val = float(close[j])/float(openn[j])
				if val > 1.0:
					var_wd[symbol_wd[count]+'CGO'].append(val)
					var_wd[symbol_wd[count]+'CGOD'].append(date[j])
					var_wd[symbol_wd[count]+'CGOO'].append(openn[j])
					var_wd[symbol_wd[count]+'CGOC'].append(close[j])
					var_wd[symbol_wd[count]+'CGOH'].append(high[j])
					var_wd[symbol_wd[count]+'CGOL'].append(low[j])
					var_wd[symbol_wd[count]+'CGOV'].append(volume[j]*10**(-7))			
					var_wd[symbol_wd[count]+'CGOCTO'].append(float(close[j])/float(openn[j]))
					var_wd[symbol_wd[count]+'CGOHTL'].append(float(high[j])/float(low[j]))
					var_wd[symbol_wd[count]+'CGOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))
				elif val == 1.0:
					var_wd[symbol_wd[count]+'CEO'].append(val)
				else:
					var_wd[symbol_wd[count]+'CLO'].append(val)
					var_wd[symbol_wd[count]+'CLOD'].append(date[j])
					var_wd[symbol_wd[count]+'CLOO'].append(openn[j])
					var_wd[symbol_wd[count]+'CLOC'].append(close[j])
					var_wd[symbol_wd[count]+'CLOH'].append(high[j])
					var_wd[symbol_wd[count]+'CLOL'].append(low[j])
					var_wd[symbol_wd[count]+'CLOV'].append(volume[j]*10**(-7))			
					var_wd[symbol_wd[count]+'CLOCTO'].append(float(close[j])/float(openn[j]))
					var_wd[symbol_wd[count]+'CLOHTL'].append(float(high[j])/float(low[j]))
					var_wd[symbol_wd[count]+'CLOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))

			var_wd[symbol_wd[count]+'FG'].append(float(len(var_wd[symbol_wd[count]+'CGO']))/float(len(date)))
			var_wd[symbol_wd[count]+'FE'].append(float(len(var_wd[symbol_wd[count]+'CEO']))/float(len(date)))
			var_wd[symbol_wd[count]+'FL'].append(float(len(var_wd[symbol_wd[count]+'CLO']))/float(len(date)))
			var_wd[symbol_wd[count]+'Final'] = var_wd[symbol_wd[count]+'FG'] + var_wd[symbol_wd[count]+'FE'] + var_wd[symbol_wd[count]+'FL']

			if count % 5 == 0:
				counter = 0
				for i in symbol_total:
					if input_path_total is None:
						main_input_path_total = os.path.join(os.getcwd(), i)
					elif input_path_total is not None:
						main_input_path_total = os.path.join(os.path.expanduser(input_path_total), i)

					var_total = {symbol_total[counter]+'tCGO' :  [], symbol_total[counter]+'tCEO' :  [], symbol_total[counter]+'tCLO' : [],
					symbol_total[counter]+'tFG' :   [], symbol_total[counter]+'tFE' :   [], symbol_total[counter]+'tFL' : [],
					symbol_total[counter]+'tFcounternal': [], symbol_total[counter]+'tCGOCTO': [], symbol_total[counter]+'tCGOHTL' : [],
					symbol_total[counter]+'tCGOO' : [], symbol_total[counter]+'tCGOC' : [], symbol_total[counter]+'tCGOH' : [],
					symbol_total[counter]+'tCGOL' : [], symbol_total[counter]+'tCGOV' : [], symbol_total[counter]+'tCLOO' : [], 
					symbol_total[counter]+'tCLOC' : [], symbol_total[counter]+'tCLOH' : [], symbol_total[counter]+'tCLOL' : [], 
					symbol_total[counter]+'tCLOV' : [], symbol_total[counter]+'tCGOCTOTHTL': [], symbol_total[counter]+'tCGOD' : [],
					symbol_total[counter]+'tCLOCTO' : [], symbol_total[counter]+'tCLOHTL' : [], symbol_total[counter]+'tCLOCTOTHTL' : [],
					symbol_total[counter]+'tCLOD' : []}
					
					
					dataArrayTotal = numpy.genfromtxt(fname = main_input_path_total , delimiter = ',',
					dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
							('close','f3'),('volume','i4'),('adjclose','f3')])
		
					date = []
					openn = []	#	openn because python will confuse open with the function "open".
					high = []
					low = []
					close = []
					volume = []
					adjclose = []
					
					date = dataArrayTotal['date']
					openn = dataArrayTotal['open']
					high = dataArrayTotal['high']
					low = dataArrayTotal['low']
					close = dataArrayTotal['close']
					volume = dataArrayTotal['volume']
					adjclose = dataArrayTotal['adjclose']
			
					for j in range(len(date)):
						val = float(close[j])/float(openn[j])
						if val > 1.0:
							var_total[symbol_total[counter]+'tCGO'].append(val)
							var_total[symbol_total[counter]+'tCGOD'].append(date[j])
							var_total[symbol_total[counter]+'tCGOO'].append(openn[j])
							var_total[symbol_total[counter]+'tCGOC'].append(close[j])
							var_total[symbol_total[counter]+'tCGOH'].append(high[j])
							var_total[symbol_total[counter]+'tCGOL'].append(low[j])
							var_total[symbol_total[counter]+'tCGOV'].append(volume[j]*10**(-7))			
							var_total[symbol_total[counter]+'tCGOCTO'].append(float(close[j])/float(openn[j]))
							var_total[symbol_total[counter]+'tCGOHTL'].append(float(high[j])/float(low[j]))
							var_total[symbol_total[counter]+'tCGOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))
						elif val == 1.0:
							var_total[symbol_total[counter]+'tCEO'].append(val)
						else:
							var_total[symbol_total[counter]+'tCLO'].append(val)
							var_total[symbol_total[counter]+'tCLOD'].append(date[j])
							var_total[symbol_total[counter]+'tCLOO'].append(openn[j])
							var_total[symbol_total[counter]+'tCLOC'].append(close[j])
							var_total[symbol_total[counter]+'tCLOH'].append(high[j])
							var_total[symbol_total[counter]+'tCLOL'].append(low[j])
							var_total[symbol_total[counter]+'tCLOV'].append(volume[j]*10**(-7))			
							var_total[symbol_total[counter]+'tCLOCTO'].append(float(close[j])/float(openn[j]))
							var_total[symbol_total[counter]+'tCLOHTL'].append(float(high[j])/float(low[j]))
							var_total[symbol_total[counter]+'tCLOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))

					var_total[symbol_total[counter]+'tFG'].append(float(len(var_total[symbol_total[counter]+'tCGO']))/float(len(date)))
					var_total[symbol_total[counter]+'tFE'].append(float(len(var_total[symbol_total[counter]+'tCEO']))/float(len(date)))
					var_total[symbol_total[counter]+'tFL'].append(float(len(var_total[symbol_total[counter]+'tCLO']))/float(len(date)))
					var_total[symbol_total[counter]+'tFinal'] = var_total[symbol_total[counter]+'tFG'] + \
					var_total[symbol_total[counter]+'tFE'] + var_total[symbol_total[counter]+'tFL']
					
					counter += 1
			
			dic_wd.append(var_wd)
			dic_total.append(var_total)
			
			#~ if count == 4:
				#~ print 
				#~ print min(var[symbol_total[count]+'CGOCTOTHTL']), "< CGOCTOTHTL <" , max(var[symbol_total[count]+'CGOCTOTHTL'])
				#~ print "And the average value of CGOCTOTHTL is: ", sum(var[symbol_total[count]+'CGOCTOTHTL'])/len(var[symbol_total[count]+'CGOCTOTHTL'])
				#~ print 
			#~ #	This is where we find the average of a couple of prameters.
				#~ axb.set_yscale('log')
				#~ axb.plot(var[symbol_total[count]+'CGOD'], var[symbol_total[count]+'CGOCTOTHTL'], linestyle = '-',color = 'green')
				#~ axb.plot(var[symbol_total[count]+'CGOD'], var[symbol_total[count]+'CLOV'], linestyle = '-',color = 'red')
				#~ 
			#~ plt.close('all')
			labels = [r'$c>o$', '$c=o$', '$c<o$']
			colors = ['yellowgreen', 'gold', 'lightskyblue']
			explode=(0, 0, 0)
			axa[count1,count2].pie(var_wd[symbol_wd[count]+'Final'], explode = explode, 
			labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, 
			startangle = 90,)
			axa[count1,count2].set_aspect('equal')
			axa[count1,count2].set_title(days[count3], fontsize=10)
			
			count2 += 1
			if count2 == 3:
				count1 += 1
				count2 = 0
			count3 += 1
			if count % 5 == 0:
				count1 = 0
				count2 = 0
				count3 = 0
				fig1.delaxes(axa[1,2])
				fig1.suptitle(r"Ratio of close to open prices based on week days")
				fig1.savefig(main_output_path+'.png', format = 'png')
				fig1, axa = plt.subplots(2,3)

 	#~ plt.ion()
 	count4 = 0
 	count5 = 0
 	count6 = 0
	fig2, axb = plt.subplots(2,3)
	cutter = []
	for dic, key in zip(range(len(dic_wd)), symbol_wd):
		cutter.append(dic)
		x_ax = dic_wd[dic][key+'CGOD']
		y_ax = dic_wd[dic][key+'CGOCTOTHTL']
		axb[count4,count5].plot(x_ax, y_ax, linestyle = '-', color = 'green')

		count5 += 1
		if count5 == 3:	#	if statement for axis
			count4 += 1
			count5 = 0

		if len(cutter) % 5 == 0:
			count4 = 0
			count5 = 0
			fig2.suptitle(r"CGOCTOTHTL" + ' for ' + key[0:3])
			fig2.savefig(main_output_path+'CGOCTOTHTL' + key[0:3] +'.png', format = 'png')
			plt.show()
			fig2, axb = plt.subplots(2,3)
