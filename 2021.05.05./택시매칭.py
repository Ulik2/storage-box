from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51) # rnadrange 이걸 통해서 배웠다 활용하자!
    if time >= 5 and time <=15:
        print("[O] {0}번째 손님 (소요시간: {1})".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1})".format(i, time))
print("\n")
print("총 탑승 승객 수: {0}명".format(cnt))
