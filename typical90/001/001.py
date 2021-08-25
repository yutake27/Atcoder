n, l = map(int, input().split())
k = int(input())
a_list = list(map(int, input().split()))
a_list.append(l)

eql = l / (k + 1)  # 均等に切った場合の長さ
selected = [False] * (n + 1)  # 選択した切れ目のリスト
selected[n] = True

ki = 0  # 既に選択した切れ目の数を数える
for i in range(n):
    length = eql * (ki + 1)  # 選択する切れ目の長さ
    if a_list[i] < length < a_list[i + 1]:
        med = a_list[i] + (a_list[i + 1] - a_list[i]) / 2
        if length <= med and selected[i] is False:
            selected[i] = True
        elif selected[i + 1] is False:
            selected[i + 1] = True
        else:
            if selected[i]:
                print('Error')
                exit()
            selected[i] = True
        ki += 1

start = 0
min_length = pow(10, 9)
for i in range(n + 1):
    if selected[i]:
        length = a_list[i] - start
        if length < min_length:
            min_length = length
        start = a_list[i]

# print(selected)
print(min_length)
