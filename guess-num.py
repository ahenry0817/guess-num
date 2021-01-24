#猜數字小遊戲
import random
number = random.randint(1,100)
i = 5
count = 0
while True:
    p = input('請輸入1~100的數字:')
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