#猜數字小遊戲
import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end =int(end)
number = random.randint(start, end)

count = 0
while True:
	p = input('請猜數字:')
	p =int(p)
	count +=1
	if number == p:
		print('你的答案是正確的,恭喜~~')
		print('這是你猜的第', count , '次')
		break
	elif number > p:
		print('你的答案太小了')
	else:
		print('你的答案太大了')
		print('這是你猜的第', count , '次')