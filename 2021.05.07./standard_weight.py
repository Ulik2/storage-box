# 이렇게 지정하고 함수 정의에서 전역변수 선언해주는거 뭔가 안 깔끔하다. 이렇게 변수 많이 지정해주면 메모리손실도 많이 나지 않을까? 비효율적인거같은데..
#male = 1
#female = 2

#def std_weight(height, gender):
#    global male
#    global female
#    if gender == male:
#        male_std = height * height * 22
#        male_std = round(male_std, 2)
#    elif gender == female:
#        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height*100, male_std))
#        female_std = height * height * 21
#        female_std = round(female_std, 2) #round함수는 소수점 몇 번째까지 표기할지 정하고 반올림해준다.
#        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height*100, female_std))

#q_height = input("Enter your height in meter: ")
#q_gender = input("Enter your gender(male or female): ")       -> 인풋 받아서 하는거 시도해봤는데 뭐가문제지?...
#std_weight(1.75, male)


#이게 더 깔끔하고 input도 살릴 수 있을 듯(영상 참고하긴 했음)

def std_weight(height, gender):
    if gender == "male":
        return height * height * 22
    elif gender == "female":
        return height * height * 21

height = input("Enter your height in meter: ")
height = float(height)
gender = input("Enter your gender(male or female): ")
weight = round(std_weight(height/100, gender), 2)
if gender == "male":
    print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))
if gender == "female":
    print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, weight))
