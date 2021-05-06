from random import *

num = range(1, 51)
num = list(num)
lotto = sample(num, 6)

# 그냥 7개 뽑아서 마지막꺼를 추가번호로 하는게 더 깔끔할듯?.. 괜히 이렇게 했네
for i in num:
    if i in lotto:
        i not in num
additional = sample(num, 1)
print(lotto, additional)
