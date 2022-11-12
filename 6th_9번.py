# 반복과 난수를 함께 사용하면 화면에 랜덤한 원을 그릴 수 있다. 화면에 10개의 랜덤한 원을 그리는 프로그램을 작성하라. 원의 중심과 반지름이 모두 난수이어야 한다.
import turtle  # turtle 라이브러리 불러오기
import random  # random 라이브러리 불러오기

t = turtle.Turtle()  # 변수 t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 가져오기

for j in range(1, 10):  # 변수 j를 1에서 9까지 반복
    t.up()  # 펜 올리기
    x = random.randint(-200, 200)  # -200부터 200까지의 숫자가 랜덤으로 지정되며 변수 x에 저장
    y = random.randint(-200, 200)  # -200부터 200까지의 숫자가 랜덤으로 지정되며 변수 y에 저장
    r = random.randint(10, 200)  # 10부터 200까지의 숫자가 랜덤으로 지정되며 변수 r에 저장
    t.goto(x, y)  # (x,y)위치로 이동
    t.down()  # 펜 내리기
    t.circle(r)  # 반지름이 r인 원을 그린다.

t._screen.exitonclick()  # 마우스로 클릭해야 종료됨
