
import sys
import time
import timeit
import datetime
import num2words
import dateutil.parser as dp
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from matplotlib.dates import strpdate2num




#sys.exit('Program terminated') # This is how you termint the program where ever you want.

stockNumber = int(raw_input('How many stocks would you like to compare?'))
stocks = []
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])


for i in range(0, stockNumber):
	stockIn = raw_input('Please type in the name of the '+ordinal(i)+' stock:') 
	stocks.extend([stockIn])

for i in stocks:
	print(i)

#sys.exit('program terminated')
answer = 'n'
while answer == 'n':
	begYear, begMonth, begDay = raw_input('Please type in the BEGINNING year of your interval (yyyy):'), raw_input('Month (mm):'), raw_input('Day (dd):')
	beginningDay = datetime.date(int(begYear), int(begMonth), int(begDay)).weekday()
	if beginningDay >= 5: # if you put day == 5 or 6 you won't get the right answer and I don't know why!!!
		print('The given date belongs to either Saturday or Sunday and there is no data available for this date. Please type in another date.')
		answer = 'n'
	elif beginningDay < 5:
		answer = str(raw_input('Is '+begYear+'-'+begMonth+'-'+begDay+' the BEGINNING date (Y or N) ?'))

begDateMatch = datetime.date.toordinal(datetime.date(int(begYear), int(begMonth), int(begDay)))

#print(begDateMatch)

answer = 'n'
while answer == 'n':
	endYear, endMonth, endDay = raw_input('Please type in the ENDING year of your interval (yyyy):'), raw_input('Month (mm):'), raw_input('Day (dd):')
	endingDay = datetime.date(int(endYear), int(endMonth), int(endDay)).weekday()
	if endingDay >= 5: # if you put day == 5 or 6 you won't get the right answer and I don't know why!!!
		print('The given date belongs to either Saturday or Sunday and there is no data available for this date. Please type in another date.')
		answer = 'n'
	elif endingDay < 5:
		answer = raw_input('Is '+endYear+'-'+endMonth+'-'+endDay+' the ENDING date (Y or N) ?')

endDateMatch = datetime.date.toordinal(datetime.date(int(endYear), int(endMonth), int(endDay)))

print # empty space.

print('Reading data ...')

head = []
foot = []
dateRange = []

for i in range(0, stockNumber):
	date = np.loadtxt(stocks[i]+'.csv', delimiter = ',', usecols = (0, ),
				converters = {0:strpdate2num('%Y-%m-%d')}, skiprows = 1, ndmin = 2, unpack = True)
	date = date.T
#	print('This is the length and shape of the date array: ', len(date), date.shape)
	for j in range(0, len(date)):
		if date[j,0] == endDateMatch:
#			print(date[j,0], datetime.date.fromordinal(int(date[j,0])))
			head.extend([j+2]) # Since the first line in the file is header we have count for that by adding 1 to the counter.
		elif date[j,0] == begDateMatch:
#			print(date[j,0], datetime.date.fromordinal(int(date[j,0])))
			foot.extend([j+2]) 
	dateRange.extend([len(date)])

arrays = {} # Here we introduce a dictionary and from this point forward 
					# we work with this dictionary.

col = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']
aveCol = ['dateAve', 'openAve', 'highAve', 'lowAve', 'closeAve', 'volumeAve', 'adjcloseAve']

start = timeit.default_timer()

print # empty space.

print('Loading data into arrays ...')

counter = 0
for j in stocks:
	date, open, high, low, close, volume, adjclose = np.genfromtxt(j+'.csv', delimiter = ',',
	skip_header = int(head[counter] - 1), skip_footer = int(dateRange[counter] - foot[counter] + 1), 
	converters = {0:strpdate2num('%Y-%m-%d')}, unpack = True)
	arrays['date_%s' % j] = date
	arrays['open_%s' % j] = open
	arrays['high_%s' % j] = high
	arrays['low_%s' % j] = low
	arrays['close_%s' % j] = close
	arrays['volume_%s' % j] = volume
	arrays['adjclose_%s' % j] = adjclose
	arrays['dateAve_%s' % j] = np.mean(date, axis=None)
	arrays['openAve_%s' % j] = np.mean(open, axis=None)
	arrays['highAve_%s' % j] = np.mean(high, axis=None)
	arrays['lowAve_%s' % j] = np.mean(low, axis=None)
	arrays['closeAve_%s' % j] = np.mean(close, axis=None)
	arrays['volumeAve_%s' % j] = np.mean(volume, axis=None)
	arrays['adjcloseAve_%s' % j] = np.mean(adjclose, axis=None)
	arrays['highToLow_%s' % j] = high/low
	arrays['highToOpen_%s' % j] = high/open
	arrays['lowToOpen_%s' % j] = low/open
	arrays['closeToOpen_%s' % j] = close/open
	arrays['adjcloseToOpen_%s' % j] = adjclose/open
	arrays['highToClose_%s' % j] = high/close
	arrays['lowToClose_%s' % j] = low/close
	arrays['highToAdjclose_%s' % j] = high/adjclose
	arrays['lowToadjclose_%s' % j] = low/adjclose
	arrays['closeMinusOpen_%s' %j] = abs(close - open)
	counter = counter + 1

