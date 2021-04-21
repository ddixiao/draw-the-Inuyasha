import turtle



def draw_shape():
    #speed
    turtle.speed(0)
    turtle.bgcolor('snow')
    turtle.setup(580,470)

    turtle.penup()
    turtle.goto(-300,-75)
    
    
   
    turtle.left(65)
    turtle.circle(-1000,15)
    turtle.pendown()
    turtle.right(105)
    #turtle.fillcolor('ghost white')
    #turtle.begin_fill()
    turtle.circle(-100,10)
    
    turtle.right(180)
    turtle.circle(-300,10)
    
    turtle.right(90)
    turtle.circle(-150,20)
    turtle.left(10)
    turtle.circle(30,10)

    turtle.left(45)
    turtle.circle(-50,43)
    
    turtle.circle(-40,50)
    # hair top 1
    turtle.left(170)
    turtle.circle(40,40)
    turtle.right(30)
    turtle.circle(40,40)

    turtle.right(150)
    turtle.circle(-60,80)
    #hair top 2
    turtle.left(110)
    turtle.circle(-60,60)
    turtle.right(150)
    turtle.circle(80,40)

    turtle.left(140)
    turtle.circle(-80,50)
    turtle.right(9)
    turtle.circle(-130,40)

    turtle.right(150)
    turtle.circle(180,14)
    turtle.left(165)
    turtle.circle(-180,14)
    turtle.right(10)
    turtle.circle(-140,30)
    turtle.right(10)
    turtle.circle(-55,30)
    
    turtle.right(150)
    turtle.circle(60,30)
    turtle.left(150)
    turtle.circle(-50,45)
    turtle.right(10)
    turtle.circle(-30,30)
    
    turtle.right(70)
    turtle.fd(8)
    
    turtle.right(180)
    turtle.fd(25)
    turtle.circle(100,30)
    
    turtle.right(30)
    turtle.circle(-180,30)
    turtle.right(10)
    turtle.circle(-65,45)
   
    turtle.right(125)
    turtle.circle(200,10)
    turtle.left(10)
    turtle.circle(250,10)
    turtle.left(20)
    turtle.circle(-120,25)
    
    
    # draw right half of jaw
    turtle.left(120)
   
    for _ in range(1,6):
        turtle.fd(15)
        turtle.right(5)
    #draw left half of jaw
    turtle.right(28)
    for _ in range(1,7):
        turtle.fd(15)
        turtle.right(5)
    turtle.fd(11)
    turtle.right(5)
    turtle.right(10)
    turtle.penup()
    for _ in range(1,7):
        turtle.fd(15)
        turtle.right(5)
      #back  
    for _ in range(1,7):
        turtle.left(5)
        turtle.bk(15)
    turtle.left(10)
    turtle.pendown()   
    #back to the central of jaw(the invet of left jaw)
    turtle.left(5)
    turtle.bk(11)
    turtle.left(5)
    for _ in range(1,7):
        turtle.bk(15)
        turtle.left(5)
    turtle.left(23)
    #back to top of right jaw
    
    turtle.left(5)
    for _ in range(1,8):
        turtle.bk(15)
        turtle.left(5)
    # draw right of face
    
    turtle.right(160)
    for _ in range(1,4):
        turtle.fd(20)
        turtle.left(3)
    turtle.fd(2)
    
#draw hair1
    turtle.right(50)
    for _ in range(1,12):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,12):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,5):
        turtle.fd(5)
        turtle.right(12)

    turtle.right(105)

    for _ in range(1,7):
        turtle.fd(6)
        turtle.left(8)
    
#draw hair2
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,16):
        turtle.fd(3)
        turtle.right(3)

    turtle.right(130)

    for _ in range(1,11):
        turtle.fd(5)
        turtle.left(8)

#draw hair3
    turtle.right(50)
    for _ in range(1,16):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,16):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,26):
        turtle.fd(3)
        turtle.right(2)

    turtle.right(110)

    for _ in range(1,6):
        turtle.fd(8)
        turtle.left(5)
    
