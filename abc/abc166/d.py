X = int(input())

X_range = int(pow(X, 1/4))+1

for i in range(X_range, -X_range-1, -1):
    for j in range(-X_range, X_range+1):
        if pow(i, 5) - pow(j, 5) == X:
            print(i, j)
            exit()
