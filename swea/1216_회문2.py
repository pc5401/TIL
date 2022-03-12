import sys
sys.stdin = open('input_회문2.txt', 'r')

for _ in range(10):
    tc = int(input())
    lst_origin = [input() for i in range(100)]

    maxi = 0
    for row in lst_origin:  # 첫 줄, 두번째 줄.....
        for spt in range(len(lst_origin)):  # 0,1,3,4.....99
            for lng in range(100, 1, -1):  # 0, 1, 2, 3 .... 100-spt
                text = row[spt:lng]

                if len(text) == 1:
                    break

                elif len(text) > maxi:
                    if text == text[::-1]:
                        maxi = len(text)
                else:
                    break

    # print(f'1-{tc} {maxi}')

    lst_revers = list(zip(*lst_origin))
    for row in lst_revers:  # 첫 줄, 두번째 줄.....
        for spt in range(len(lst_revers)):  # 0,1,3,4.....99
            for lng in range(100, 1, -1):  # 0, 1, 2, 3 .... 100-spt
                text = row[spt:lng]

                if len(text) == 1:
                    break

                elif len(text) > maxi:
                    if text == text[::-1]:
                        maxi = len(text)
                else:
                    break



    # for row in lst_revers:
    #     for i in range(100):
    #         for j in range(100, 1, -1):
    #             text = row[i:j-i]
    #             if len(text) > maxi:
    #                 if text == text[::-1]:
    #                     maxi = len(text)
    #                     break


    # print(f'2-{tc} {maxi}')
    # print(maxi)

    print(f'#{tc} {maxi}')