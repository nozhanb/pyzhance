
import sys
import numpy
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#~ plt.rc('text', usetex=True)
#~ plt.rc('font', family='serif')
tag = ['Mon','Tue','Wed','Thu','Fri']
days = ['SBUX0thMon', 'SBUX0thTue', 'SBUX0thWed', 'SBUX0thThu', 'SBUX0thFri']
fig, ax = plt.subplots(2,3)
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
	var = {days[count]+'CG' : [], days[count]+'CE' : [], days[count]+'CL' : [],
	days[count]+'FG' : [], days[count]+'FE' : [], days[count]+'FL' : [],
	days[count]+'Final': []}
	
	date = dataArray['date']
	openn = dataArray['open']
	high = dataArray['high']
	low = dataArray['low']
	close = dataArray['close']
	volume = dataArray['volume']
	adjclose = dataArray['adjclose']
	
	for j in range(len(date)):
		val = float(close[j]/openn[j])
		if val > 1.0:
			var[days[count]+'CG'].append(val)
		elif val == 1.0:
			var[days[count]+'CE'].append(val)
		else:
			var[days[count]+'CL'].append(val)
	
	var[days[count]+'FG'].append(float(len(var[days[count]+'CG']))/float(len(date)))
	var[days[count]+'FE'].append(float(len(var[days[count]+'CE']))/float(len(date)))
	var[days[count]+'FL'].append(float(len(var[days[count]+'CL']))/float(len(date)))
	var[days[count]+'Final'] = var[days[count]+'FG'] + var[days[count]+'FE'] + var[days[count]+'FL']
		
	labels = [r'$c>o$', '$c=o$', '$c<o$']
	colors = ['yellowgreen', 'gold', 'lightskyblue']
	explode=(0, 0, 0)
		
	ax[count1,count2].pie(var[days[count]+'Final'],explode = explode, labels = labels, 
	colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90,)
	ax[count1,count2].set_aspect('equal')
	ax[count1,count2].set_title(tag[count], fontsize=10)
	count2 += 1
	if count2 == 3:
		count1 += 1
		count2 = 0
	count += 1
fig.delaxes(ax[1,2])
fig.suptitle(r"Ratio of close to open prices based on week days")
plt.show()
