n = int(input('Введите число от 3 до 20:'))
result_1 = []
result_2 = []
result = []
result_ = ''
for i in range(1, n):
    if n % i == 0:
        para = i
        for j in range(1, para):
            r = para - j
            if j not in result_1 and j != r:
                result_1.append(j)
                result_1.append(r)
#print(result_1)

for g in range(1, n):
    a = n - g
    if g not in result_2 and g != a:
        result_2.append(g)
        result_2.append(a)
#print(result_2)

result = result_1 + result_2


# for i in range(len(result) + 1):
#     if result[i + 2] > result[i]:
#         s = result[i]
#         d = result[i + 1]
#         result[i] = result[i + 2]
#         result[i + 1] = result[i + 3]
#         result[i + 2] = s
#         result[i + 3] = d


print(*result)

for i in result:
    result_ += f'{i}'
print(result_)
