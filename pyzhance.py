#~ #This is yet to begin.
import os

def data_downloader(readIn = "FALSE", symbol = None, startDate = None,
					endDate = None, outputPath = None,inputPath = None,
					inputFileName = None, outputFileName = None, 
					intraday = "FALSE", message = "FALSE"):
						
	# read_in: if set to "TRUE" the code will use the given text file 
	# to read in symbols from that file. Note that the user MUST provide
	# a path (i.e. inputPath) so the machine can find the file. Note that
	# if user sets the readIN option to "FALSE" a list of symbols MUST be
	# provided for the symbol argument (see below).
	# inputPath: is the path to the text file that this code will use to 
	# read in the symbols from the file (see above).
	# symbol: a list of symbols.
	# start_Date, end_Date: a date of the 'yyyy-mm-dd' format with 
	# quotation marks.
	# outputPath: a path to tell the machine where to save the output. 
	# The default is the current directory.
	# file_name: User can set a name for the output file.
	# intraday: if it is set to "TRUE" the code will download the intr
	# day information of the symbols and ignores the given dates. The de
	# fault is "FALSE" and it downloads the data based on the given dates.
	# message: if set to "TRUE" it prints out some information a long 
	# the procedure such as the data of what symbol is downloading. The 
	# default is "FALSE" so it does NOT print out anything.
	
	
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
	
	# Things to do for tomorrow:
	# 1- url section needs to be shortened.
	# 2- the rest nameFile section needs to be reviewed and think about
	# adding a new argument as the list of the output names.
	
#	type(datetime.datetime.strftime(datetime.datetime.fromtimestamp(1457706672), "%Y-%m-%d"))
#	<type 'str'>

#	http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=1d/csv
	
	import os
	import sys
	import time
	import urllib2

#	outputPath = '~/nozhan/science/computation/data/finance/output/code/pyzhance/data_downloader'
		
	if readIn == "TRUE":
		if inputPath is None:
			file = os.path.join(os.getcwd(),inputFileName)
		elif inputPath is not None:
			file = os.path.join(inputPath,inputFileName)
		symbolRead = open(file,'r')
		symbol = []
		for line in symbolRead:
			symbol.append(line.strip()) # The strip command removes 
		symbolRead.close()				# unwanted empty space of each
		#~ print(symbol)					# line when it is reading the file.
		#~ sys.exit("********It worked just fine.*******")
	
	if outputPath is None:
		outputPath = os.getcwd()
	
	if inputPath is None:
		inputPath = os.getcwd()


	outPath = os.path.join(outputPath)
	sDate = startDate.split("-")
	a = str(int(sDate[1]) - 1)	# month (I added a -1 so it matched the yahoo format)
	b = sDate[2]	# day
	c = sDate[0]	# year
	eDate = endDate.split("-")
	d = str(int(eDate[1]) - 1)	# month (same as above)
	e = eDate[2]	# day
	f = eDate[0]	# year
	storeName = []
	
	if fileName is None:
		fileName = symbol
	if intraday == "FALSE":
		for sym in fileName:
			storeName.extend([sym])
			file = outPath + sym + ".csv"
			downloadFile = open(file, "w")
			urlToRead = "http://real-chart.finance.yahoo.com/table.csv?s="+sym+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g=d&ignore=.csv"
			sourceCode = urllib2.urlopen(urlToRead).read()
			downloadFile.write(sourceCode)
			downloadFile.close()
			if message == "TRUE":
				print
				print(sym+".csv ---> downloaded")
				print
	if intraday == "TRUE":
		for sym in fileName:
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
			time.sleep(3)
			
			
			
			
'''			
def datetime_convertor(input_file = None, column_number = None, 
						outputPath = os.getcwd(), input_format = None, 
						output_format = None, output_file = None):
	import numpy
	import datetime
	# name of the file
	# name/number of the column(s)
	# format to read (format of the input data)
	# format to convert to (format of the output data)
	# name of the file to be written to (the output file)
	
	for name in input_file:
		for column in column_number:
			numpy.genfromtxt(fname = input_file, usecols = column_number)
'''	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
