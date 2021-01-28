'''
完全数（perfectNumber）
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。
第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
例如：6=1+2+3；28=1+2+3+...+6+7；496=1+2+3+...+30+31；8128=1+2+3…+126+127。
'''

import time
import math

def isPerfectNumber(num) :
	# 计算因子
	if num <= 1 :
		return False;

	sum = 0;
	for i in range(1 , int(math.sqrt(num)) + 1) :
		if num % i == 0 :
			sum += i;
			if i > 1 and num / i != i :
				sum += num / i
	return sum == num;

def main() :
	begin = time.clock();
	start = 1;
	end = 10000;
	count = 0;
	for i in range(start, end):
		if (isPerfectNumber(i)) :
			count += 1;
			print(i, end=' ');
	stop = time.clock();
	print();
	print(start,'~', end, '有',count,'个完美数');
	print("执行时间:", (stop - begin), "秒")

main();