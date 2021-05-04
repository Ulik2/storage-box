x = ["A", "B", "C"]
y = ["D", "E", "F"]
result = [i+j for i in x for j in y]
print(result)

#2차원 리스트로 하면 결과가 다르다
stuff = [[i+j for i in x]for j in y]
print(stuff)
