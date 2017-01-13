



import os
import sys
import numpy
import pyformat
import matplotlib
import matplotlib.pyplot as plt

#	In this part we try to indicate which path is taken as the input path.
def pieplot(inputfile, inputpath = None, ratio = None, sign = 'minus', previous_day = 'off'):
	dic3 = {}
	for files in inputfile:
		if inputpath is None:
			filetoread = os.path.join(os.getcwd(), files)
		elif inputpath is not None:
			filetoread = os.path.join(os.path.expanduser(inputpath), files)
			
#	In this section we read in the files and their contents.
	content = numpy.genfromtxt(fname = filetoread, delimiter = ',',  
			dtype = [('sdate', 'S10'), ('odate', 'i6'), ('open', 'f8'), 
			('high', 'f8'), ('low', 'f8'), ('close', 'f8'), ('adjclose', 'f8'), ('volume', 'i')])

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
		
		for count3 in range(len(dic1['odate_{}'.format(files)])):
			openn = dic1['open_{}'.format(files)][count3]
			high = dic1['high_{}'.format(files)][count3]
			low = dic1['low_{}'.format(files)][count3]
			close = dic1['close_{}'.format(files)][count3]
			if openn == high:
				if openn == close:
					oehec.append(count3)
				elif close > low:
					oehcgw.append(count3)
				elif close == low:
					oehcew.append(count3)
			elif openn == low:
				if openn == close:
					oewec.append(count3)
				elif close < high:
					oewclh.append(count3)
				elif close == high:
					oewceh.append(count3)
			elif openn < high and openn > low:
				if close > openn:
					olhgwlc.append(count3)
				elif close < openn:
					olhgwgc.append(count3)
				elif openn == close:
					olhgwec.append(count3)
		print 
		print 'oehec', ':', len(oehec), 'oehcgw', ':', len(oehcgw), 'oehcew', ':', len(oehcew),\
				'oewec', ':', len(oewec), 'oewclh', ':', len(oewclh), 'oewceh', ':', len(oewceh),\
				'olhgwlc', ':', len(olhgwlc), 'olhgwgc', ':', len(olhgwgc), 'olhgwec', ':', len(olhgwec),\
				'Total number', ':', len(dic1['odate_{}'.format(files)])
		print 
		
	graphtype()		

	if ratio is not None:
		for rr in ratio:
			if previous_day == 'off':
				if len(rr) == 2:
					numerator = rr[0]
					denominator = rr[1]
					value = numpy.divide(dic1[numerator+'_{}'.format(files)], dic1[denominator+'_{}'.format(files)])
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
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] - dic1[numerator2+'_{}'.format(files)][:len(dic1[numerator2+'_{}'.format(files)]) - 1], 
						dic1[denominator1+'_{}'.format(files)][1:] - dic1[denominator2+'_{}'.format(files)][:len(dic1[denominator2+'_{}'.format(files)]) - 1])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] + dic1[numerator2+'_{}'.format(files)][:len(dic1[numerator2+'_{}'.format(files)]) - 1], 
						dic1[denominator1+'_{}'.format(files)][1:] + dic1[denominator2+'_{}'.format(files)][:len(dic1[denominator2+'_{}'.format(files)]) - 1])
	
			dic2 = {files + '_ratio': value}
			dic3.update(dic2)
		dic3.update(dic1)
		
#	Plotting section:
	x = [dic1['odate_{}'.format(files)], numpy.divide(dic1['close_{}'.format(files)], dic1['open_{}'.format(files)]), numpy.divide(dic1['open_{}'.format(files)][1:], dic1['close_{}'.format(files)][:len(dic1['close_{}'.format(files)]) - 1])]
	y = [dic1['volume_{}'.format(files)], dic1['volume_{}'.format(files)][1:]]
	
	fig2, axb = plt.subplots(1)
	par1 = axb.twinx()
	#~ par2 = axb.twinx()

	axb.plot(x[0],y[0], 'g-')
	par1.scatter(x[0],x[1], c = 'r', alpha = 1, s = 18)
	#~ par2.scatter(x[0][1:],x[2], c = 'b', alpha = 1, s = 25)
	par1.set_ylim(0.97, 1.03)
	#~ par2.set_ylim(0.97, 1.03)
	
	
	plt.show()

