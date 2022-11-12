# 터틀 그래픽과 반복을 사용하여 싸인(sine) 그래프를 그려보자. 거북이를 싸인값에 따라서 움직이면 된다.
import turtle  # turtle 라이브러리 불러오기
import math  # math 라이브러리 불러오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 가져오기
t.color('red', 'yellow')  # 선: 빨간색, 채우기: 노란색으로 지정

for x in range(0, 360):  # 변수 x를 0부터 359까지 반복
    t.goto(x, 200*math.sin(x*3.14/180))  # (x,200*math.sin(x*3.14/180))점으로 이동

t._screen.exitonclick()  # 마우스로 클릭해야 화면이 종료됨