#draw hair4
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(15)
    
    turtle.right(15)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(15)
    
    turtle.right(145)

    for _ in range(1,18):
        turtle.fd(3)
        turtle.right(2.5)

    turtle.right(120)

    for _ in range(1,11):
        turtle.fd(4)
        turtle.left(5)

#draw hair5
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(15)
    
    turtle.right(15)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(15)
    
    turtle.right(160)

    for _ in range(1,18):
        turtle.fd(3)
        turtle.right(2.5)

    turtle.right(140)

    for _ in range(1,13):
        turtle.fd(4)
        turtle.left(3)

#draw hair6
    turtle.left(135)
    for _ in range(1,11):
        turtle.fd(7)
        turtle.right(4)
    turtle.right(135)
    turtle.circle(-90,10)
    turtle.left(135)
    for _ in range(1,16):
        turtle.fd(3)
        turtle.left(5.8)

    turtle.right(160)
    for _ in range(1,8):
        turtle.fd(10)
        turtle.right(10)
    turtle.left(170)
    for _ in range(1,13):
        turtle.fd(3)
        turtle.left(4)

    turtle.right(160)
    for _ in range(1,12):
        turtle.fd(7)
        turtle.right(7)
    turtle.left(15)
    for _ in range(1,61):
        turtle.fd(1)
        turtle.right(0.3)
   
#draw hair 7
    turtle.penup()
    turtle.goto(-93,75)
    turtle.pendown()

    turtle.right(120)
    for _ in range(1,13):
        turtle.fd(10)
        turtle.right(3)

    turtle.left(15)
    for _ in range(1,13):
        turtle.fd(9)
        turtle.left(3)

    turtle.right(145)
    for _ in range(1,16):
        turtle.fd(10)
        turtle.right(5)

    turtle.right(10)
    for _ in range(1,4):
        turtle.fd(8)
        turtle.right(3)

    turtle.left(10)
    for _ in range(1,5):
        turtle.fd(13)
        turtle.left(4)
    turtle.fd(10)
    #turtle.end_fill()
#draw face_color
def draw_color_face():
    turtle.speed(0)
    turtle.fillcolor('papayawhip')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-85,90)
    turtle.pendown()
    turtle.left(149)
    for _ in range(1,4):
        turtle.fd(7)
        turtle.right(3)
    turtle.left(60)
    for _ in range(1,7):
        turtle.fd(15)
        turtle.right(5)
    turtle.right(135.5)
    turtle.left(10)
    turtle.pendown()   
    #back to the central of jaw(the invet of left jaw)
    turtle.left(5)
    turtle.bk(11)
    turtle.left(5)
    for _ in range(1,7):
        turtle.bk(15)
        turtle.left(5)
    turtle.left(23)
    #back to top of right jaw
    
    turtle.left(5)
    for _ in range(1,8):
        turtle.bk(15)
        turtle.left(5)
    # draw right of face
    
    turtle.right(160)
    for _ in range(1,4):
        turtle.fd(20)
        turtle.left(3)
    turtle.fd(2)

    turtle.right(50)
    for _ in range(1,12):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,12):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,5):
        turtle.fd(5)
        turtle.right(12)

    turtle.right(105)

    for _ in range(1,7):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,16):
        turtle.fd(3)
        turtle.right(3)

    turtle.right(130)

    for _ in range(1,11):
        turtle.fd(5)
        turtle.left(8)

    turtle.right(50)
    for _ in range(1,16):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,16):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,26):
        turtle.fd(3)
        turtle.right(2)

    turtle.right(110)

    for _ in range(1,6):
        turtle.fd(8)
        turtle.left(5)
    

    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(15)
    
    turtle.right(15)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(15)
    
    turtle.right(145)

    for _ in range(1,18):
        turtle.fd(3)
        turtle.right(2.5)

    turtle.right(120)

    for _ in range(1,11):
        turtle.fd(4)
        turtle.left(5)


    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(15)
    
    turtle.right(15)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(15)
    
    turtle.right(160)

    for _ in range(1,18):
        turtle.fd(3)
        turtle.right(2.5)

    turtle.right(140)

    for _ in range(1,13):
        turtle.fd(4)
        turtle.left(3)


    turtle.left(135)
    for _ in range(1,6):
        turtle.fd(7)
        turtle.right(4)
    for _ in range(1,6):
        turtle.right(4)
    turtle.right(135)

   
    turtle.end_fill()
