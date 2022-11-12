# 터틀 그래픽과 반복을 사용하여 눈 모양을 그려보자.
import turtle  # turtle 라이브러리 가져오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 모양 불러오기
t.color("blue")  # 파란색으로 색을 채움
t.left(90)  # 왼쪽으로 90도 회전

for i in range(1, 7):  # 변수 i를 1에서 6까지 반복
    t.forward(100)  # 100만큼 전진
    t.forward(-30)  # -30만큼 전진
    t.left(60)  # 왼쪽으로 60도 회전
    t.forward(30)  # 30만큼 전진
    t.forward(-30)  # -30만큼 전진

    t.right(120)  # 오른쪽으로 120도 회전
    t.forward(30)  # 30만큼 전진
    t.forward(-30)  # -30만큼 전진

    t.left(60)  # 왼쪽으로 60도 회전
    t.forward(-70)  # -70만큼 전진
    t.left(60)  # 60만큼 전진

t._screen.exitonclick()  # 마우스로 클릭해야 종료
