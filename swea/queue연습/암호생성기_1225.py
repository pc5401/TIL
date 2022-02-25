import sys
sys.stdin = open('암호생성기.txt', 'r')

while 1:
    try:  # EOFError 대처하기 위해
        tc = int(input())  # 입력처리
        lst = list(map(int, input().split()))

        while lst[-1]:  # rear(top)이 '0'이 될 때까지
            for cnt in range(1, 5+1):  # 5 순회
                rear = lst.pop(0) - cnt

                if rear <= 0:
                    rear = 0
                    lst.append(rear)
                    break  # 0으로 치환 후, 탈출

                lst.append(rear)

        print(f'#{tc}', *lst)
    except EOFError:
        break