def draw_clother():
#draw clothes
    turtle.speed(0)
    turtle.penup()
    turtle.goto(92,-105)
    turtle.pendown()
    turtle.left(55)
    
    for _ in range(1,5):
        turtle.fd(14)
        turtle.left(4)
    
    turtle.right(30)
    turtle.fd(16)
    turtle.right(2)
    turtle.fd(10)
    
    for _ in range(1,3):
        turtle.left(20)
        turtle.fd(4)
    turtle.right(20)
    turtle.right(20)
    turtle.penup()
    turtle.goto(15,-70)
    turtle.pendown()
    turtle.left(20)
    
    turtle.fillcolor('floralwhite')
    turtle.begin_fill()
    for _ in range(1,7):
        turtle.fd(6)
        turtle.left(2)

    turtle.left(15)
    for _ in range(1,6):
        turtle.fd(5)
        turtle.left(2)

    turtle.left(45)
    for _ in range(1,15):
        turtle.fd(1)
        turtle.left(2)
    turtle.end_fill()
#back
 
    for _ in range(1,15):
        turtle.right(2)
        turtle.bk(1)
    turtle.right(140)
    
#fd
    
    turtle.fd(14)
    
#back
    turtle.bk(14)
    turtle.left(140)
    for _ in range(1,15):
        turtle.fd(1)
        turtle.left(2)
    
#go
    turtle.right(80)
    turtle.fd(12)
    turtle.left(80)
    for _ in range(1,5):
        turtle.fd(4)
        turtle.right(2)
#go
    turtle.right(70)
    for _ in range(1,5):
        turtle.fd(5.8)
        turtle.right(1)
    
#back
    for _ in range(1,5):
        turtle.left(1)
        turtle.bk(5.8)
    turtle.left(70)

    for _ in range(1,5):
        turtle.left(2)
        turtle.bk(4)
    turtle.right(80)
    turtle.bk(12)
    
# draw collar
    turtle.left(180)
    turtle.fillcolor('floralwhite')
    turtle.begin_fill()
    for _ in range(1,7):
        turtle.fd(6)
        turtle.left(2)
    turtle.right(45)
    for _ in range(1,7):
        turtle.fd(6)
        turtle.right(1)
    turtle.fd(3)
    turtle.left(135)
    for _ in range(1,6):
        turtle.fd(4.5)
        turtle.left(1)
    turtle.right(23)
    turtle.end_fill()
    for _ in range(1,6):
        turtle.fd(3)
        turtle.left(1)
    
#back
    for _ in range(1,6):
        turtle.right(1)
        turtle.bk(3)
    turtle.left(23)
    
    for _ in range(1,6):
        turtle.right(1)
        turtle.bk(4.5)
    turtle.right(135)
#go
    turtle.fillcolor('floralwhite')
    turtle.begin_fill()
    for _ in range(1,4):
        turtle.left(2)
        turtle.fd(5)
    turtle.fd(3)
    turtle.left(120)
    
    for _ in range(1,11):
        turtle.fd(4.7)
        turtle.left(6)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(92,-105)
  
