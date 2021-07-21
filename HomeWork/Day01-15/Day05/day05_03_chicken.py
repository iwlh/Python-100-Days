'''
百鸡百钱
我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

设母鸡x只，公鸡y只，小鸡（100-x-y）只，
所以3x+5y+(100-x-y)/3=100
'''

import time
import math

for x in range(0, 100//5+1) :
	for y in range(0, (100-x*5)//3+1) :
		z = 100-x-y;
		if (z % 3 != 0) :
			continue;
		if 5*x+3*y + z/3 == 100 :
			print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, (100-x-y)))