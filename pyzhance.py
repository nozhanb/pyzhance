
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

def data_slicer(symbol, date_day, interval, inputFileName = None, 
				outputPath = None, inputPath = None,
				day = None, month = None, year = None,
				letterSearch = False, letterDay = None, 
				outputFileName = None):
		
		#	write = if "TRUE" the code will write out the result to a 
		#	file. The default is "FALSE".

#	for the first part.
#~ pyzhance.data_slicer(symbol = ['DIS'], date_day = [('2010-01-26','2011-07-27'),('2012-05-01', '2013-05-30'), ('2014-05-20','2016-06-30')], interval = [('2010-01-22','2016-07-01')])

		
	import os
	import sys
	import numpy
	import datetime

	for inputs in symbol:
		#~ if inputPath is not None:
			#~ inputPathFile = os.path.join(os.path.expanduser(inputPath),inputs)
		#~ elif inputPath is None:
			#~ inputPathFile = os.path.join(os.getcwd(),inputs)
		#~ if outputPath is None:
			#~ outputPath = os.getcwd()
		#~ elif outputPath is not None:
			#~ outputPath = os.path.expanduser(outputPath)
		#~ if outputFileName is None:
			#~ outputFileName = os.path.join(os.getcwd(), inputs)
		#~ elif outputFileName is not None:
			#~ outputFileName = os.path.join(os.path.expanduser(inputPath), outputFileName)
			
			
		def date_converter(tag): # tag: German word for day.
			dateFormat = '%Y-%m-%d'
			convertedDate = datetime.datetime.strptime(tag,dateFormat)
			ordinalDate = datetime.date.toordinal(convertedDate)
			return ordinalDate
			#~ print ordinalDate
		
		#	NOTE: Do NOT use the dtype argument or you will get the "Too many
		#	values to unpack". The best way is to use the "strpdate2num" function 
		#	and the "converters" argument as follows.

		dataArray = numpy.genfromtxt(fname = inputs, delimiter = ",", 
		dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
		('close','f3'),('volume','i4'),('adjclose','f3')],converters = {0:date_converter})
		
		dic1 = {'date_{}'.format(inputs): dataArray['date'], 'open_{}'.format(inputs): dataArray['open'], 
		'high_{}'.format(inputs): dataArray['high'], 'low_{}'.format(inputs): dataArray['low'], 
		'close_{}'.format(inputs): dataArray['close'], 'volume_{}'.format(inputs): dataArray['volume'], 
		'adjclose_{}'.format(inputs): dataArray['adjclose']}
		
		for sdate, edate in interval:
			startdate1 = datetime.datetime.strptime(sdate, '%Y-%m-%d')
			enddate1 = datetime.datetime.strptime(edate, '%Y-%m-%d')
			startdate2 = datetime.date.toordinal(startdate1)
			enddate2 =  datetime.date.toordinal(enddate1)
			datearray = numpy.array(range(startdate2, enddate2 + 1))
			
			for day in date_day:
				if isinstance(day, tuple) == True:	#	this line checks to see if the day object is a list.
					startdate3, enddate3 = day
					if len(startdate3) ==  10:
						startdate4 = datetime.datetime.strptime(startdate3, '%Y-%m-%d')
						enddate4 = datetime.datetime.strptime(enddate3, '%Y-%m-%d')
						startdate5 = datetime.date.toordinal(startdate4)
						enddate5 =  datetime.date.toordinal(enddate4)
						index = []
						if enddate7 < dic1['date_{}'.format(inputs)][0]:
							while len(index) < 2:
								for count1 in list(reversed(range(len(dic1['date_{}'.format(inputs)])))):
									if startdate5 == dic1['date_{}'.format(inputs)][count1]:
										index1 = count1
										index.append((index1, 0))
									elif enddate5 == dic1['date_{}'.format(inputs)][count1]:
										index2 = count1
										index.append((index2, 1))
								if len(index) == 1:
									if index[0][1] == 0:
										enddate5 += 1
										index = []
									elif index[0][1] == 1:
										startdate5 += 1
										index = []
								elif len(index) == 0:
									startdate5 += 1
									enddate5 += 1
									index = []
							with open(inputs+'_'+sdate+'_'+edate, 'a') as ftw:
								for count2 in range(index[0][0], index[1][0] - 1, -1):
									ftw.write('{}\t{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n'.format(
									datetime.date.fromordinal(dic1['date_{}'.format(inputs)][count2]),
									dic1['date_{}'.format(inputs)][count2], dic1['open_{}'.format(inputs)][count2], 
									dic1['high_{}'.format(inputs)][count2], dic1['low_{}'.format(inputs)][count2], 
									dic1['close_{}'.format(inputs)][count2], dic1['adjclose_{}'.format(inputs)][count2], 
									dic1['volume_{}'.format(inputs)][count2]))
						
						elif enddate7 > dic1['date_{}'.format(inputs)][0]:
							break
	
					elif len(startdate3) == 5:
						startdate4 = datetime.datetime.strptime(startdate3, '%m-%d')
						enddate4 = datetime.datetime.strptime(enddate3, '%m-%d')
						startdate5 = datetime.date.toordinal(startdate4)
						enddate5 =  datetime.date.toordinal(enddate4)
						if startdate5 != enddate5:
							startyear1 = startdate1.strftime('%Y')
							endyear1 = enddate1.strftime('%Y')
							#	some where around here I have to check the end of the interval to make sure if 
							#	the end of interval falls in the total interval I have. Something like a loop or
							#	... If it does not then I have to tell the code that ignore the last cycle and 
							#	just print out the output based on what we have from the previous cycles.
							for count3 in range(abs(int(startyear1) - int(endyear1)) + 1):
								startdate6 = datetime.datetime.strptime(str(int(startyear1) + count3) +'-'+ startdate3,'%Y-%m-%d')
								enddate6 = datetime.datetime.strptime(str(int(startyear1) + count3) +'-'+ enddate3,'%Y-%m-%d')
								startdate7 = datetime.date.toordinal(startdate6)
								enddate7 = datetime.date.toordinal(enddate6)
								index = []
								if enddate7 < dic1['date_{}'.format(inputs)][0]:
									while len(index) < 2:
										for count4 in list(reversed(range(len(dic1['date_{}'.format(inputs)])))):
											if startdate7 == dic1['date_{}'.format(inputs)][count4]:
												index3 = count4
												index.append((index3,0))
											elif enddate7 == dic1['date_{}'.format(inputs)][count4]:
												index4 = count4
												index.append((index4,1))
										if len(index) == 1:
											if index[0][1] == 0:
												enddate7 += 1
												index = []
											elif index[0][1] == 1:
												startdate7 += 1
												index = []
										elif len(index) == 0:
											startdate7 += 1
											enddate7 += 1
											index = []
									with open(inputs+'_'+startdate3+'_'+enddate3, 'a') as ftw:
										for count5 in range(index[0][0], index[1][0] - 1, -1):
											ftw.write('{}\t{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n'.format(
											datetime.date.fromordinal(dic1['date_{}'.format(inputs)][count5]), 
											dic1['date_{}'.format(inputs)][count5], dic1['open_{}'.format(inputs)][count5], 
											dic1['high_{}'.format(inputs)][count5], dic1['low_{}'.format(inputs)][count5], 
											dic1['close_{}'.format(inputs)][count5], dic1['adjclose_{}'.format(inputs)][count5], 
											dic1['volume_{}'.format(inputs)][count5]))
				
								elif enddate7 > dic1['date_{}'.format(inputs)][0]:
									break
															
						elif startdate5 == enddate5:
							startyear2 = startdate1.strftime('%Y')
							endyear2 = enddate1.strftime('%Y')
							for count6 in range(abs(int(startyear2) - int(endyear2)) + 1):
								startdate8 = datetime.datetime.strptime(str(int(startyear1) + count3) +'-'+ startdate3,'%Y-%m-%d')
								startdate9 = datetime.date.toordinal(startdate8)
								index = []
								if enddate7 < dic1['date_{}'.format(inputs)][0]:
									while len(index) < 1:
										for count7 in list(reversed(range(len(dic1['date_{}'.format(inputs)])))):
											if startdate9 == dic1['date_{}'.format(inputs)][count7]:
												index5 = count7
												index.append(index5)
										if len(index) == 0:
												startdate9 += 1
									with open(inputs+'_'+startdate3+'_'+enddate3, 'a') as ftw:
										for val in index:
											ftw.write('{}\t{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n'.format(
											datetime.date.fromordinal(dic1['date_{}'.format(inputs)][val]), 
											dic1['date_{}'.format(inputs)][val], dic1['open_{}'.format(inputs)][val], 
											dic1['high_{}'.format(inputs)][val], dic1['low_{}'.format(inputs)][val], 
											dic1['close_{}'.format(inputs)][val], dic1['adjclose_{}'.format(inputs)][val], 
											dic1['volume_{}'.format(inputs)][val]))
								elif enddate7 > dic1['date_{}'.format(inputs)][0]:
									break
						else:
							startdate10 = datetime.datetime.strptime(startdate3, '%d')
							enddate8 = datetime.datetime.strptime(enddate3, '%d')
							startdate11 = datetime.date.toordinal(startdate10)
							enddate9 = datetime.date.toordinal(enddate8)	
							if startdate11 != enddate9:
								startyear3 = startdate1.strftime('%Y')
								endyear3 = enddate1.strftime('%Y')
								startmonth1 = startdate1.strftime('%m')
								endmonth1 = enddate1.strftime('%m')
								for count8 in range(abs(int(startyear3) - int(endyear3)) + 1):
									if count8 == startyear3:
										startmonth1 = startmonth1
										end = 13
									elif count8 == endyear3:
										startmonth1 = 01
										end = int(endmonth1)
									else:
										startmonth1 = '13' 
										end = 13
																					
									for count9 in range(int(startmonth1), end):
										startdate12 = datetime.datetime.strptime(str(int(startyear1) + count8) +'-'+ str(int(startmonth1) + count9) +'-'+ startdate3,'%Y-%m-%d')
										enddate10 = datetime.datetime.strptime(str(int(startyear1) + count8) +'-'+ str(int(startmonth1) + count9) + '-' + enddate3,'%Y-%m-%d')
										startdate13 = datetime.date.toordinal(startdate12)
										enddate11 = datetime.date.toordinal(enddate10)
										index = []
										if enddate7 < dic1['date_{}'.format(inputs)][0]:
											while len(index) < 2:
												for count10 in list(reversed(range(len(dic1['date_{}'.format(inputs)])))):
													if startdate14 == dic1['date_{}'.format(inputs)][count10]:
														index6 = count10
														index.append((count10,0))
													elif enddate12 == dic1['date_{}'.format(inputs)][count10]:
														index7 = count10
														index.append((count10,1))
												if len(index) == 1:
													if index[0][1] == 0:
														enddate12 += 1
														index = []
													elif index[0][1] == 1:
														startdate14 += 1
														index = []
												elif len(index) == 0:
													startdate14 += 1
													enddate12 += 1
													index = []
											with open(inputs+'_'+startdate3+'_'+enddate3, 'a') as ftw:
												for val2 in range(index[0][0], index[1][0] - 1, -1):
													ftw.write('{}\t{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n'.format(
													datetime.date.fromordinal(dic1['date_{}'.format(inputs)][val2]), 
													dic1['date_{}'.format(inputs)][val2], dic1['open_{}'.format(inputs)][val2], 
													dic1['high_{}'.format(inputs)][val2], dic1['low_{}'.format(inputs)][val2], 
													dic1['close_{}'.format(inputs)][val2], dic1['adjclose_{}'.format(inputs)][val2], 
													dic1['volume_{}'.format(inputs)][val2]))
										elif enddate7 > dic1['date_{}'.format(inputs)][0]:
											break
											
							elif startdate11 == enddate9:
								startyear3 = startdate1.strftime('%Y')
								endyear3 = enddate1.strftime('%Y')
								startmonth1 = startdate1.strftime('%m')
								endmonth1 = enddate1.strftime('%m')
								for count11 in range(int(startyear3), int(endyear3) + 1):
									if count11 == startyear3:
										startmonth1 = startmonth1
										end = 13
									elif count11 == endyear3:
										startmonth1 = 01
										end = int(endmonth1)
									else:
										startmonth1 = '13' 
										end = 13
																					
									for count12 in range(int(startmonth1), end):
										startdate12 = datetime.datetime.strptime(str(int(startyear1) + count12) +'-'+ str(int(startmonth1) + count12) +'-'+ startdate3,'%Y-%m-%d')
										startdate13 = datetime.date.toordinal(startdate12)
										index = []
										if enddate7 < dic1['date_{}'.format(inputs)][0]:
											while len(index) < 1 :
												for count13 in list(reversed(range(len(dic1['date_{}'.format(inputs)])))):
													if startdate14 == dic1['date_{}'.format(inputs)][count13]:
														index8 = count13
														index.append(count13)
												if len(index) == 0:
													startdate13 += 1
											with open(inputs+'_'+startdate3+'_'+enddate3, 'a') as ftw:
												for val3 in index:
													ftw.write('{}\t{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n'.format(
													datetime.date.fromordinal(dic1['date_{}'.format(inputs)][val3]), 
													dic1['date_{}'.format(inputs)][val3], dic1['open_{}'.format(inputs)][val3], 
													dic1['high_{}'.format(inputs)][val3], dic1['low_{}'.format(inputs)][val3], 
													dic1['close_{}'.format(inputs)][val3], dic1['adjclose_{}'.format(inputs)][val3], 
													dic1['volume_{}'.format(inputs)][val3]))
										elif enddate7 > dic1['date_{}'.format(inputs)][0]:
											break
		
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

