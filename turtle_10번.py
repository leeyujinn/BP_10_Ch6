# 다음과 같이 거북이를 왕복 달리기 시키는 프로그램을 작성해보자.
import turtle  # turtle 라이브러리 불러오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 가져오기

for i in range(5):  # 변수 i를 5번 반복
    t.forward(200)  # 앞으로 200만큼 전진
    t.right(90)  # 오른쪽으로 90도 회전
    t.forward(20)  # 앞으로 20만큼 전진
    t.right(90)  # 왼쪽으로 90도 회전
    t.forward(200)  # 앞으로 200만큼 전진
    t.left(90)  # 왼쪽으로 90도 회전
    t.forward(20)  # 앞으로 20만큼 전진
    t.left(90)  # 왼쪽으로 90도 회전

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
