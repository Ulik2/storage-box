class SoldOutError:
    pass

chicken = 10
wating = 1
while(True):
    try:
        print("남은 치킨: {0}".format(chicken))
        order = int(input("몇 마리를 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 없습니다.")
        elif order <= chicken:
        # 이 에러를 불러와라! 라는 의미
            raise ValueError
        else:
            print("대기번호[{0}]: 치킨 {1}마리 주문이 완료되었습니다.".format(wating, order))
            wating += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

# 이 기능 다양하게 사용될 수 있을듯? 고객 서비스쪽이 좋을듯 한데.. 데이터사이언스에서는 어떻게 사용될 수 있을지 알아보기!
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 주문이 불가능 합니다.")
        break
