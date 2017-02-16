



import os
import sys
import numpy
import pyformat
import datetime
import matplotlib
import matplotlib.pyplot as plt

#	In this part we try to indicate which path is taken as the input path.
def pieplot(inputfile, inputpath = None, ratio = None, sign = 'minus', previous_day = 'off'):
	dic3 = {}
	counter1 = 0
	for files in inputfile:
		if inputpath is None:
			filetoread = os.path.join(os.getcwd(), files)
		elif inputpath is not None:
			filetoread = os.path.join(os.path.expanduser(inputpath), files)
			
#	In this section we read in the files and their contents.
	content = numpy.genfromtxt(fname = filetoread, delimiter = ',',  
			dtype = [('sdate', 'S10'), ('odate', 'i6'), ('open', 'f8'), 
			('high', 'f8'), ('low', 'f8'), ('close', 'f8'), ('adjclose', 'f8'), ('volume', 'i8')])

	dic1 = {'sdate_{}'.format(files): content['sdate'], 'odate_{}'.format(files): content['odate'], 
	'open_{}'.format(files): content['open'], 'high_{}'.format(files): content['high'], 
	'low_{}'.format(files): content['low'], 'close_{}'.format(files): content['close'], 
	'adjclose_{}'.format(files): content['adjclose'], 'volume_{}'.format(files): content['volume']}

	def graphtype():
		gtdic = {}	#	gtdic stands for graphtype dictionary
		oehec = []	#	o stands for open, e stands for equal, h for high and c for close. 
		oehcgw = []	#	g stands for greater than
		oehcew = []	#	l stands for less than
		
		olhgwec = []	#	w stands for low
		olhgwgc = []
		olhgwlc = []
		
		oewec = []
		oewclh = []
		oewceh = []
		
		olhgwlcday = []
		olhgwgcday = []
		olcodate = []
		ogcodate = []
		
		olhgwgcclose = []
		olhgwlcclose = []
	
		ogcMonord = []
		olcMonord = []
		ogcTueord = []
		olcTueord = []
		ogcWedord = []
		olcWedord = []
		ogcThuord = []
		olcThuord = []
		ogcFriord = []
		olcFriord = []
	
		ogcFriclose = [] # I need to add another right below this for olc
		
		presopentoprevclose = []
		presopentopresclose = []
		presopentopreslow = []
		
		for count3 in range(len(dic1['odate_{}'.format(files)])):
			odate = dic1['odate_{}'.format(files)][count3]
			openn = '{:07.5f}'.format(dic1['open_{}'.format(files)][count3])
			high = '{:07.5f}'.format(dic1['high_{}'.format(files)][count3])
			low = '{:07.5f}'.format(dic1['low_{}'.format(files)][count3])
			close = '{:07.7f}'.format(dic1['close_{}'.format(files)][count3])
			if openn == high:
				if openn == close:
					oehec.append(count3)
				elif close > low:
					oehcgw.append(count3)
					olhgwgcday.append(datetime.datetime.strftime(datetime.date.fromordinal(odate), '%a'))
					#~ olhgwgcclose.append(dic1['close_{}'.format(files)][count3])
					#~ ogcodate.append(dic1['odate_{}'.format(files)][count3])
				elif close == low:
					oehcew.append(count3)
			elif openn == low:
				if openn == close:
					oewec.append(count3)
				elif close < high:
					oewclh.append(count3)
					olhgwlcday.append(datetime.datetime.strftime(datetime.date.fromordinal(odate), '%a'))
					olhgwlcclose.append(dic1['close_{}'.format(files)][count3])
					olcodate.append(dic1['odate_{}'.format(files)][count3])
				elif close == high:
					oewceh.append(count3)
			elif openn < high and openn > low:
				if close > openn:
					olhgwlc.append(count3)
					wdaycgo = datetime.datetime.strftime(datetime.date.fromordinal(odate), '%a')
					olhgwlcday.append(wdaycgo)
					olcodate.append(dic1['odate_{}'.format(files)][count3])
					olhgwlcclose.append(dic1['close_{}'.format(files)][count3])
					
					if wdaycgo == 'Mon':
						olcMonord.append(odate)
					elif wdaycgo == 'Tue':
						olcTueord.append(odate)
					elif wdaycgo == 'Wed':
						olcWedord.append(odate)
					elif wdaycgo == 'Thu':
						olcThuord.append(odate)
					else:
						olcFriord.append(odate)
					
				elif close < openn:
					olhgwgc.append(count3)
					wdayogc = datetime.datetime.strftime(datetime.date.fromordinal(odate), '%a')
					olhgwgcday.append(wdayogc)
					ogcodate.append(dic1['odate_{}'.format(files)][count3])
					olhgwgcclose.append(dic1['close_{}'.format(files)][count3])
					
					if wdayogc == 'Mon':
						ogcMonord.append(odate)
					elif wdayogc == 'Tue':
						ogcTueord.append(odate)
					elif wdayogc == 'Wed':
						ogcWedord.append(odate)
					elif wdayogc == 'Thu':
						ogcThuord.append(odate)
					else:
						ogcFriord.append(odate)
						ogcFriclose.append(close)
					
				elif openn == close:
					olhgwec.append(count3)
		
		for count12 in range(len(dic1['odate_{}'.format(files)]) - 1):
			prevdayclose = dic1['close_{}'.format(files)][count12]
			presdayopen = dic1['open_{}'.format(files)][count12 + 1]
			presdayclose = dic1['close_{}'.format(files)][count12 + 1]
			presdaylow = dic1['low_{}'.format(files)][count12 + 1]
			
			if (presdayopen - prevdayclose) > 0:
				presdayopentoprevdayclose = float(presdayopen)/float(prevdayclose)
				presdayopentopresdayclose = float(presdayopen)/float(presdayclose)
				presdayopentopresdaylow = float(presdayopen)/float(presdaylow)
				presopentoprevclose.append(presdayopentoprevdayclose)
				presopentopresclose.append(presdayopentopresdayclose)
				presopentopreslow.append(presdayopentopresdaylow)
		
		dic3.update({'ogcodate_{}'.format(files): numpy.array(ogcodate)})
		dic3.update({'olhgwgcclose_{}'.format(files): numpy.array(olhgwgcclose)})
		dic3.update({'ogcFriord_{}'.format(files):numpy.array(ogcFriord)})
		dic3.update({'ogcFriclose_{}'.format(files):numpy.array(ogcFriclose)})
		dic3.update({'presopentoprevclose_{}'.format(files): numpy.array(presopentoprevclose)})
		dic3.update({'presopentopresclose_{}'.format(files): numpy.array(presopentopresclose)})
		dic3.update({'presopentopreslow_{}'.format(files): numpy.array(presopentopreslow)})
							
		print
		print 'oehec', ':', len(oehec),',', 'oehcgw', ':', len(oehcgw),',', 'oehcew', ':', len(oehcew),',',\
				'oewec', ':', len(oewec),',', 'oewclh', ':', len(oewclh),',', 'oewceh', ':', len(oewceh),',',\
				'olhgwlc', ':', len(olhgwlc),',', 'olhgwgc', ':', len(olhgwgc),',', 'olhgwec', ':', len(olhgwec),',',\
				'Total number', ':', len(dic1['odate_{}'.format(files)])
		print
		print '*'*20
		print 'Week day section:'
		print '*'*20
		print 
		print 'The fraction of weekd days in which open price is greater than close price.'
		print 'Mon: ', (float(len(ogcMonord))/float(len(olhgwgcday)))*100 , '%', ',','Tue: ', (float(len(ogcTueord))/float(len(olhgwgcday)))*100 , '%', ',','Wed: ', (float(len(ogcWedord))/float(len(olhgwgcday)))*100 , '%',',',\
				'Thu: ', (float(len(ogcThuord))/float(len(olhgwgcday)))*100 , '%',',', 'Fri: ', (float(len(ogcFriord))/float(len(olhgwgcday)))*100 , '%'
		print
		print '*'*20
		print 'End:'
		print '*'*20			
					
		print 
		print 'oehec', ':', len(oehec),',', 'oehcgw', ':', len(oehcgw),',', 'oehcew', ':', len(oehcew),',',\
				'oewec', ':', len(oewec),',', 'oewclh', ':', len(oewclh),',', 'oewceh', ':', len(oewceh),',',\
				'olhgwlc', ':', len(olhgwlc),',', 'olhgwgc', ':', len(olhgwgc),',', 'olhgwec', ':', len(olhgwec),',',\
				'Total number', ':', len(dic1['odate_{}'.format(files)])
		print
		print '*'*20
		print 'Week day section:'
		print '*'*20
		print 
		print 'The fraction of weekd days in which open price is less than close price.'
		print 'Mon: ', (float(len(olcMonord))/float(len(olhgwlcday)))*100 , '%', ',','Tue: ', (float(len(olcTueord))/float(len(olhgwlcday)))*100 , '%', ',','Wed: ', (float(len(olcWedord))/float(len(olhgwlcday)))*100 , '%',',',\
				'Thu: ', (float(len(olcThuord))/float(len(olhgwlcday)))*100 , '%',',', 'Fri: ', (float(len(olcFriord))/float(len(olhgwlcday)))*100 , '%'
		print
		print '*'*20
		print 'End:'
		print '*'*20
	
		ogcdiff = []
		for odate in range(len(dic3['ogcFriord_{}'.format(files)]) -1 ):
			diff = abs(dic3['ogcFriord_{}'.format(files)][odate] - dic3['ogcFriord_{}'.format(files)][odate + 1])
			ogcdiff.append(diff)
	
		dayav = numpy.average(numpy.array(ogcdiff))
		daystd = numpy.std(numpy.array(ogcdiff))
	
		print
		print '*'*20
		print 'Weekd day difference section:'
		print '*'*20
		
		print 'The average and std of number of days between two consecutive days in which the open price is less than the close price.'
		print 	'Average: ', dayav, ' , ', 'std: ', daystd

		print
		print '*'*20
		print 'END'
		print '*'*20		
		
	graphtype()

	if ratio is not None:
		count2 = 0
		for rr in ratio:
			rat = []
			if previous_day == 'off':
				if len(rr) == 2:
					numerator = rr[0]
					denominator = rr[1]
					value = numpy.divide(dic1[numerator+'_{}'.format(files)], dic1[denominator+'_{}'.format(files)])
					average = numpy.average(value)
					std = numpy.std(value)
					
				elif len(rr) == 3:
					numerator1  = rr[0]
					numerator2  = rr[1]
					denominator = rr[2]
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)] - dic1[numerator2+'_{}'.format(files)], dic1[denominator+'_{}'.format(files)])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)] + dic1[numerator2+'_{}'.format(files)], dic1[denominator+'_{}'.format(files)])
				else:
					numerator1  = rr[0]
					numerator2  = rr[1]
					denominator1 = rr[2]
					denominator2 = rr[3]
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)] - dic1[numerator2+'_{}'.format(files)], dic1[denominator1+'_{}'.format(files)] - dic1[denominator2+'_{}'.format(files)])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)] + dic1[numerator2+'_{}'.format(files)], dic1[denominator1+'_{}'.format(files)] + dic1[denominator2+'_{}'.format(files)])
	
			elif previous_day == 'on':
				if len(rr) == 2:
					numerator = rr[0]
					denominator = rr[1]
					value = numpy.divide(dic1[numerator+'_{}'.format(files)][1:], dic1[denominator+'_{}'.format(files)][:len(dic1[denominator+'_{}'.format(files)]) - 1])

				elif len(rr) == 3:
					numerator1  = rr[0]
					numerator2  = rr[1]
					denominator = rr[2]
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] - dic1[numerator2+'_{}'.format(files)][1:], dic1[denominator+'_{}'.format(files)][:len(dic1[denominator+'_{}'.format(files)]) - 1])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] + dic1[numerator2+'_{}'.format(files)][1:], dic1[denominator+'_{}'.format(files)][:len(dic1[denominator+'_{}'.format(files)]) - 1])
				else:
					numerator1  = rr[0]		#	present day
					numerator2  = rr[1]		#	previous day
					denominator1 = rr[2]	#	present day 
					denominator2 = rr[3]	#	previous day
					#### ONT FORGET TO FIX THIS PART. You have made some changes like adding the for loop.
					if sign == 'minus':
						for count11 in range(len(dic1['odate_{}'.format(files)]) - 1):
							a = (float(dic1[numerator1+'_{}'.format(files)][count11]) - float(dic1[numerator2+'_{}'.format(files)][count11 + 1]))
							
							b = (float(dic1[denominator1+'_{}'.format(files)][count11]) - float(dic1[denominator2+'_{}'.format(files)][count11]))
							
							if b == 0:
								b = float(1)
	
							value = float(a) / float(b)
							
							rat.append(value)
								
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] + dic1[numerator2+'_{}'.format(files)][:len(dic1[numerator2+'_{}'.format(files)]) - 1], 
						dic1[denominator1+'_{}'.format(files)][1:] + dic1[denominator2+'_{}'.format(files)][:len(dic1[denominator2+'_{}'.format(files)]) - 1])

			print 
			#~ print 'The average of '+str(ratio[count2][0])+'/'+str(ratio[count2][1])+ ' in present day mode is: ', '{:07.5f}'.format(numpy.average(value))
			#~ print 'The std of '+str(ratio[count2][0])+'/'+str(ratio[count2][1])+ ' in present day mode is: ', '{:07.5f}'.format(numpy.std(value))
	#~ 
			dic3.update({'ratio_' + files: numpy.array(rat)})
			count2 += 1
		dic3.update(dic1)
	counter1 += 1
	
	print 'average = ', numpy.average(dic3['ratio_{}'.format(files)]), 'std = ', numpy.std(dic3['ratio_{}'.format(files)]), '<-------'
	
