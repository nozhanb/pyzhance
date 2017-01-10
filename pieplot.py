



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
				if len(rr) == 4:
					numerator1  = rr[0]		#	present day
					numerator2  = rr[1]		#	previous day
					denominator1 = rr[2]	#	present day 
					denominator2 = rr[3]	#	previous day
					if sign == 'minus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] - dic1[numerator2+'_{}'.format(files)][:len(dic1[numerator2+'_{}'.format(i)]) - 1], 
						dic1[denominator1+'_{}'.format(files)][1:] - dic1[denominator2+'_{}'.format(files)][:len(dic1[denominator2+'_{}'.format(files)]) - 1])
					elif sign == 'plus':
						value = numpy.divide(dic1[numerator1+'_{}'.format(files)][1:] + dic1[numerator2+'_{}'.format(files)][:len(dic1[numerator2+'_{}'.format(files)]) - 1], 
						dic1[denominator1+'_{}'.format(files)][1:] + dic1[denominator2+'_{}'.format(files)][:len(dic1[denominator2+'_{}'.format(files)]) - 1])
	
			dic2 = {files + '_ratio': value}
			dic3.update(dic2)
		dic3.update(dic1)
#	Plotting section:

	fig1, axa = plt.subplots(3, 2)
	