#~ (symbol = ['DIS0thMon','DIS0thTue','DIS0thWed','DIS0thThu','DIS0thFri','KO0thMon','KO0thTue','KO0thWed','KO0thThu','KO0thFri'],ratios = [('close','open')], cTo = True, output_path = '~/nozhan/science/computation/data/finance/output/code/pyzhance/ratio_weekday')


def ratio(symbol , input_path_wd = None, ratios = None, input_path_total = None, output_path = None, 
			output_file = 'single', sign = 'minus', previous_day = 'ON'):

	#	This function will find differeant ratios for different stocks 
	#	based on weekdays.	cMoThMl
	
	#	symbol_wd: is the list of file names where each file contains
	#	the data of a symbol based on single week days of a given interval.
	#	symbol_total: is the list of file names where each file contains
	#	the data of a symbol for all days of a given interval.

#####
#NOTE:	If the user sets the previous_day == 'ON' then it is better to give the ratios argument a tuple such as ('open', 'close',
#		'volume', 'volume') so one will not encounter division by zero. However, if one would like to set the previous-day to 'OFF'
#		then it is recommanded to change the divison from two 'volume' in denominator to one (i.e. ratios = (open, close, volume). 
#		This way the user will not get a error message or division by zero.
#####
	counter1 = 0
	dic3 = {}
	for i in symbol:
		if input_path_wd is None:
			main_input_path_wd = os.path.join(os.getcwd(), i)
		elif input_path_wd is not None:
			main_input_path_wd = os.path.join(os.path.expanduser(input_path_wd), i)				
		if output_path is None:
			main_output_path = os.path.join(os.getcwd(), i)
		elif output_path is not None:
			main_output_path = os.path.join(os.path.expanduser(output_path), i)
		
		#	We creat a dictionary of different varibles.
		
		#	POTPCGone stands for Present day's Open To Previous day's Close Greater than one.
		#	PVTPVGone stands for Present day's Volume To Previous day's Volume for days with POTPCGone.
		# 	The same holds true for other abbreviations of THIS group.
		dataArrayDay = numpy.genfromtxt(fname = main_input_path_wd , delimiter = ',',
		dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
				('close','f3'),('volume','i4'),('adjclose','f3')])
		
		dic1 = {'date_{}'.format(i): dataArrayDay['date'], 'open_{}'.format(i): dataArrayDay['open'], 
		'high_{}'.format(i): dataArrayDay['high'], 'low_{}'.format(i): dataArrayDay['low'], 
		'close_{}'.format(i): dataArrayDay['close'], 'volume_{}'.format(i): dataArrayDay['volume'], 
		'adjclose_{}'.format(i): dataArrayDay['adjclose']}

		#	This part is where we calculate different ratios
		
		counter2 = 0
		for rr in ratios:
			if previous_day == 'OFF':
				if len(rr) == 2:
					numerator = rr[0]
					denominator = rr[1]
					value = numpy.divide(dic1[numerator+'_{}'.format(i)], dic1[denominator+'_{}'.format(i)])
				elif len(rr) == 3:
					numerator1  = rr[0]
					numerator2  = rr[1]
					denominator = rr[2]
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(i)] - dic1[numerator2+'_{}'.format(i)], dic1[denominator+'_{}'.format(i)])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(i)] + dic1[numerator2+'_{}'.format(i)], dic1[denominator+'_{}'.format(i)])
				else:
					numerator1  = rr[0]
					numerator2  = rr[1]
					denominator1 = rr[2]
					denominator2 = rr[3]
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(i)] - dic1[numerator2+'_{}'.format(i)], dic1[denominator1+'_{}'.format(i)] - dic1[denominator2+'_{}'.format(i)])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(i)] + dic1[numerator2+'_{}'.format(i)], dic1[denominator1+'_{}'.format(i)] + dic1[denominator2+'_{}'.format(i)])

			elif previous_day == 'ON':
				if len(rr) == 4:
					numerator1  = rr[0]		#	present day
					numerator2  = rr[1]		#	previous day
					denominator1 = rr[2]	#	present day 
					denominator2 = rr[3]	#	previous day
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(i)][1:] - dic1[numerator2+'_{}'.format(i)][:len(dic1[numerator2+'_{}'.format(i)]) - 1], 
						dic1[denominator1+'_{}'.format(i)][1:] - dic1[denominator2+'_{}'.format(i)][:len(dic1[denominator2+'_{}'.format(i)]) - 1])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(i)][1:] + dic1[numerator2+'_{}'.format(i)][:len(dic1[numerator2+'_{}'.format(i)]) - 1], 
						dic1[denominator1+'_{}'.format(i)][1:] + dic1[denominator2+'_{}'.format(i)][:len(dic1[denominator2+'_{}'.format(i)]) - 1])

			dic2 = {i + '_ratio': value}
			dic3.update(dic2)
			
			#~ curly.append('{:011.6f}\t')
			#~ if counter2 == len(ratios):
				#~ curly.append('{:011.6f}\t\n') 
			counter2 += 1
			#~ for count4 in range(len(curly)):
				#~ if count4 == 0:
					#~ form1 = curly[count4]
					#~ form = form1
				#~ if count4 > 0:
					#~ form1 =curly[count4]
					#~ form = form + form1
							
		dic3.update(dic1)
		with open(i + '_ratio', 'w') as ftw:	#	ftw stands for file to write!
			if previous_day == 'OFF':
				for count3 in range(len(dic3['date_{}'.format(i)])):
					ftw.write("{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{<:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n".format(dic3['date_{}'.format(i)][count3], 
					dic3['open_{}'.format(i)][count3], dic3['high_{}'.format(i)][count3], dic3['low_{}'.format(i)][count3], 
					dic3['close_{}'.format(i)][count3], dic3[i + '_ratio'.format(i)][count3],dic3['adjclose_{}'.format(i)][count3], 
					dic3['volume_{}'.format(i)][count3]))
			elif previous_day == 'ON':
				for count3 in range(len(dic3[i + '_ratio'.format(i)])):
					ftw.write("{}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{:011.6f}\t{}\n".format(dic3['date_{}'.format(i)][count3], 
					dic3['open_{}'.format(i)][count3], dic3['high_{}'.format(i)][count3], dic3['low_{}'.format(i)][count3], 
					dic3['close_{}'.format(i)][count3], dic3[i + '_ratio'.format(i)][count3],dic3['adjclose_{}'.format(i)][count3], 
					dic3['volume_{}'.format(i)][count3]))
		counter1 += 1


	'''
			for j in range(len(date)):
				var_wd[symbol[count]+'date'].append(date[j])
				var_wd[symbol[count]+'open'].append(openn[j])
				var_wd[symbol[count]+'close'].append(close[j])
				var_wd[symbol[count]+'high'].append(high[j])
				var_wd[symbol[count]+'low'].append(low[j])
				var_wd[symbol[count]+'volume'].append(volume[j])
				var_wd[symbol[count]+'adjclose'].append(adjclose[j])

				
				var_wd[symbol_wd[count]+'CGOCTO'].append(float(close[j])/float(openn[j]))
				var_wd[symbol_wd[count]+'CGOHTL'].append(float(high[j])/float(low[j]))
				#~ var_wd[symbol_wd[count]+'CGOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))
				var_wd[symbol_wd[count]+'CGOCTOTHTL'].append(float(high[j]/openn[j]))

				if j > 0:
					ratio1 = openn[j]/close[j-1]
					if ratio1 > 1:
						var_wd[symbol_wd[count]+'POTPCGone'].append(ratio1)
						var_wd[symbol_wd[count]+'POTPCDGone'].append(date[j])
						var_wd[symbol_wd[count]+'PVTPVGone'].append(float(volume[j])/float(volume[j-1]))
					elif ratio1 == 1:
						var_wd[symbol_wd[count]+'POTPCEone'].append(ratio1)
						var_wd[symbol_wd[count]+'POTPCDEone'].append(date[j])
						var_wd[symbol_wd[count]+'PVTPVEone'].append(float(volume[j])/float(volume[j-1]))
					else:
						var_wd[symbol_wd[count]+'POTPCLone'].append(ratio1)
						var_wd[symbol_wd[count]+'POTPCDLone'].append(date[j])
						var_wd[symbol_wd[count]+'PVTPVLone'].append(float(volume[j])/float(volume[j-1]))

			var_wd[symbol_wd[count]+'FG'].append(float(len(var_wd[symbol_wd[count]+'CGO']))/float(len(date)))
			var_wd[symbol_wd[count]+'FE'].append(float(len(var_wd[symbol_wd[count]+'CEO']))/float(len(date)))
			var_wd[symbol_wd[count]+'FL'].append(float(len(var_wd[symbol_wd[count]+'CLO']))/float(len(date)))
			var_wd[symbol_wd[count]+'Final'] = var_wd[symbol_wd[count]+'FG'] + var_wd[symbol_wd[count]+'FE'] + var_wd[symbol_wd[count]+'FL']
			
			#	symbol_total averaging section
			cc = 0
			for ii in range(len(var_wd[symbol_wd[count]+'CGOCTOTHTL'])):
				aa = var_wd[symbol_wd[count]+'CGOCTOTHTL'][ii]
				cc = cc + aa
			var_wd[symbol_wd[count]+'CGOCTOTHTL_AV'].append(float(cc)/float(len(var_wd[symbol_wd[count]+'CGOCTOTHTL'])))

			empG = []	#	I introduce this empty list to use it to find the variance.
			for iii in range(len(var_wd[symbol_wd[count]+'CGOCTOTHTL'])):
				empG.append((var_wd[symbol_wd[count]+'CGOCTOTHTL'][iii] - var_wd[symbol_wd[count]+'CGOCTOTHTL_AV'][0]) ** 2)
			varG = float(sum(empG))/float(len(var_wd[symbol_wd[count]+'CGOCTOTHTL']))
			stdG = numpy.sqrt(varG)

			dd = 0
			for jj in range(len(var_wd[symbol_wd[count]+'CLOCTOTHTL'])):
				bb = abs(var_wd[symbol_wd[count]+'CLOCTOTHTL'][jj])
				dd = dd + bb
			var_wd[symbol_wd[count]+'CLOCTOTHTL_AV'].append(float(dd)/float(len(var_wd[symbol_wd[count]+'CLOCTOTHTL'])))
			empL = []	#	I introduce this empty list to use it to find the variance.
			for iii in range(len(var_wd[symbol_wd[count]+'CLOCTOTHTL'])):
				empL.append((var_wd[symbol_wd[count]+'CLOCTOTHTL'][iii] - var_wd[symbol_wd[count]+'CLOCTOTHTL_AV'][0]) ** 2)
			varL = float(sum(empL))/float(len(var_wd[symbol_wd[count]+'CLOCTOTHTL']))
			stdL = numpy.sqrt(varL)
			
			cutter1.append(count)
			
			if len(cutter1) % 5 == 0:
				if input_path_total is None:
					main_input_path_total = os.path.join(os.getcwd(), symbol_total[counter])
				elif input_path_total is not None:
					main_input_path_total = os.path.join(os.path.expanduser(input_path_total), symbol_total[counter])

				var_total = {symbol_total[counter]+'tCGO' :  [], symbol_total[counter]+'tCEO' :  [], symbol_total[counter]+'tCLO' : [],
				symbol_total[counter]+'tFG' :   [], symbol_total[counter]+'tFE' :   [], symbol_total[counter]+'tFL' : [],
				symbol_total[counter]+'tFcounternal': [], symbol_total[counter]+'tCGOCTO': [], symbol_total[counter]+'tCGOHTL' : [],
				symbol_total[counter]+'tCGOO' : [], symbol_total[counter]+'tCGOC' : [], symbol_total[counter]+'tCGOH' : [],
				symbol_total[counter]+'tCGOL' : [], symbol_total[counter]+'tCGOV' : [], symbol_total[counter]+'tCLOO' : [], 
				symbol_total[counter]+'tCLOC' : [], symbol_total[counter]+'tCLOH' : [], symbol_total[counter]+'tCLOL' : [], 
				symbol_total[counter]+'tCLOV' : [], symbol_total[counter]+'tCGOCTOTHTL': [], symbol_total[counter]+'tCGOD' : [],
				symbol_total[counter]+'tCLOCTO' : [], symbol_total[counter]+'tCLOHTL' : [], symbol_total[counter]+'tCLOCTOTHTL' : [],
				symbol_total[counter]+'tCLOD' : [], symbol_total[counter]+'tCGOCTOTHTL_AV': [],symbol_total[counter]+'tCLOCTOTHTL_AV': [],
				symbol_total[counter]+'tPOTPCGone' : [], symbol_total[counter]+'tPOTPCEone' : [], symbol_total[counter]+'tPOTPCLone' : [],
				symbol_total[counter]+'tPVTPVGone' : [], symbol_total[counter]+'tPVTPVEone' : [], symbol_total[counter]+'tPVTPVLone' : []}
				
				
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
						var_total[symbol_total[counter]+'tCGOV'].append(volume[j])			
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
						var_total[symbol_total[counter]+'tCLOV'].append(volume[j])			
						var_total[symbol_total[counter]+'tCLOCTO'].append(float(close[j])/float(openn[j]))
						var_total[symbol_total[counter]+'tCLOHTL'].append(float(high[j])/float(low[j]))
						var_total[symbol_total[counter]+'tCLOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))
						

					if j > 0:
						ratio2 = float(openn[j])/float(close[j-1])
						if ratio2 > 1:
							var_total[symbol_total[counter]+'tPOTPCGone'].append(ratio2)
							var_total[symbol_total[counter]+'tPVTPVGone'].append(float(volume[j])/float(volume[j-1]))
							
						elif ratio2 == 1:
							var_total[symbol_total[counter]+'tPOTPCEone'].append(ratio2)
							var_total[symbol_total[counter]+'tPVTPVEone'].append(float(volume[j])/float(volume[j-1]))
						else:
							var_total[symbol_total[counter]+'tPOTPCLone'].append(ratio2)
							var_total[symbol_total[counter]+'tPVTPVLone'].append(float(volume[j])/float(volume[j-1]))

				var_total[symbol_total[counter]+'tFG'].append(float(len(var_total[symbol_total[counter]+'tCGO']))/float(len(date)))
				var_total[symbol_total[counter]+'tFE'].append(float(len(var_total[symbol_total[counter]+'tCEO']))/float(len(date)))
				var_total[symbol_total[counter]+'tFL'].append(float(len(var_total[symbol_total[counter]+'tCLO']))/float(len(date)))
				var_total[symbol_total[counter]+'tFinal'] = var_total[symbol_total[counter]+'tFG'] + \
				var_total[symbol_total[counter]+'tFE'] + var_total[symbol_total[counter]+'tFL']
				
				#	symbol_total averaging section
				cc = 0
				for ii in range(len(var_total[symbol_total[counter]+'tCGOCTOTHTL'])):
					aa = var_total[symbol_total[counter]+'tCGOCTOTHTL'][ii]
					cc = cc + aa
				var_total[symbol_total[counter]+'tCGOCTOTHTL_AV'].append(float(cc)/float(len(var_total[symbol_total[counter]+'tCGOCTOTHTL'])))
				empG = []	#	I introduce this empty list to use it to find the variance.
				for iii in range(len(var_total[symbol_total[counter]+'tCGOCTOTHTL'])):
					empG.append((var_total[symbol_total[counter]+'tCGOCTOTHTL'][iii] - var_total[symbol_total[counter]+'tCGOCTOTHTL_AV'][0]) ** 2)
				varG = float(sum(empG))/float(len(var_total[symbol_total[counter]+'tCGOCTOTHTL']))
				stdG = numpy.sqrt(varG)

				dd = 0
				for jj in range(len(var_total[symbol_total[counter]+'tCLOCTOTHTL'])):
					bb = abs(var_total[symbol_total[counter]+'tCLOCTOTHTL'][jj])
					dd = dd + bb
				var_total[symbol_total[counter]+'tCLOCTOTHTL_AV'].append(float(dd)/float(len(var_total[symbol_total[counter]+'tCLOCTOTHTL'])))
				empL = []	#	I introduce this empty list to use it to find the variance.
				for iii in range(len(var_total[symbol_total[counter]+'tCLOCTOTHTL'])):
					empL.append((var_total[symbol_total[counter]+'tCLOCTOTHTL'][iii] - var_total[symbol_total[counter]+'tCLOCTOTHTL_AV'][0]) ** 2)
				varL = float(sum(empL))/float(len(var_total[symbol_total[counter]+'tCLOCTOTHTL']))
				stdL = numpy.sqrt(varL)
				
				dic_total.append(var_total)
				
				counter += 1
			
			dic_wd.append(var_wd)
	
			labels = [r'$c>o$', '$c=o$', '$c<o$']
			colors = ['yellowgreen', 'gold', 'lightskyblue']
			explode=(0, 0, 0)
			axa[count1,count2].pie(var_wd[symbol_wd[count]+'Final'], explode = explode, 
			labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, 
			startangle = 90,)	
			axa[count1,count2].set_aspect('equal')
			axa[count1,count2].set_title(days[count3], fontsize=10)
			cutter2.append(count)	#	I add this line to use it as a cutter in the following if statement.
			
			count2 += 1
			if count2 == 3:
				count1 += 1
				count2 = 0
			count3 += 1		#	count3 is used for counting days of the week.
			
			if len(cutter2) % 5 == 0:
				count1 = 0
				count2 = 0
				count3 = 0
				fig1.delaxes(axa[1,2])
				fig1.suptitle(r"close to open price-ratio based on week days for " + symbol_total[count6])
				fig1.savefig(main_output_path+'.png', format = 'png')
				if len(cutter2) < len(symbol_wd):	#	If this "if statement" (and the similar one below) 
					fig1, axa = plt.subplots(2,3)	#	gets removed there will be two more empty figures.
				count6 += 1
			count += 1
				
			#~ plt.ion()
 	count4 = 0
 	count5 = 0
 	count7 = 0
	fig2, axb = plt.subplots(2,3)
	for dic, key in zip(range(len(dic_wd)), symbol_wd):
		cutter3.append(dic)
#		x_ax = dic_wd[dic][key+'POTPCDGone']
		y_ax = dic_wd[dic][key+'PVTPVLone']
		x_ax = dic_wd[dic][key+'POTPCLone']
		axb[count4,count5].plot(x_ax, y_ax, 'o', color = 'green')
		#~ y_ax = dic_wd[dic][key+'CGOCTOTHTL']
#		x_ax = dic_wd[dic][key+'POTPCDGone']
#		z_ax = dic_wd[dic][key+'PVTPVGone']
		#~ z_ax = [i/max(dic_wd[dic][key+'CGOV']) for i in dic_wd[dic][key+'CGOV']]
#		axb[count4,count5].plot(x_ax, z_ax, linestyle = '-', color = 'red')

		count5 += 1
		if count5 == 3:	#	if statement for axis
			count4 += 1
			count5 = 0
	
		if len(cutter3) % 5 == 0:
			count4 = 0
			count5 = 0
			fig2.delaxes(axb[1,2])
			#~ fig2.suptitle(r"CGOCTOTHTL" + ' for ' + symbol_total[count7])
			fig2.suptitle(r"CGOHmO" + ' for ' + symbol_total[count7])
			fig2.savefig(main_output_path+'CGOCTOTHTL' + symbol_total[count7] +'.png', format = 'png')
			if len(cutter3) < len(dic_wd):
				fig2, axb = plt.subplots(2,3)
			count7 += 1
	plt.show()
'''


