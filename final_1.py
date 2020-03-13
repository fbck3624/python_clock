from turtle import *
from datetime import *
import pytz
import pygame
import os

x = input("請輸入時區代碼:")

n = pytz.timezone(pytz.country_timezones(x)[0])
print (n)
a=datetime.now(n)
print (a)



 
def Skip(step):
    penup()
    forward(step)
    pendown()
 
def mkHand(name, length):
    #註冊Turtle形状，建立表針Turtle
    reset()  #清除當前窗口，並重置位置等信息為默認值
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm) 
 
def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")# 重置Turtle指向北
    #建立三個表针Turtle並初始化
    mkHand("secHand", 135)
    mkHand("minHand",  110)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    #建立輸出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()
     
def SetupClock(radius):
    #建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)
         
def Week(t):    
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
 
 
def Tick():
    #繪製錶針的動態顯示
    t = datetime.now(n)
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    s=round(second)
    m=int(minute)
    h=int(hour)
    print (h,":",m,":",s)
    if m == 45 and (s == 0 or s==1):
     pygame.init()
     pygame.mixer.music.load("test.mp3")
     pygame.mixer.music.play(loops=0, start=4.0)
     if h >=6 and h<12:
      os.system('pig.py')
     elif h >=12 and h<18:
      os.system('pikachu.py')
     elif h>=18 or h<6:
      os.system('doramon.py')
	
     
	
    secHand.setheading(6*second) #設置朝向，每秒轉動6度
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    tracer(False)  #不顯示繪製的過程，直接顯示繪製结果
    printer.forward(65)
    printer.write(Week(t), align="center",
                 font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                 font=("Courier", 14, "bold"))
    printer.back(50)
    #printer.write("i_chaoren", align="center",
     #             font=("Courier", 14, "bold"))
     #加上字體
    printer.home()
    tracer(True)
 
 

    ontimer(Tick, 1000)#1000ms後繼續調用tick
	
def time(h,m):
 m=int(minute)
 h=int(hour)
 print (h,m)

 
def main():
    tracer(False) #使多個繪製對象同時顯示
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()
 
if __name__ == "__main__":       
    main()
