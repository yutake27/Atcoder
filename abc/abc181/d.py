# 実装が汚い
s = input()
keta_list = [0] * 10
for keta in s:
    keta_list[int(keta)] += 1

eight_list = []

if len(s) == 1:
    if keta_list[8]:
        print('Yes')
    else:
        print('No')
elif len(s) == 2:
    for i in range(10, 100):
        if i % 8 == 0:
            eight_list.append(i)
    for eb in eight_list:
        e1 = eb // 10
        e2 = eb % 10
        if e1 == e2:
            if keta_list[e1] >= 2:
                print('Yes')
                exit()
        elif keta_list[e1] and keta_list[e2]:
            print('Yes')
            exit()
    print('No')
else:
    for i in range(100, 1000):
        if i % 8 == 0:
            eight_list.append(i)
    flag = False
    for eb in eight_list:
        e1 = eb // 100 % 10
        e2 = eb // 10 % 10
        e3 = eb % 10
        if e1 == e2 == e3:
            if keta_list[e1] >= 3:
                flag = True
                break
        elif e1 == e2:
            if keta_list[e1] >= 2 and keta_list[e3]:
                flag = True
                break
        elif e2 == e3:
            if keta_list[e2] >= 2 and keta_list[e1]:
                flag = True
                break
        elif e3 == e1 and e2:
            if keta_list[e3] >= 2  and keta_list[e2]:
                flag = True
                break
        elif keta_list[e1] and keta_list[e2] and keta_list[e3]:
            flag = True
            break

    if flag:
        print('Yes')
    else:
        print('No')