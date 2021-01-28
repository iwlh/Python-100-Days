'''

输入一个正整数判断它是不是素数

判断是否素数，有两个方法。
方法1： 假如n是合数，必然存在非1的两个约数p1和p2，其中p1<=sqrt(n)，p2>=sqrt(n)。
方法2： 素数还有一个特点，就是它总是等于 6x-1 或者 6x+1，其中 x 是大于等于1的自然数。

'''

from math import sqrt
#import time


def isPrimeV1(x):
	if x <= 3:
		if x > 1 : return True;
		else: return False;
	else:
		sqrtNum = int(sqrt(x));
		for i in range(2, sqrtNum+1, 1):
			if x % i == 0:
				return False;
		return True;


def isPrimeV2(x):
	if x <= 3:
		if x > 1 : return True;
		else: return False;
	elif (x % 6 != 1) and (x % 6 != 5) : # 等于5，就是6x-1的另外种写法
		return False;
	else:
		sqrtNum = int(sqrt(x));
		for i in range(5, sqrtNum+1, 6):
			if (x % i == 0) or (x % (i+2) == 0):
				return False;
		return True;


def main():
	num = int(input('计算1~X之间的素数。请输入X（一个正整数）:'))

	print('使用isPrimeV1');
	count = 0;
	#start = time.time()*1000
	for i in range(1, num):
		if isPrimeV1(i):
			print(i, end=' ');
			count+=1;
	#end = time.time()*1000
	print();
	print('1 ~', num, '有',count,"个素数")
	#print('use', (end - start))

	count = 0;
	print('使用isPrimeV2');
	#start = time.time()*1000
	for i in range(1, num):
		if isPrimeV2(i):
			print(i, end=' ');
			count+=1;
	#end = time.time()*1000
	print();
	print('1 ~', num, '有',count,"个素数")
	#print('use', (end-start))


main();
