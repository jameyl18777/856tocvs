#James Ledbetter McKesson 856 
#import necessary modules
#This is just a converter and may be modified for any system or any Drug Wholesaler

import sys
import os
import csv
# create variables for file names and file handlers
# change the path for your files below
f1 = open('c:\Users\Jledbetter\desktop\856an test McKesson.txt', 'r')
f2 = open('C:\Users\Jledbetter\desktop\856an.csv', 'w')
# create variable for csv module writer
a=csv.writer(f2, delimiter=',', quoting=csv.QUOTE_ALL)
try:
	for l in f1:
		l.rstrip()
		x2=l.split('*')
		if x2[0] == 'ISA':
			del x2[-1]
			a.writerow(x2)
		else:
			x4=x2[-1]
			x4=x4[0:-1]
			del x2[-1]
			x2.append(x4)
			a.writerow(x2)
finally:
    f1.close()
    f2.close()
