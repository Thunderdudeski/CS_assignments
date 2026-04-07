import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 10, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['firebrick', 'purple', 'pink', 'turquoise' ]
explodelist = [0.0, 0.0, 0.1, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 180)
plot.axis('equal')
plot.savefig('piechart.png')

