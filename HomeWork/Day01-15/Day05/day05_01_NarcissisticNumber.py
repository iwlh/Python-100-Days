'''
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
'''


def isNarcissisticNumber(num):
	if num < 100 or num > 999 :
		return False;
	bai = num // 100;
	shi = (num % 100) // 10;
	ge = num % 10;
	return num == bai**3 + shi**3 + ge**3;

def main():
	start = 100;
	end = 1000;
	count = 0;
	for num in range(start, end) :
		if isNarcissisticNumber(num) :
			count+=1;
			print(num, end=' '); '''此处end为print函数的参数，非变量 '''
	print();
	print(start, '~', end, '有',count,'个水仙花数')

main();