'''
			axa[count1,count2].pie(var_wd[symbol_wd[count]+'Final'], explode = explode, 
			labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, 
			startangle = 90,)
			axa[count1,count2].set_aspect('equal')
			axa[count1,count2].set_title(days[count3], fontsize=10)
			cutter2.append(count)	#	I add this line to use it as a cutter in the following if statement.
			
			count2 += 1
			if count2 == 3:
				count1 += 1
				count2 = 0
			count3 += 1		#	count3 is used for counting days of the week.
			
			if len(cutter2) % 5 == 0:
				count1 = 0
				count2 = 0
				count3 = 0
				fig1.delaxes(axa[1,2])
				fig1.suptitle(r"close to open price-ratio based on week days for " + symbol_total[count6])
				fig1.savefig(main_output_path+'.png', format = 'png')
				if len(cutter2) < len(symbol_wd):	#	If this "if statement" (and the similar one below) 
					fig1, axa = plt.subplots(2,3)	#	gets removed there will be two more empty figures.
				count6 += 1
			count += 1
			
	#~ plt.ion()
 	count4 = 0
 	count5 = 0
 	count7 = 0
	fig2, axb = plt.subplots(2,3)
	for dic, key in zip(range(len(dic_wd)), symbol_wd):
		cutter3.append(dic)
#		x_ax = dic_wd[dic][key+'POTPCDGone']
		y_ax = dic_wd[dic][key+'PVTPVLone']
		x_ax = dic_wd[dic][key+'POTPCLone']
		axb[count4,count5].plot(x_ax, y_ax, 'o', color = 'green')
		#~ y_ax = dic_wd[dic][key+'CGOCTOTHTL']
#		x_ax = dic_wd[dic][key+'POTPCDGone']
#		z_ax = dic_wd[dic][key+'PVTPVGone']
		#~ z_ax = [i/max(dic_wd[dic][key+'CGOV']) for i in dic_wd[dic][key+'CGOV']]
#		axb[count4,count5].plot(x_ax, z_ax, linestyle = '-', color = 'red')

		count5 += 1
		if count5 == 3:	#	if statement for axis
			count4 += 1
			count5 = 0

		if len(cutter3) % 5 == 0:
			count4 = 0
			count5 = 0
			fig2.delaxes(axb[1,2])
			#~ fig2.suptitle(r"CGOCTOTHTL" + ' for ' + symbol_total[count7])
			fig2.suptitle(r"CGOHmO" + ' for ' + symbol_total[count7])
			fig2.savefig(main_output_path+'CGOCTOTHTL' + symbol_total[count7] +'.png', format = 'png')
			if len(cutter3) < len(dic_wd):
				fig2, axb = plt.subplots(2,3)
			count7 += 1
'''