##########
#draw shape of clother

    turtle.pendown()
    turtle.right(180)
    
    turtle.fd(12.5)
    
    turtle.penup()
    turtle.goto(120,-122)
    turtle.pendown()
    turtle.right(20)

    for _ in range(1,6):
        turtle.fd(22)
        turtle.right(10)
    
    turtle.penup()
    turtle.goto(93,-73)
    
   
    for _ in range(1,6):
        turtle.right(5)
        turtle.fd(6)
    
    #turtle.penup()
    turtle.goto(-128,-89)
    turtle.pendown()
    turtle.right(15)
    for _ in range(1,11):
        turtle.fd(5)
        turtle.left(3)
    turtle.left(90)
    for _ in range(1,11):
        turtle.fd(5)
        turtle.right(1.5)
    turtle.right(35)
    for _ in range(1,6):
        turtle.fd(17)
        turtle.right(1)
    #back
    for _ in range(1,6):
        turtle.left(1)
        turtle.bk(17)
    turtle.left(35)
    for _ in range(1,11):
        turtle.left(1.5)
        turtle.bk(5)
    turtle.right(90)

    for _ in range(1,6):
        turtle.fd(22)
        turtle.left(5)

    turtle.penup()
    turtle.goto(-86,-80)
    turtle.pendown()
    turtle.left(135)
    
    #draw The Pearl of speech and spirit
    turtle.pensize(1.5)
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    
    turtle.left(130)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(4)
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    
    turtle.left(220)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(7)
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(140)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(5)
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,6):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.bk(5)
    #moon
    turtle.left(20)
    turtle.fillcolor('darkgray')
    turtle.begin_fill()
    for _ in range(1,6):
        turtle.fd(5)
        turtle.left(20)
    turtle.left(115)
    turtle.fd(10)
    turtle.right(15)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.right(15)
    turtle.left(135)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.left(20)
    turtle.end_fill()
    #back
    for _ in range(1,6): 
        turtle.right(20)
        turtle.bk(3)
    turtle.right(135)
    for _ in range(1,6):
        turtle.left(15)
        turtle.bk(3)
    turtle.right(45)
    turtle.fd(6)
    #go1
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(160)
    turtle.fd(5)
    #go2
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(170)
    turtle.fd(10)
    #go3
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(160)
    turtle.fd(10)
    #go4
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(150)
    turtle.fd(10)
    #go5
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(50)
    turtle.fd(5)

    
    #moon
    
    turtle.bk(15)
    turtle.fillcolor('darkgray')
    turtle.begin_fill()
    for _ in range(1,6):
        turtle.fd(5)
        turtle.left(20)
    turtle.left(115)
    turtle.fd(10)
    turtle.right(15)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.right(15)
    turtle.left(135)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.left(20)
    turtle.end_fill()
    #back
    for _ in range(1,6): 
        turtle.right(20)
        turtle.bk(3)
    turtle.right(135)
    for _ in range(1,6):
        turtle.left(15)
        turtle.bk(3)
    turtle.right(45)
    turtle.fd(6)
    #go1
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(150)
    turtle.fd(10)
    #go2
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(50)
    turtle.fd(5)
    
    
    
#################
    #draw face
def draw_face():
    turtle.speed(0)
    #left eyes
    turtle.penup()
    turtle.goto(-80,90)
    turtle.pendown()
    turtle.fillcolor('old lace')
    turtle.begin_fill()
    turtle.pensize(1)
    turtle.right(22)
    turtle.fd(75)
    turtle.penup()
    turtle.bk(15)
    turtle.pendown()
    turtle.right(90)
    turtle.penup()
    turtle.pensize(0.5)
    turtle.fd(25)
    turtle.pendown()
    turtle.pensize(1)
    turtle.right(75)
    turtle.fd(55)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-58,70)
    turtle.pendown()
  
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(7,130)
    turtle.end_fill()
    turtle.fillcolor('orange3')
    turtle.begin_fill()
    turtle.circle(7,230)
    turtle.end_fill()
# right
      
    turtle.penup()
    turtle.goto(45,60)
    turtle.pendown()
    turtle.right(180)
    for _ in range(1,6):
        turtle.fd(10)
        turtle.left(2)

    turtle.fillcolor('old lace')
    turtle.begin_fill()
    for _ in range(1,6):
        turtle.right(3)
        turtle.bk(11)
    turtle.right(75)
    turtle.penup()
    turtle.right(5)
    turtle.fd(22)
    turtle.pendown()
    turtle.left(75)
    turtle.fd(37)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(55,39)
    turtle.pendown()

    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(7,130)
    turtle.end_fill()
    turtle.fillcolor('orange3')
    turtle.begin_fill()
    turtle.circle(7,230)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0,5)
    turtle.right(70)
    turtle.pendown()
    for _ in range(1,5):
        turtle.fd(6)
        turtle.left(2)
    
    turtle.left(150)
    for _ in range(1,6):
        turtle.fd(5.5)
        turtle.left(2)
