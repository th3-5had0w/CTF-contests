#!/usr/bin/python3

import os
import time
import random
from pwn import *

goldfish = """
                      _.'      .
':'.               .''   __ __  .
  '.:._          ./  _ ''     '-'.__
.'''-: '''-._    | .                '-'._
 '.     .    '._.'                       '
    '.   '-.___ .        .'          .  :o'.
      |   .----  .      .           .'     (
       '|  ----. '   ,.._                _-'
        .' .---  |.''  .-:;.. _____.----'
        |   .-''''    |      '
      .'  _'          |    _'
     |_.-'             '-.'
"""

shark = """
                       ,-,
                     ,' /
                   ,'  (          _          _
           __...--'     `-....__,'(      _,-'/
  _,---''''                     ````-._,'  ,'
,'  o                                  `  <
`.____  )))                          ...'  \\
   `--..._        .   .__....----''''   `-. \\
          ```7--i-`.  \                    `-`
             `.(    `-.`.
"""

small = """
<><
"""

dir_path = os.path.dirname(os.path.realpath(__file__))
flag = open(dir_path + "/flag.txt").read().strip()

def print_fl(s: str):
    print(s, flush=True)

def shuffle(arr):
    res = []
    while len(arr) > 0:
        randIndex = random.randint(0, len(arr) - 1)
        res.append(arr[randIndex])
        arr.pop(randIndex)
    return res

def get_fish() -> str:
    arr = [
        {"type": "Cá vàng", "value": goldfish},
        {"type": "Cá mập", "value": shark},
        {"type": "Cá cơm", "value": small},
    ]
    return shuffle(arr)

def main():
    io = remote('178.128.19.56', 25555)
    print(io.recvuntil('id = '))
    print(io.recvline())
    random.seed(int(time.time() * 256))
    user_id = random.randint(1000000, 9999999)
    print(user_id)
    exit()

    print_fl("""
=================================================
== 🐟🐟 Chào mừng đến với trò chơi câu cá 🐟🐟 ==
=================================================
Xin chào, bạn là người chơi với id = %d
Nhà vua của thế giới ảo yêu cầu bạn phải câu 60 con cá và giao nộp trong vòng 2 tháng nữa.
Địa điểm câu cá của bạn tại hồ Kamap. Tại đây có 3 loại cá:
- Cá cơm: câu trúng được +1 điểm
- Cá vàng: câu trúng được +10 điểm
- Cá mập 🐟: câu trúng sẽ bị cá mập ăn hết giỏ cá mà bạn câu được 😅.
Mỗi ngày bạn phải chọn 1 trong 3 loại mồi câu. Tùy vào mồi câu, bạn sẽ thu hút được các loài cá khác nhau.
""".strip() % user_id)

    score = 0
    '''
    for i in range(1, 61):
        print_fl("Ngày %d, hãy chọn mồi câu của bạn [1 - 3]: " % i)
        bait = input()
        if (bait != "1" and bait != "2" and bait != "3"):
            print_fl("Bạn chọn sai mồi câu, hãy nhập 1, hoặc 2, hoặc 3")
            exit()
        bait = int(bait)
        fish = get_fish()[bait - 1]
        print_fl("Bạn đã câu trúng: %s\n%s" % (fish["type"], fish["value"]))
        if fish["type"] == "Cá mập": score = 0
        elif fish["type"] == "Cá cơm": score += 1
        else: score += 10

    if score >= 599:
        print_fl("Bạn được nhà vua ban thưởng:\n\"%s\"" % flag)
    else:
        print_fl("Nhà vua khen bạn làm rất tốt và thưởng bạn %d lượng vàng. Hẹn gặp lại" % score)
    '''

if __name__ == '__main__':
    main()
