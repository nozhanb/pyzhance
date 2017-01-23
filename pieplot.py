



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
					olhgwlcday.append(datetime.datetime.strftime(datetime.date.fromordinal(odate), '%a'))
					olcodate.append(dic1['odate_{}'.format(files)][count3])
					olhgwlcclose.append(dic1['close_{}'.format(files)][count3])
					
				elif close < openn:
					olhgwgc.append(count3)
					olhgwgcday.append(datetime.datetime.strftime(datetime.date.fromordinal(odate), '%a'))
					ogcodate.append(dic1['odate_{}'.format(files)][count3])
					olhgwgcclose.append(dic1['close_{}'.format(files)][count3])
					
				elif openn == close:
					olhgwec.append(count3)
		
		dic3.update({'ogcodate_{}'.format(files): numpy.array(ogcodate)})
		dic3.update({'olhgwgcclose_{}'.format(files): numpy.array(olhgwgcclose)})
		
		ogcMon = []
		olcMon = []
		ogcTue = []
		olcTue = []
		ogcWed = []
		olcWed = []
		ogcThu = []
		olcThu = []
		ogcFri = []
		olcFri = []

		for gdays in olhgwgcday:
			if gdays == 'Mon':
				ogcMon.append(gdays)
			elif gdays == 'Tue':
				ogcTue.append(gdays)
			elif gdays == 'Wed':
				ogcWed.append(gdays)
			elif gdays == 'Thu':
				ogcThu.append(gdays)
			else:
				ogcFri.append(gdays)
				
		#~ dic3.update{'{}_friodate'.format(ogcFri)}
					
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
		print 'Mon: ', (float(len(ogcMon))/float(len(olhgwgcday)))*100 , '%', ',','Tue: ', (float(len(ogcTue))/float(len(olhgwgcday)))*100 , '%', ',','Wed: ', (float(len(ogcWed))/float(len(olhgwgcday)))*100 , '%',',',\
				'Thu: ', (float(len(ogcThu))/float(len(olhgwgcday)))*100 , '%',',', 'Fri: ', (float(len(ogcFri))/float(len(olhgwgcday)))*100 , '%'
		print
		print '*'*20
		print 'End:'
		print '*'*20			
	
		for ldays in olhgwlcday:
			if ldays == 'Mon':
				olcMon.append(ldays)
			elif ldays == 'Tue':
				olcTue.append(ldays)
			elif ldays == 'Wed':
				olcWed.append(ldays)
			elif ldays == 'Thu':
				olcThu.append(ldays)
			else:
				olcFri.append(ldays)
					
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
		print 'Mon: ', (float(len(olcMon))/float(len(olhgwlcday)))*100 , '%', ',','Tue: ', (float(len(olcTue))/float(len(olhgwlcday)))*100 , '%', ',','Wed: ', (float(len(olcWed))/float(len(olhgwlcday)))*100 , '%',',',\
				'Thu: ', (float(len(olcThu))/float(len(olhgwlcday)))*100 , '%',',', 'Fri: ', (float(len(olcFri))/float(len(olhgwlcday)))*100 , '%'
		print
		print '*'*20
		print 'End:'
		print '*'*20
	
		ogcdiff = []
		for odate in range(len(ogcodate) -1 ):
			diff = abs(ogcodate[odate] - ogcodate[odate + 1])
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
	
	
#	Plotting section:
	x = [dic1['odate_{}'.format(files)], numpy.divide(dic1['close_{}'.format(files)], dic1['open_{}'.format(files)]), numpy.divide(dic1['close_{}'.format(files)][1:], dic1['close_{}'.format(files)][:len(dic1['close_{}'.format(files)]) - 1])]
	y = [dic1['volume_{}'.format(files)], dic1['volume_{}'.format(files)][1:]]
	fig1, axa = plt.subplots(1)
	fig2, axb = plt.subplots(1)
	#~ par1 = axb.twinx()
	#~ par2 = axb.twinx()

	axa.plot(x[0], dic1['close_{}'.format(files)], 'g-')
	axa.plot(dic3['ogcodate_{}'.format(files)], dic3['olhgwgcclose_{}'.format(files)], 'ro')
	axb.plot(x[0][1:], dic3['ratio_' + files], 'g-')
	axb.plot(x[0][1:], numpy.zeros(len(x[0]) - 1), 'r-')
	#~ for count12 in range(len(x[0]) - 1):
		#~ print x[0][count12], dic3['ratio_' + files][count12]
	
	plt.show()

