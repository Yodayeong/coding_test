#스탬프 찍기

#주어진 숫자만큼 # 을 출력해보세요.
#주어질 숫자는 100,000 이하다.

import sys
sys.stdin = open('5_스탬프찍기.txt', 'r')

times = int(input())
for i in range(times):
    #반복문 활용
    print('#', end = '')

print('\n')
##or
#그냥 곱하기로
times = int(input())
print('#'*times)