#	Plotting section:
	x = [dic1['odate_{}'.format(files)], numpy.divide(dic1['close_{}'.format(files)], dic1['open_{}'.format(files)]), numpy.divide(dic1['close_{}'.format(files)][1:], dic1['close_{}'.format(files)][:len(dic1['close_{}'.format(files)]) - 1])]
	y = [dic1['volume_{}'.format(files)], dic1['volume_{}'.format(files)][1:]]
	fig1, axa = plt.subplots(1)
	fig2, axb = plt.subplots(1)
	fig3, axc = plt.subplots(1)
	#~ par1 = axb.twinx()
	#~ par2 = axb.twinx()

	axa.plot(x[0], dic1['close_{}'.format(files)], 'g-')
	#~ axa.plot(dic3['ogcodate_{}'.format(files)], dic3['olhgwgcclose_{}'.format(files)], 'ro')
	axa.plot(dic3['ogcFriord_{}'.format(files)], dic3['ogcFriclose_{}'.format(files)], 'bo')
	
	axb.plot(x[0][1:], dic3['ratio_' + files], 'g-')
	axb.plot(x[0][1:], numpy.zeros(len(x[0]) - 1), 'r-')

	axc.plot(dic3['presopentoprevclose_{}'.format(files)], dic3['presopentopresclose_{}'.format(files)], 'go')
	axc.plot(dic3['presopentoprevclose_{}'.format(files)], dic3['presopentopreslow_{}'.format(files)], 'ro')
	
	plt.show()

