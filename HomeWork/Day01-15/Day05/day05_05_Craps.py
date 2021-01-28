'''
Craps赌博游戏
规则：玩家掷两个骰子，每个骰子点数为1-6.
如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。

'''

from random import randint

# 玩家信息
money = 1000; # 筹码
debt = 0; # 押注

# 玩家玩的信息
pelt = 0; # 投掷骰子次数
win = 0;  # 赢的次数
lose = 0; # 输的次数

# 盘面信息
point = 0 # 点数

while money > 0 :
	
	debt = int(input( '您的筹码：%d，下注：' % money ));
	if (debt <= 0) : 
		print( '您一共投掷%d次，赢了%d次，输了%d次，胜率%f。剩余筹码%d。' % (pelt, win, lose, (win / (win+lose)), money) );
		quit();

	if (debt > money) : 
		print('筹码不足');
		continue;

	
	pelt +=1; # 投掷次数加一
	point = randint(1, 6) + randint(1, 6);
	print('\t您投掷了%d' % point);
	if (point == 7 or point == 11) :
		money += debt;
		win +=1;
		debt=0;
	elif (point == 2 or point == 3 or point == 12) :
		money -= debt;
		lose +=1;
		debt=0;
	else :
		while True :
			pelt +=1; # 投掷次数加一
			replay = randint(1, 6) + randint(1, 6);
			print('\t您投掷了%d，点数为%d' % (replay, point));
			if (replay == point) :
				money += debt;
				win +=1;
				debt=0;
				break;
			elif (replay == 7):
				money -= debt;
				lose +=1;
				debt=0;
				break;

print( '游戏结束！您一共投掷%d次，赢了%d次，输了%d次，胜率%f。剩余筹码%d。' % (pelt, win, lose, (win / (win+lose)), money) );
quit();


