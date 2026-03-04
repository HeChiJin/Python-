
import random
"""
题目要求：随机生成一个0~99之间的整数，让用户猜数，
用户猜对结束并显示“猜对了”，猜错时显示“猜大了”或
“猜小了”，最多5次机会
"""

def guess_num():
    computer_num = random.randint(1, 100)
    # computer_num = 5
    i = 0
    while i < 5:
        user_num = int(input('请输入:'))
        if user_num > computer_num:
            print('猜大了')
        elif user_num < computer_num:
            print('猜小了')
        else:
            print('猜对了')
            break
        i += 1
    else:  # 没有从break出来，就会走else
        print('机会用完了')
    print(f'computer_num{computer_num}')


def for_else():
    for i in range(10):
        if i == 15:
            break
    else:
        print('走到最后啦')


# guess_num()
for_else()

