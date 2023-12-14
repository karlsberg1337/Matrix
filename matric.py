###111
'''
arr = []
rows = int(input('ввдите количество строк: '))
for i in range(rows):
    arr.append(list(map(int, input().split())))

colums = len(arr[0])
print()
print(f'Razmer: {rows}*{colums}')
summ = 0
avg = 0
s = 0
for i in range(rows):
    for j in range(colums):
        print(arr[i][j], end=' ')
        summ = summ + arr[i][j]
        s += 1
    print()
print(summ)
avg = summ / s
print(avg)

####11111
arr = []
rows = int(input('введите количество строк: '))
for i in range(rows):
    arr.append(list(map(int, input().split())))

colums = len(arr[0])
print()
print(f'Razmer: {rows}*{colums}')
summ = 0
avg = 0
s = 0
for i in range(rows):
    for j in range(colums):
        print(arr[i][j], end=' ')
        summ = summ + arr[i][j]
        s += 1
    print()
print(summ)
avg = summ / s
print(avg)

####2222

a = [[2, -1], [3, 1]]
b = [[0, 4], [7, -3]]

m = len(a)
n = len(a[0])

c = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]

print(c)


###33333


def summ_matrix(a, b):
    m = len(a)
    n = len(a[0])
    c = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c


a = [[2, -1], [3, 1]]
b = [[0, 4], [7, -3]]
c = summ_matrix(a, b)
print(c)
###4444
'''

a = [[2, -1], [3, 1]]
b = [[0, 4], [7, -3]]


def mult_matrix(a, b):
    a_r = len(a)
    a_c = len(a[0])
    b_r = len(b)
    b_c = len(b[0])
    if (a_c != b_r):
        print('Количество студентов не соотвецтвует')
        return
    c = [[0 for row in range(b_c)] for col in range(a_r)]
    for i in range(a_r):
        for j in range(b_c):
            for k in range(a_c):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c


a = [[2, -1], [3, 1]]
b = [[0, 4], [7, -3]]
print(mult_matrix(a, b))

#####55555

'''
a = [[2, -1], [3, 1]]
k = int(input())


def mult_matrix(a, k):
    m = len(a)
    n = len(a[0])
    c = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] * k
    return c


print(mult_matrix(a, k))
'''