from turtle import *
# 绘制阴鱼
fillcolor('black')
begin_fill()
circle(60,180)
circle(30,180)
circle(-30,180)
end_fill() # 绘制阴鱼眼
penup()
goto(0, 100)
pendown()
fillcolor('white')
begin_fill()
circle(10)
end_fill() # 绘制阳鱼
penup()
goto(0, 120)
pendown()
fillcolor('white')
begin_fill()
circle(60, 180)
circle(30,180)
circle(-30,180)
end_fill() # 绘制阳鱼眼
penup()
goto(0, 20)
pendown()
fillcolor('black')
begin_fill()
circle(10)
end_fill()
hideturtle()
done()

