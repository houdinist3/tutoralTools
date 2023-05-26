import timeUtils
import time
from datetime import datetime

# timeUtils, time, datetime 모듈을 import 합니다.

def printIt():
    print(time.ctime())

# printIt 함수를 정의합니다. 이 함수는 현재 시간을 출력합니다.

delay = datetime(2023, 5, 26, 20, 56)

# 2023년 5월 26일 20시 56분을 delay 변수에 할당합니다.

while datetime.now() < delay:
    time.sleep(5)

# 현재 시간이 delay보다 작을 때까지 5초씩 대기합니다.

print("now start", time.ctime())

# "now start"와 현재 시간을 출력합니다.

timeUtils.repeatIt(4, printIt, 5)

# timeUtils 모듈의 repeatIt 함수를 호출합니다. 이 함수는 printIt 함수를 4번 반복하며, 각 반복마다 5초씩 대기합니다.
