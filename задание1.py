# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import math
import xml.etree.ElementTree as et
import numpy as np

def func(x):
        return 100 * math.sqrt(abs(A - 0.01 * x ** 2)) + 0.01 * abs(x + 10)

if __name__ == '__main__':
   A=1
   xmin = -15.0
   xmax = 5
   count = 200
   xlist = np.linspace(xmin, xmax, count)
   ylist = [func(x) for x in xlist]
   plt.plot(xlist, ylist)
   plt.show()

if not os.path.exists('results'):
     os.mkdir('results')


data = et.Element('data')
xdata = et.SubElement(data, 'xdata')
ydata = et.SubElement(data, 'ydata')
for i in range(count):
    et.SubElement(xdata, 'x').text = str(xlist[i])
for i in range(count):
    et.SubElement(ydata, 'y').text = str(ylist[i])
os.chdir(os.path.join(os.getcwd(), 'results'))
xml_file = et.ElementTree(data)
xml_file.write('results.xml')