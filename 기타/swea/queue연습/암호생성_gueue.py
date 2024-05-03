from collections import deque
import sys
sys.stdin = open('암호생성기.txt', 'r')

while 1:
    try:  # EOFError 대처하기 위해
        tc = int(input())  # 입력처리
        dque = deque(map(int, input().split()))

        while dque[-1]:
            for cnt in range(1, 5+1):
                front = dque.popleft()
                rear = front - cnt
                if rear <= 0:
                    rear = 0
                    dque.append(rear)
                    break
                dque.append(rear)

        print(f'#{tc}', *dque)

    except EOFError:
        break