#self는 멤버변수로 class 내부에서 사용할 수 있는 변수이며 외부에서 새로운 메소드 선언에도 도움을 준다.
#그리고 꼭 __init__에서 밑줄은 붙여야한다!!
class AtUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}가 생성되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}".format(self.hp, self.damage))

#여기서 location은 왜 셀프를 쓰지않지? => self는 멤버변수로 곧 자신을 뜻하는 변수라고 생각하면 된다. 즉 나의 위치가 아니니까 !
    def attack(self, location):
        print("{0}가 {1}방향으로 {2}의 피해를 입혔습니다.".format(self.name, location, self.damage))

#무지성으로 self.harm썼네.. 생각하고 self쓰자! 처음이니까 봐준다 나야..
    def damaged(self, harm):
        print("{0} : {1}의 피해를 입었습니다.".format(self.name, harm))
        self.hp -= harm
        print("남은 체력: {0}".format(self.hp))
        if self.hp <= 0:
            print("{0}이 파괴되었습니다.".format(self.name))

wraith1 = AtUnit("레이스", 75, 10)
wraith1.clocking = True

#클로킹이라는 메소드를 선언하지 않아도 파이썬에서는 self를 통해서 외부에서 바로 만들 수 있다.
if wraith1.clocking == True:
    print("{0} : 클로킹 상태입니다.".format(wraith1.name))

wraith1.attack("3시")
wraith1.damaged(60)
wraith1.damaged(60)