#draw_meimao
    turtle.penup()
    turtle.goto(-70,110)
    turtle.pendown()
    turtle.right(100)
    turtle.pensize(2)
    turtle.fd(20)
    for _ in range(1,8):
        turtle.right(3)
        turtle.fd(6.3)
    turtle.penup()
    
    turtle.goto(47,73)
    turtle.pendown()
    turtle.left(50)
    turtle.fd(60)

    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()

def clother_color():
    turtle.penup()
    turtle.goto(-86,-80)
    
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.right(5)
    turtle.pensize(3)
    for _ in range(1,5):
        turtle.fd(5.2)
        turtle.right(1)
    turtle.left(82)
    for _ in range(1,7):
        turtle.fd(2)
        turtle.left(1)
    turtle.right(100)
    for _  in range(1,4):
        turtle.fd(3)
        turtle.left(3)
    turtle.right(3)
    for _ in range(1,3):
        turtle.fd(7)
        turtle.left(3)
        
    for _ in range(1,7):
        turtle.fd(6)
        turtle.left(2)
    turtle.right(51)
    for _ in range(1,7):
        turtle.fd(8)
        turtle.right(1)
    turtle.fd(3)
    turtle.left(136)
    for _ in range(1,6):
        turtle.fd(5)
        turtle.left(1)
    turtle.left(10)

    for _ in range(1,6):
        turtle.fd(3)
        turtle.left(1)
    turtle.left(40)

    for _ in range(1,6):
        turtle.fd(2)
        turtle.left(1)

    turtle.left(180)

    for _ in range(1,11):
        turtle.fd(3)
        turtle.right(2)
    turtle.right(20)

    for _ in range(1,6):
        turtle.fd(2)
        turtle.right(2)
    turtle.left(40)
    for _ in range(1,5):
        turtle.fd(20)
        turtle.left(4)
    turtle.left(10)
   
    turtle.right(48)
    for _ in range(1,6):
        turtle.fd(25)
        turtle.right(10)

    turtle.right(75)
    turtle.fd(338)

    #
    turtle.penup()
    turtle.goto(-128,-89)
    turtle.pendown()
    turtle.left(35)
    for _ in range(1,11):
        turtle.fd(5)
        turtle.left(3)
    turtle.left(90)
    for _ in range(1,11):
        turtle.fd(5)
        turtle.right(1.5)
    turtle.right(35)
    for _ in range(1,6):
        turtle.fd(17)
        turtle.right(1)
    #back
    for _ in range(1,6):
        turtle.left(1)
        turtle.bk(17)
    turtle.left(35)
    for _ in range(1,11):
        turtle.left(1.5)
        turtle.bk(5)
    turtle.right(90)

    for _ in range(1,6):
        turtle.fd(23)
        turtle.left(5)
        
    turtle.penup()
    turtle.goto(-128,-89)
    turtle.pendown()
    turtle.penup()
    turtle.right(240)
    for _ in range(1,7):
        turtle.fd(7)
        turtle.right(10)
    turtle.end_fill()
    turtle.pendown()
