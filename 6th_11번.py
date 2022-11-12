# 다음의 터틀 그래픽 프로그램을 분석해보자. 학습하지 않은 함수가 있다면 인터넷에서 조사하여 보자.
import turtle  # turtle 라이브러리 불러오기
t = turtle.Turtle()  # 변수t에 turtle.Turtle()를 선언
t.shape("turtle")  # turtle 도형 가져오기
t.color('red', 'yellow')  # 선:빨간색, 채우기:노란색으로 지정
t.begin_fill()  # 도형 색칠할 준비
while True:  # 무한 반복
    t.forward(200)  # 앞으로 200만큼 전진
    t.left(170)  # 왼쪽으로 170도 회전
    if abs(t.pos()) < 1:  # 거북이의 절대위치 좌표, 1보다 작으면 break를 이용해 종료
        break
t.end_fill()  # 그린 도형에 색칠하기

t._screen.exitonclick()  # 클릭해야 화면이 종료됨
