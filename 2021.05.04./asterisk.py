def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)


def asterisk_test_k(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test_k(1, b=2, c=3, d=4, e=5, f=6)


def asterisk_test_t(a, *args):
    print(a, args[0]) #그래서 여기서 args[0]로 해서 첫번째 문항 즉, 안하면 ()하나 더 나오고 , 도 붙음 왜? 그냥 args는 튜플로 묶으니까 튜플 안에 저 튜플을 넣게 되지
    print(type(args))

asterisk_test_t(1, (2, 3, 4, 5, 6)) # 여기서 (2~6)은 하나의 값임, 왜? 하나의 튜플이거든!!


def asterisk_test(a, args):
    print(a, *args)
    print(type(args))

asterisk_test(1, (2,3,4,5,6)) # 위에 정의를 잘 봐 그러면 1은 a고 *(2,3,4,5,6,)이지? 근데 *은 튜플을 벗기는 unpacking의 기능을 해 그래서 1,2,3,4,5,6이 최종적으로 출력된다.