def draw_ylnz():
    turtle.penup()
    #back
    for _ in range(1,7):
        turtle.left(10)
        turtle.bk(7)
    turtle.left(240)

    #go

    
    turtle.goto(-86,-80)
    turtle.pendown()
    turtle.left(135)
    
    #draw The Pearl of speech and spirit
    turtle.pensize(1.5)
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    
    turtle.left(130)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(4)
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    
    turtle.left(220)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(7)
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(140)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(5)
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,6):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.bk(5)
    #moon
    turtle.left(20)
    turtle.fillcolor('darkgray')
    turtle.begin_fill()
    for _ in range(1,6):
        turtle.fd(5)
        turtle.left(20)
    turtle.left(115)
    turtle.fd(10)
    turtle.right(15)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.right(15)
    turtle.left(135)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.left(20)
    turtle.end_fill()
    #back
    for _ in range(1,6): 
        turtle.right(20)
        turtle.bk(3)
    turtle.right(135)
    for _ in range(1,6):
        turtle.left(15)
        turtle.bk(3)
    turtle.right(45)
    turtle.fd(6)
    #go1
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(160)
    turtle.fd(5)
    #go2
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(170)
    turtle.fd(10)
    #go3
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(160)
    turtle.fd(10)
    #go4
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(150)
    turtle.fd(10)
    #go5
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(50)
    turtle.fd(5)

    
    #moon
    
    turtle.bk(15)
    turtle.fillcolor('darkgray')
    turtle.begin_fill()
    for _ in range(1,6):
        turtle.fd(5)
        turtle.left(20)
    turtle.left(115)
    turtle.fd(10)
    turtle.right(15)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.right(15)
    turtle.left(135)
    for _ in range(1,6):
        turtle.fd(3)
        turtle.left(20)
    turtle.end_fill()
    #back
    for _ in range(1,6): 
        turtle.right(20)
        turtle.bk(3)
    turtle.right(135)
    for _ in range(1,6):
        turtle.left(15)
        turtle.bk(3)
    turtle.right(45)
    turtle.fd(6)
    #go1
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.right(150)
    turtle.fd(10)
    #go2
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,9):
        turtle.fd(5)
        turtle.right(45)
    turtle.end_fill()
    for _ in range(1,5):   #back
        turtle.left(45)
        turtle.bk(5)
    turtle.left(50)
    turtle.fd(5)
    
def draw_haircolor():
    turtle.speed(0)    
    turtle.pensize(0)
    turtle.penup()
    turtle.goto(-300,-75)
    
    
   
    turtle.left(64.5)
    turtle.circle(-1000,15)
    turtle.pendown()
    turtle.right(105)
    turtle.fillcolor('ghost white')
    turtle.begin_fill()
    turtle.circle(-100,10)
    
    turtle.right(180)
    turtle.circle(-300,10)
    
    turtle.right(90)
    turtle.circle(-150,20)
    turtle.left(10)
    turtle.circle(30,10)

    turtle.left(45)
    turtle.circle(-50,43)
    
    turtle.circle(-40,50)
    # hair top 1
    turtle.left(170)
    turtle.circle(40,40)
    turtle.right(30)
    turtle.circle(40,40)

    turtle.right(150)
    turtle.circle(-60,80)
    #hair top 2
    turtle.left(110)
    turtle.circle(-60,60)
    turtle.right(150)
    turtle.circle(80,40)

    turtle.left(140)
    turtle.circle(-80,50)
    turtle.right(9)
    turtle.circle(-130,40)

    turtle.right(150)
    turtle.circle(180,14)
    turtle.left(165)
    turtle.circle(-180,14)
    turtle.right(10)
    turtle.circle(-140,30)
    turtle.right(10)
    turtle.circle(-55,30)
    
    turtle.right(150)
    turtle.circle(60,30)
    turtle.left(150)
    turtle.circle(-50,45)
    turtle.right(10)
    turtle.circle(-30,30)
    
    turtle.right(70)
    turtle.fd(8)
    
    turtle.right(180)
    turtle.fd(25)
    turtle.circle(100,30)
    
    turtle.right(30)
    turtle.circle(-180,30)
    turtle.right(10)
    turtle.circle(-65,45)
   
    turtle.right(125)
    turtle.circle(200,10)
    turtle.left(10)
    turtle.circle(250,10)
    turtle.left(20)
    turtle.circle(-120,25)
    
    
    # draw right half of jaw
    turtle.left(120)
   
    for _ in range(1,6):
        turtle.fd(15)
        turtle.right(5)
    #draw left half of jaw
    turtle.right(28)
    for _ in range(1,7):
        turtle.fd(15)
        turtle.right(5)
    turtle.fd(11)
    turtle.right(5)
    turtle.right(10)
    turtle.penup()
    for _ in range(1,7):
        turtle.fd(15)
        turtle.right(5)
      #back  
    for _ in range(1,7):
        turtle.left(5)
        turtle.bk(15)
    turtle.left(10)
    turtle.pendown()   
    #back to the central of jaw(the invet of left jaw)
    turtle.left(5)
    turtle.bk(11)
    turtle.left(5)
    for _ in range(1,7):
        turtle.bk(15)
        turtle.left(5)
    turtle.left(23)
    #back to top of right jaw
    
    turtle.left(5)
    for _ in range(1,8):
        turtle.bk(15)
        turtle.left(5)
    # draw right of face
    
    turtle.right(160)
    for _ in range(1,4):
        turtle.fd(20)
        turtle.left(3)
    turtle.fd(2)
    
