import math

n = int(input())
a_array = list(map(int, input().split()))

def get_primenumber(number):#エラトステネスの篩
    prime_list = []
    search_list = list(range(2,number+1))
    #search_listの先頭の値が√nの値を超えたら終了
    while search_list[0] <= math.sqrt(number):
        #search_listの先頭の値が√nの値を超えたら終了
        #search_listの先頭をprime_listに入れて、先頭をリストに追加して削除
        head_num = search_list.pop(0)
        prime_list.append(head_num)
        #head_numの倍数を除去
        for i in range(number // head_num):
            index = head_num * (i + 1)
            if D[index] == index:
                D[index] = head_num
        search_list = [num for num in search_list if num % head_num != 0]
    #prime_listにsearch_listを結合
    prime_list.extend(search_list)
    return prime_list


def factrization_prime(number):
    div = D[number]
    s = math.sqrt(number)
    div_set = set()
    while number > 1:
        number //= div
        div_set.add(div)
        div = D[number]
    if number > 1:
        div_set.add(div)
    for div in div_set:
        ans_array[div] += 1


thre = max(a_array) + 1
ans_array = [0] * thre
D = list(range(thre + 1))

prime_list = get_primenumber(thre)
for a in a_array:
    factrization_prime(a)

max_ans_array = max(ans_array)
if max_ans_array <= 1:
    print('pairwise coprime')
elif max_ans_array < n:
    print('setwise coprime')
else:
    print('not coprime')