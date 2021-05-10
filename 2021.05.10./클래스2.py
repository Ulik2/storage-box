class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self, name, location, speed):
        print("{0}가 {1}방향으로 이동합니다. (속도: {2})".format(self.name, location, speed))

class AtUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, name, damage):
        print("{0}가 공격합니다. [피해: {1}]".format(self.name, self.damage))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location, flying_speed):
        print("{0}: {1}방향으로 날아갑니다. (속도: {2})".format(self.name, location, self.flying_speed))

#상속을 다중으로 받을 수 있음
class FlyableAtUnit(AtUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AtUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

#move를 공중 지상 따로 구분해서 쓰기 귀찮으니까 한꺼번에 move라고 쓸 수 있게 재정의 한 것 => 이게 왜 될까? 코딩은 위에서 아래로 순차적 해석이라는 것을 기억해 (my피셜) = 클래스 분류되니까 어차,
    def move(self, location, flying_speed):
        print("공중유닛이 날아갑니다.")
        self.fly(self.name, location, flying_speed)

battle = FlyableAtUnit("배틀크루저", 300, 250, 5)
#battle.fly(battle.name, "2시", 5)
battle.move(battle.name, "2시") #논항 2개인데 왜 3개라고 뜨지?오류.. => 정답: 재 정의한 move에서 move 논항에 fly_speed를 안썼는데 밑에 self.fly의 논항에는 쓰니까 오류가나지!
                                 # 그렇다면 아예 flying_speed를 없애는 건 안됬을까? 위의 fly를 받아오기 때문에 위의 fly까지 모두 다 없애면 가능하다!