#draw hair1
    turtle.right(50)
    for _ in range(1,12):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,12):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,5):
        turtle.fd(5)
        turtle.right(12)

    turtle.right(105)

    for _ in range(1,7):
        turtle.fd(6)
        turtle.left(8)
    
#draw hair2
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,16):
        turtle.fd(3)
        turtle.right(3)

    turtle.right(130)

    for _ in range(1,11):
        turtle.fd(5)
        turtle.left(8)

#draw hair3
    turtle.right(50)
    for _ in range(1,16):
        turtle.fd(6)
        turtle.left(8)
    
    turtle.right(8)
    for _ in range(1,16):
        turtle.bk(6)
        turtle.right(8)
        
    turtle.left(175)

    for _ in range(1,26):
        turtle.fd(3)
        turtle.right(2)

    turtle.right(110)

    for _ in range(1,6):
        turtle.fd(8)
        turtle.left(5)
    
#draw hair4
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(15)
    
    turtle.right(15)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(15)
    
    turtle.right(145)

    for _ in range(1,18):
        turtle.fd(3)
        turtle.right(2.5)

    turtle.right(120)

    for _ in range(1,11):
        turtle.fd(4)
        turtle.left(5)

#draw hair5
    turtle.right(50)
    for _ in range(1,9):
        turtle.fd(6)
        turtle.left(15)
    
    turtle.right(15)
    for _ in range(1,9):
        turtle.bk(6)
        turtle.right(15)
    
    turtle.right(160)

    for _ in range(1,18):
        turtle.fd(3)
        turtle.right(2.5)

    turtle.right(140)

    for _ in range(1,13):
        turtle.fd(4)
        turtle.left(3)

#draw hair6
    turtle.left(135)
    for _ in range(1,11):
        turtle.fd(7)
        turtle.right(4)
    turtle.right(135)
    turtle.circle(-90,10)
    turtle.left(135)
    for _ in range(1,16):
        turtle.fd(3)
        turtle.left(5.8)

    turtle.right(160)
    for _ in range(1,8):
        turtle.fd(10)
        turtle.right(10)
    turtle.left(170)
    for _ in range(1,13):
        turtle.fd(3)
        turtle.left(4)

    turtle.right(160)
    for _ in range(1,12):
        turtle.fd(7)
        turtle.right(7)
    turtle.left(15)
    for _ in range(1,61):
        turtle.fd(1)
        turtle.right(0.3)
   
#draw hair 7
    turtle.penup()
    turtle.goto(-93,75)
    turtle.pendown()

    turtle.right(120)
    for _ in range(1,13):
        turtle.fd(10)
        turtle.right(3)

    turtle.left(15)
    for _ in range(1,13):
        turtle.fd(9)
        turtle.left(3)

    turtle.right(145)
    for _ in range(1,16):
        turtle.fd(10)
        turtle.right(5)

    turtle.right(10)
    for _ in range(1,4):
        turtle.fd(8)
        turtle.right(3)

    turtle.left(10)
    for _ in range(1,5):
        turtle.fd(13)
        turtle.left(4)
    turtle.fd(10)
    turtle.end_fill()
    
    
if __name__ == '__main__':
    draw_shape()
    draw_color_face()
    draw_clother()
    draw_face()
    clother_color()
    draw_ylnz()
    draw_haircolor()
