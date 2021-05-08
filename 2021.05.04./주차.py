#파일 열어서 하는 것인데 내가한 버전은 다른파일에 있음 이건 정답(내 파일에 있는거 보기)
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "urf-8") as report_file:
        report_file.write(" - {0}주차 주간보고".format(i))
        report_file.write("부서: ")
        report_file.write("이름: ")
        report_file.write("업무요약: ")