# Price change part

priceChange1 = raw_input('Please insert your price change (with NO percent sign). If you would like to insert more than one price change seperate each value with "," (e.g. 27,92.5,34): ')
priceChange2 = priceChange1.split(',')

change = []
for price in priceChange2:
	change.extend([float(price)/100.0])

upperPriceThreshold = []
lowerPriceThreshold = []
for j in stocks:
	for priceChange in change:
		bigger = []
		less = []
		for open in range(len(arrays['open_%s' % j])):
			upperPriceThreshold = (priceChange * arrays['open_%s' %j][open]) + arrays['open_%s' % j][open]
			lowerPriceThreshold = (arrays['open_%s' %j][open] - (priceChange * arrays['open_%s' %j][open]))
			if (arrays['high_%s' % j][open]) >= upperPriceThreshold:
				bigger.extend([arrays['high_%s' % j][open]])
			if (arrays['low_%s' % j][open]) <= lowerPriceThreshold: 
				less.extend([arrays['low_%s' % j][open]])
#				print('found')
#				print('###',arrays['low_%s' % j][open], arrays['open_%s' %j][open])
#			print('*********', 'upper: ',upperPriceThreshold, arrays['high_%s' % j][open],
#			'lower: ', lowerPriceThreshold, arrays['low_%s' % j][open])
		highChange = (float(len(bigger))/len(arrays['open_%s' % j])) * 100
		lowChange = (float(len(less))/len(arrays['open_%s' % j])) * 100
		print
		print tabulate([[datetime.date(int(begYear), int(begMonth), int(begDay))
		, datetime.date(int(endYear), int(endMonth), int(endDay)), j, 
		priceChange * 100, highChange, lowChange]], 
		headers=['from', 'to', 'stock', 'target price change (in percent)', 
		'higher than threshold (in percent)', 'lower than threshold (in percent)'], 
		tablefmt='orgtbl')


##########
# Plotting part
##########

print # empty space.

print("""A short note on how to get the right plot(s):
Below is a list of possible prameters from which the user can pick the desired 
prameters for the X and Y axes.""")

print # empty space.

print '*'*10
print 'List of prameters'
print '*'*10
print('''date, open, high, low, close, volume, adjclose, openAve, highAve, 
lowAve, closeAve, volumeAve, adjcloseAve, highToLow, highToOpen, 
lowToOpen, closeToOpen, adjcloseToOpen, highToClose, lowToClose,
highToAdjclose, lowToadjclose, closeMinusOpen''')
print '*'*10
print # empty space.

plotNum = int(raw_input('''How many plots would like to have (notice that 
each plot needs a separate pair of X and Y axis): '''))

axis1 = raw_input('Please type in your X and Y axis (follow this format: X1,Y1,X2,Y2, ... ): ')

axis2 = axis1.split(',') # in the terminal user has to type NO space after ",".

xaxis = []
yaxis = []

for number in range(len(axis2)):
	if number % 2 == 0:
		xaxis.extend([axis2[number]])
	elif number % 2 != 0:
		yaxis.extend([axis2[number]])

print('X_axis: ', xaxis)
print('Y_axis: ', yaxis)
# sys.exit('terminated here')

plots = []
for i in range(plotNum):
	word = num2words.num2words(i)
	plots.extend([word])
print(plots)

#

fig = plt.figure()
color = ['b','g','r','m','c','y','k']
counter = 0
for i in range(plotNum):
	patchLabel = []
	col = 0
	plots[i] = plt.subplot2grid((plotNum,1), (i,0), rowspan = 1, colspan = 1)
	for j in stocks:
		if xaxis[counter] == 'date':
			plots[i].plot_date(arrays[xaxis[counter]+'_'+j], arrays[yaxis[counter]+'_'+j], '-')
		plt.xlabel(xaxis[counter])
		plt.ylabel(yaxis[counter])
		if xaxis[counter] != 'date':
			plots[i].plot(arrays[xaxis[counter]+'_'+j], arrays[yaxis[counter]+'_'+j], 'o')
			plt.xlabel(xaxis[counter])
			plt.ylabel(yaxis[counter])
		patchLabel.extend([matplotlib.patches.Patch(color = color[col], label = j)])
		col += 1
	counter += 1

	plots[i].grid(True)
	plots[i].legend(handles=patchLabel)

plt.show()
# # stop = timeit.default_timer()

# # print stop, start


#https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

#http://www.diveintopython.net/toc/index.html