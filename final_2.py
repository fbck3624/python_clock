from turtle import *
from datetime import *
import pytz
import pygame
import os

x = input("�п�J�ɰϥN�X:")

n = pytz.timezone(pytz.country_timezones(x)[0])
print (n)
a=datetime.now(n)
print (a)
print ("�г]�w�x���T�a�ɶ�:")
a,b=map(int,input().split())
#a = input("�г]�w�x���T�a�ɶ�:")
print (a,b)

 
def Skip(step):
    penup()
    forward(step)
    pendown()
 
def mkHand(name, length):
    #���UTurtle�Ϊ��A�إߪ�wTurtle
    reset()  #�M�ŷ�e�����A�í��m��m���H�����q�{��
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm) 
 
def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")# ���mTurtle���V�_
    #�إߤT�Ӫ�wTurtle�ê�l��
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
    #�إ߿�X��rTurtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()
     
def SetupClock(radius):
    #�إߪ��~��
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
    week = ["�P���@", "�P���G", "�P���T",
            "�P���|", "�P����", "�P����", "�P����"]
    return week[t.weekday()]
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
 
 
def Tick():
    #ø�s��w���ʺA���
    t = datetime.now(n)
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    h=int(hour)
    s=round(second)
    m=int(minute)
    print (h,":",m,":",s)
    if h == a and m == b and (s == 0 or s == 1):
     pygame.init()
     pygame.mixer.music.load("test.mp3")
     pygame.mixer.music.play(loops=0, start=4.0)
     if h >=6 and h<12:
      os.system('pig.py')
     elif h >=12 and h<18:
      os.system('pikachu.py')
     elif h>=18 or h<6:
      os.system('doramon.py')
    secHand.setheading(6*second) #�]�m�¦V�A�C�����6��
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    tracer(False)  #�����ø��L�{�A�������ø��G
    printer.forward(65)
    printer.write(Week(t), align="center",
                 font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                 font=("Courier", 14, "bold"))
    printer.back(50)
    #printer.write("i_chaoren", align="center",
     #             font=("Courier", 14, "bold"))
     #�[�W�r��
    printer.home()
    tracer(True)
 
 

    ontimer(Tick, 1000)#1000ms���~��ե�tick

	
def main():
    tracer(False) #�Ϧh��ø���H�P�����
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()
 
if __name__ == "__main__":       
    main()
