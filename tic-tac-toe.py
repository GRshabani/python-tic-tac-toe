import turtle

def circle():
    pu()
    turtle.bk(10)
    turtle.rt(90)
    pd()
    turtle.circle(10)
    pu()
    turtle.goto(0,0)
    turtle.lt(90)
    pd()

def ix():
    pd()
    turtle.rt(45)
    turtle.fd(10)
    turtle.bk(20)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(10)
    turtle.bk(20)
    turtle.fd(10)
    turtle.rt(45)
    pu()
    turtle.goto(0, 0)
    pd()


def pu():
    turtle.penup()


def pd():
    turtle.pendown()


def paye():
    pu()
    turtle.fd(30)
    pd()
    turtle.lt(90)
    turtle.fd(90)
    turtle.rt(90)
    pu()
    turtle.fd(30)
    turtle.rt(90)
    pd()
    turtle.fd(90)
    pu()
    turtle.goto(0, 0)
    turtle.lt(180)
    turtle.goto(0, 30)
    turtle.rt(90)
    pd()
    turtle.fd(90)
    pu()
    turtle.goto(0, 60)
    pd()
    turtle.goto(90, 60)
    pu()
    turtle.goto(0,0)
    turtle.lt(90)
    pd()


paye()


def tx():
    pu()
    if x == 1:
        turtle.goto(15, 75)
        ix()
    elif x == 2:
        turtle.goto(45, 75)
        ix()
    elif x == 3:
        turtle.goto(75, 75)
        ix()
    elif x == 4:
        turtle.goto(15, 45)
        ix()
    elif x == 5:
        turtle.goto(45, 45)
        ix()
    elif x == 6:
        turtle.goto(75, 45)
        ix()
    elif x == 7:
        turtle.goto(15, 15)
        ix()
    elif x == 8:
        turtle.goto(45, 15)
        ix()
    elif x == 9:
        turtle.goto(75, 15)
        ix()
    else:
        print('adad bein 1 ta 9')
    pd()


def to():
    pu()
    if o == 1:
        turtle.goto(15, 75)
        circle()
    elif o == 2:
        turtle.goto(45, 75)
        circle()
    elif o == 3:
        turtle.goto(75, 75)
        circle()
    elif o == 4:
        turtle.goto(15, 45)
        circle()
    elif o == 5:
        turtle.goto(45, 45)
        circle()
    elif o == 6:
        turtle.goto(75, 45)
        circle()
    elif o == 7:
        turtle.goto(15, 15)
        circle()
    elif o == 8:
        turtle.goto(45, 15)
        circle()
    elif o == 9:
        turtle.goto(75, 15)
        circle()
    else :
        print ('adad bein 1 ta 9')
    pd()


bx = 0
bo = 0
def barande():
    if (a[1] == 1 and a[2] == 1 and a[3] == 1) or (a[1] == 1 and a[5] == 1 and a[9] == 1) or (a[3] == 1 and a[5] == 1 and a[7] == 1) or (a[1] == 1 and a[4] == 1 and a[7] == 1) or (a[3] == 1 and a[6] == 1 and a[9] == 1) or (a[7] == 1 and a[8] == 1 and a[9] == 1) or (a[4] == 1 and a[5] == 1 and a[6] == 1) or (a[2] == 1 and a[5] == 1 and a[8] == 1) :
        print('player x wins')
        bx=1
    if (a[1] == 2 and a[2] == 2 and a[3] == 2) or (a[1] == 2 and a[5] == 2 and a[9] == 2) or (a[3] == 2 and a[5] == 2 and a[7] == 2) or (a[1] == 2 and a[4] == 2 and a[7] == 2) or (a[3] == 2 and a[6] == 2 and a[9] == 2) or (a[7] == 2 and a[8] == 2 and a[9] == 2) or (a[4] == 2 and a[5] == 2 and a[6] == 2) or (a[2] == 2 and a[5] == 2 and a[8] == 2) :
        print('player o wins')
        bo=1


def baranden():
    if (a[1] == 1 and a[2] == 1 and a[3] == 1) or (a[1] == 1 and a[5] == 1 and a[9] == 1) or (a[3] == 1 and a[5] == 1 and a[7] == 1) or (a[1] == 1 and a[4] == 1 and a[7] == 1) or (a[3] == 1 and a[6] == 1 and a[9] == 1) or (a[7] == 1 and a[8] == 1 and a[9] == 1) or (a[4] == 1 and a[5] == 1 and a[6] == 1) or (a[2] == 1 and a[5] == 1 and a[8] == 1) :
        print('player o wins')
        bo=1
    if (a[1] == 2 and a[2] == 2 and a[3] == 2) or (a[1] == 2 and a[5] == 2 and a[9] == 2) or (a[3] == 2 and a[5] == 2 and a[7] == 2) or (a[1] == 2 and a[4] == 2 and a[7] == 2) or (a[3] == 2 and a[6] == 2 and a[9] == 2) or (a[7] == 2 and a[8] == 2 and a[9] == 2) or (a[4] == 2 and a[5] == 2 and a[6] == 2) or (a[2] == 2 and a[5] == 2 and a[8] == 2) :
        print('player x wins')
        bx=1
    else :
        print('mosavi!')

a = ["0", "0", '0', '0', '0', '0', '0', '0', '0', '0']



for i in range(4):
        if bo==0 or bx==0 :
            x = int(input('x = '))
            while x>=10 or x<=0 :
                x = int(input('x bayad beyn 1 ta 9 bashe. x jadid :'))
            while a[x]==1 or a[x]==2 :
                x= int(input("x tekrarist. x jadid :"))
            a[x]=1
            tx()
            barande()
        if bo==0 or bx==0 :
            o = int(input('o = '))
            while o >= 10 or o <= 0:
                o = int(input('o bayad beyn 1 ta 9 bashe. o jadid :'))
            while a[o] == 1 or a[o] == 2:
                o = int(input("o tekrarist. o jadid :"))
            a[o] = 2
            to()
            barande()
if bo != 1 or bx != 1 :
    x = int(input('x = '))
    while x >= 10 or x <= 0:
        x = int(input('x bayad beyn 1 ta 9 bashe. x jadid :'))
    while a[x] == 1 or a[x] == 2 :
        x = int(input("x tekrarist. x jadid :"))
    a[x] = 1
    tx()
    baranden()


