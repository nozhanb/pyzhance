
import sys
import numpy
import pyformat
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#~ plt.rc('text', usetex=True)
#~ plt.rc('font', family='serif')
tag = ['Mon','Tue','Wed','Thu','Fri']
days = ['DIS0thMon', 'DIS0thTue', 'DIS0thWed', 'DIS0thThu', 'DIS0thFri']
fig1, axa = plt.subplots(2,3)
fig2, axb = plt.subplots(1,1)
count = 0
count1 = 0
count2 = 0

for i in days:
	dataArray = numpy.genfromtxt(fname = i, delimiter = ',',
	dtype = [('date','i4'),('open','f3'),('high','f3'),('low','f3'),
			('close','f3'),('volume','i4'),('adjclose','f3')])
		
	date = []
	openn = []	#	openn because python will confuse open with the function "open".
	high = []
	low = []
	close = []
	volume = []
	adjclose = []
	
	#	We creat a dictionary of different varibles.
	count3 = count
	var = {days[count3]+'CGO' : [], days[count3]+'CEO' : [], days[count3]+'CLO' : [],
	days[count3]+'FG' : [], days[count3]+'FE' : [], days[count3]+'FL' : [],
	days[count3]+'Final': [], days[count3]+'CGOCTO': [], days[count3]+'CGOHTL' : [],
	days[count3]+'CGOO' : [], days[count3]+'CGOC' : [],days[count3]+'CGOH' : [],
	days[count3]+'CGOL' : [], days[count3]+'CGOV' : [], days[count3]+'CLOO' : [], 
	days[count3]+'CLOC' : [], days[count3]+'CLOH' : [], days[count3]+'CLOL' : [], 
	days[count3]+'CLOV' : [], days[count3]+'CGOCTOTHTL': [], days[count3]+'CGOD' : []}
	
	date = dataArray['date']
	openn = dataArray['open']
	high = dataArray['high']
	low = dataArray['low']
	close = dataArray['close']
	volume = dataArray['volume']
	adjclose = dataArray['adjclose']
	
	#	This part is where we calculate the ratio of close to open price
	#	based on week days.
	
	for j in range(len(date)):
		val = float(close[j])/float(openn[j])
		if val > 1.0:
			var[days[count3]+'CGO'].append(val)
			var[days[count3]+'CGOD'].append(date[j])
			var[days[count3]+'CGOO'].append(openn[j])
			var[days[count3]+'CGOC'].append(close[j])
			var[days[count3]+'CGOH'].append(high[j])
			var[days[count3]+'CGOL'].append(low[j])
			var[days[count3]+'CLOV'].append(volume[j]*10**(-7))			
			var[days[count3]+'CGOCTO'].append(float(close[j])/float(openn[j]))
			var[days[count3]+'CGOHTL'].append(float(high[j])/float(low[j]))
			var[days[count3]+'CGOCTOTHTL'].append(float(close[j]-openn[j])/float(high[j]-low[j]))
		elif val == 1.0:
			var[days[count3]+'CEO'].append(val)
		else:
			var[days[count3]+'CLO'].append(val)
			var[days[count3]+'CLOO'].append(openn[j])
			var[days[count3]+'CLOC'].append(close[j])
			var[days[count3]+'CLOH'].append(high[j])
			var[days[count3]+'CLOL'].append(low[j])
	
	var[days[count3]+'FG'].append(float(len(var[days[count3]+'CGO']))/float(len(date)))
	var[days[count3]+'FE'].append(float(len(var[days[count3]+'CEO']))/float(len(date)))
	var[days[count3]+'FL'].append(float(len(var[days[count3]+'CLO']))/float(len(date)))
	var[days[count3]+'Final'] = var[days[count3]+'FG'] + var[days[count3]+'FE'] + var[days[count3]+'FL']
	
	if count == 4:
		#~ print (', '.join(['%.5f']*len(var[days[count3]+'CGOCTOTHTL']))) % tuple(var[days[count3]+'CGOCTOTHTL'])
		print 
		print min(var[days[count3]+'CGOCTOTHTL']), "< CGOCTOTHTL <" , max(var[days[count3]+'CGOCTOTHTL'])
		print "And the average value of CGOCTOTHTL is: ", sum(var[days[count3]+'CGOCTOTHTL'])/len(var[days[count3]+'CGOCTOTHTL'])
		print 
	#	This is where we find the average of a couple of prameters.
		axb.set_yscale('log')
		axb.plot(var[days[count3]+'CGOD'], var[days[count3]+'CGOCTOTHTL'], linestyle = '-',color = 'green')
		axb.plot(var[days[count3]+'CGOD'], var[days[count3]+'CLOV'], linestyle = '-',color = 'red')
		#~ axb.plot([min(var[days[count3]+'CGOD']),max(var[days[count3]+'CGOD'])],
		#~ [sum(var[days[count3]+'CGOCTOTHTL'])/len(var[days[count3]+'CGOCTOTHTL']),sum(var[days[count3]+'CGOCTOTHTL'])/len(var[days[count3]+'CGOCTOTHTL'])],
		 #~ linestyle='-', color='red', linewidth=2)
	
	labels = [r'$c>o$', '$c=o$', '$c<o$']
	colors = ['yellowgreen', 'gold', 'lightskyblue']
	explode=(0, 0, 0)	
	axa[count1,count2].pie(var[days[count3]+'Final'],explode = explode, labels = labels, 
	colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90,)
	axa[count1,count2].set_aspect('equal')
	axa[count1,count2].set_title(tag[count3], fontsize=10)
	count2 += 1
	if count2 == 3:
		count1 += 1
		count2 = 0
	count += 1
fig1.delaxes(axa[1,2])
fig1.suptitle(r"Ratio of close to open prices based on week days")


plt.show()
