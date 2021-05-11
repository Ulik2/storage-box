class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_details(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    show_details(house)
    #print(house) -> 이건 왜 안되는거지? 위를 보면 House(~~)이렇게 한게 house1이라고 해놨는데 결국 이건 __init__만 해놓은 거임
                   # !!!!!!!!!!!!100% 이해가안된다 이거 이해하고 넘어가기
                   # -> House는 그냥 저 값을 house1.location = ~~ house1.house_type = ~~ 이렇게 저장하는 것일 뿐이야 그냥 변수처럼 쓰는게 아니라구!!
                   # 이게 정답맞지? 그래서 print하고 셀프가 들어간 show_details를 써줘야지!


#이렇게하면 프로그램의 유연함이 거의 없잖아.. 대충하지 말라구 나야
#print("총 3대의 매물이 있습니다.")
#house1.show_details()
#house2.show_details()
#house3.show_details()
