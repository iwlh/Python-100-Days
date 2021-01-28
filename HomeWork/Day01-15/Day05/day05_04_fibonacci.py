'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
'''

import time
import math

x = 0;
y = 1;
for i in range(20):
	tmp = x;
	x = y;
	y = tmp+x;
	print(x, end=' ');
	
print();