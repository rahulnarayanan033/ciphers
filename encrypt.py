import math
text = 'chillout'
n = len(text)
sqrt = math.sqrt(n)
print(sqrt)
rows = math.floor(sqrt)
cols = math.ceil(sqrt)

lst = []
for i in range(rows):
    lst.append([])
    for j in range(cols):
        lst[i].append(0)

print(lst)
