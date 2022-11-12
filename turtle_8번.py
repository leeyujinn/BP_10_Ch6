# 우리는 이번 장에서 터틀 그래픽으로 별을 그려보았다. 이 코드를 응용하여서 다음과 같이 10개의 별을 그리는 프로그램을 작성하라. 별들은 시작 각도가 약간씩 다르다.
import turtle  # 터틀 라이브러리 불러오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle() 선언
t.speed(0)  # 속도 0으로 지정
t.color("#FF0000")  # 선을 빨간색으로 지정

for j in range(1, 10):  # 변수 j를 1에서 9까지 반복
    for i in range(1, 6):  # 변수 i를 1에서 5까지 반복
        t.left(144)  # 왼쪽으로 144도 회전
        t.forward(200)  # 200만큼 전진
    t.left(10)  # 왼쪽으로 10도 회전

t._screen.exitonclick()  # 마우스로 클릭하면 종료됨
