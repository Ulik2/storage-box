naver = "http://naver.com"
address = naver.split("//")

# 또 다른 방법! 영상의 정답
# my_str = naver.replace("http://", "") -> replace의 활용 지린다.. 확실히 깔끔 -
# my_str = my_str[:my_str.index(".")] -> 슬라이싱과 인덱스의 활용!
# password = my_str[:3] + len(my_str) + str(my_str.count("e")) + "!"

address_1 = address[1]
address_2 = address_1.split(".")
address_3 = address_2[0]

a = address_3[:3]
b = len(address_3)
counts = 0
for i in address_3:
    if i == "e":
        counts = counts + 1
c = counts
d = "!"

password = a + str(b) + str(c) + d
print(password)
