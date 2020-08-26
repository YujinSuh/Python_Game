##For Extra Credit
#-Restart mid-game 
#Variable game difficulty - press '1' to make the game faster 
#Multiple (Three) enemies 
#Enemy snakes can lose partly 
#My own idea - 1. set background - REMEMBER, I ATTACHED EXTRA IMAGE FILE FOR THIS. 
#My own idea - 2. set button to restart


import tkinter as tk
import random


#enemy1:purple
#enemy2:blue
#enemy3:black
#enemy4:white

class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, width=660, height=660)
        self.canvas.pack()
        self.variable()
        self.gameloop()
        
    def variable(self):
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        #image
        self.myimage=[]
        self.myimage.append(tk.PhotoImage(file='bg.jpg'))
        self.myimage_canvas = self.canvas.create_image(330,330, image = self.myimage[0])
        #button
        self.button_restart=tk.Button(self.win, text='Restart',bg='pink', width=15, height=1, command=self.click_restart)
        self.button_restart.place(x=270, y=0)
        #labelframe
##        self.labelframe=tk.LabelFrame(self.win, text="Help Keys")
##        self.label_wg=tk.Label(self.labelframe, text = "<1> : Faster, <2>: Harder, <r>:Restart")
##        self.labelframe.pack(padx=50,pady=50)
##        self.label_wg.pack()
        self.snake =Snake(330,330, 'green', self.canvas)
        self.win.bind('<Down>',self.snake.go_down)
        self.win.bind('<Up>',self.snake.go_up)
        self.win.bind('<Left>',self.snake.go_left)
        self.win.bind('<Right>',self.snake.go_right)
        self.win.bind('<r>',self.restart)
        self.win.bind('1',self.faster)
        numbers=[]
        for i in range(30,601,30):
            numbers.append(i)
        del numbers[8:9]
        self.ovalx=random.choice(numbers)
        self.ovaly=random.choice(numbers)
        self.xpos_e=random.choice(numbers)
        self.ypos_e=random.choice(numbers)
        self.oval = self.canvas.create_oval(self.ovalx,self.ovaly,self.ovalx+30,self.ovaly+30, fill='red')
        self.enemy = Enemy(self.xpos_e,self.ypos_e, 'purple', self.canvas)
        self.enemy2 = Enemy2(random.choice(numbers),random.choice(numbers), 'blue', self.canvas)
        self.enemy3 = Enemy3(random.choice(numbers),random.choice(numbers), 'black', self.canvas)
        self.enemy4 = Enemy4(60,30, 'white', self.canvas)
        self.gameover = False
        
        
    def gameloop(self):
        if 0>=self.enemy2.xpos_e or self.enemy2.xpos_e>=630 or 0>=self.enemy2.ypos_e or 630<=self.enemy2.ypos_e:
            self.canvas.delete(self.enemy2)
            self.canvas.create_text(200,10 ,fill="red",font=('Arial',10),text = 'One Enemy is DEAD!')

        if self.gameover==False:
            check = self.snake.move(self.ovalx, self.ovaly)
            check_e = self.enemy.move(self.ovalx, self.ovaly)
            check_e2 = self.enemy2.move2(self.ovalx, self.ovaly)
            check_e3 = self.enemy3.move(self.ovalx, self.ovaly)
            check_e4 = self.enemy4.move(self.ovalx, self.ovaly)

            if 0>=self.snake.xpos or self.snake.xpos>=630 or 0>=self.snake.ypos or 630<=self.snake.ypos:
                self.gameover=True
            #gameover if snake and enemy overlapped
            for i in range(1,len(self.snake.segments)):
                if self.canvas.coords(self.snake.segments[0]) == self.canvas.coords(self.snake.segments[i]):
                    self.gameover=True
            for i in range(0,len(self.snake.segments)):
                if self.canvas.coords(self.enemy.segments[0]) == self.canvas.coords(self.snake.segments[i]):
                    self.gameover=True
            for i in range(0,len(self.enemy.segments)):
                if self.canvas.coords(self.snake.segments[0]) == self.canvas.coords(self.enemy.segments[i]):
                    self.gameover=True
            for i in range(1,len(self.enemy.segments)):
                if self.canvas.coords(self.enemy.segments[0]) == self.canvas.coords(self.enemy.segments[i]):
                    self.gameover=True

            #gameover for enemy2
            for i in range(0,len(self.snake.segments)):
                if self.canvas.coords(self.enemy2.segments[0]) == self.canvas.coords(self.snake.segments[i]):
                    self.gameover=True
            for i in range(0,len(self.enemy2.segments)):
                if self.canvas.coords(self.snake.segments[0]) == self.canvas.coords(self.enemy2.segments[i]):
                    self.gameover=True
            #gameover for enemy3
            for i in range(0,len(self.snake.segments)):
                if self.canvas.coords(self.enemy3.segments[0]) == self.canvas.coords(self.snake.segments[i]):
                    self.gameover=True
            for i in range(0,len(self.enemy3.segments)):
                if self.canvas.coords(self.snake.segments[0]) == self.canvas.coords(self.enemy3.segments[i]):
                    self.gameover=True
            #gameover for enemy4
            for i in range(0,len(self.snake.segments)):
                if self.canvas.coords(self.enemy4.segments[0]) == self.canvas.coords(self.snake.segments[i]):
                    self.gameover=True
            for i in range(0,len(self.enemy4.segments)):
                if self.canvas.coords(self.snake.segments[0]) == self.canvas.coords(self.enemy4.segments[i]):
                    self.gameover=True 

            

            if check or check_e or check_e2 or check_e3 or check_e4:
                self.canvas.delete(self.oval)
                numbers=[]
                for i in range(30,601,30):
                    numbers.append(i)
                self.ovalx=random.choice(numbers)
                self.ovaly=random.choice(numbers)
                self.oval = self.canvas.create_oval(self.ovalx,self.ovaly,self.ovalx+30,self.ovaly+30, fill='red')
                
        else:
            self.canvas.create_text(460,10,fill="orange",font=('Arial',15),text = "Your score is "+str(len(self.snake.segments)))
        self.loop = self.canvas.after(300, self.gameloop)
        
    def restart(self, event):
        self.canvas.delete(tk.ALL)
        self.variable()

    def faster(self, event):
        self.variable()
        self.loop = self.canvas.after(200, self.gameloop)

    def click_restart(self):
        self.canvas.delete(tk.ALL)
        self.variable()
        

class Snake:
    def __init__(self, xpos, ypos, col, canvas):
        self.xpos=xpos
        self.ypos=ypos
        self.col = col
        self.canvas=canvas
        self.snake= self.canvas.create_rectangle(self.xpos,self.ypos,self.xpos+30,self.ypos+30, fill='green')
        self.segments = []
        self.segments.append(self.snake)
        self.vx = 30
        self.vy = 0
        
    def move(self, ovalx, ovaly):
        obj = self.canvas.create_rectangle(self.xpos,self.ypos,self.xpos+30,self.ypos+30, fill='green' )
        self.segments.insert(0,obj)
        self.xpos += self.vx
        self.ypos += self.vy 
        if self.xpos != ovalx or self.ypos!=ovaly:
            a=self.segments.pop(-1)
            self.canvas.delete(a)
            return False
        return True

    def go_down(self, event):
        self.vy=30
        self.vx=0
    def go_up(self, event):
        self.vy=-30
        self.vx=0
    def go_left(self, event):
        self.vx=-30
        self.vy=0
    def go_right(self, event):
        self.vx=30
        self.vy=0
    

class Enemy:
    def __init__(self, xpos_e, ypos_e, col_e, canvas):
        self.xpos_e=xpos_e
        self.ypos_e=ypos_e
        self.col_e = col_e
        self.canvas=canvas
        self.enemy= self.canvas.create_rectangle(self.xpos_e,self.ypos_e,self.xpos_e+30,self.ypos_e+30, fill='purple')
        self.segments = []
        self.segments.append(self.enemy)

    def move(self, ovalx, ovaly):
        obj = self.canvas.create_rectangle(self.xpos_e,self.ypos_e,self.xpos_e+30,self.ypos_e+30, fill='purple' )
        self.segments.insert(0,obj)
        if self.xpos_e < ovalx:
            self.xpos_e+=30
        elif self.xpos_e > ovalx:
            self.xpos_e-=30
        elif self.ypos_e > ovaly:
            self.ypos_e-=30
        elif self.ypos_e < ovaly:
            self.ypos_e+=30

        if self.xpos_e != ovalx or self.ypos_e!=ovaly:
            a=self.segments.pop(-1)
            self.canvas.delete(a)
            return False
        return True

  
class Enemy2(Enemy): # move randomly
    def __init__(self, xpos_e, ypos_e, col_e, canvas):
        Enemy.__init__(self, xpos_e, ypos_e, col_e, canvas)

    def move2(self, ovalx, ovaly):
        obj = self.canvas.create_rectangle(self.xpos_e,self.ypos_e,self.xpos_e+30,self.ypos_e+30, fill='blue' )
        self.segments.insert(0,obj)
        self.vx=random.choice([-30,0,30])
        if self.vx == 0:
            self.vy=random.choice([-30,30])
        else:
            self.vy = 0
        self.xpos_e += self.vx
        self.ypos_e += self.vy
        if self.xpos_e != ovalx or self.ypos_e!=ovaly:
            a=self.segments.pop(-1)
            self.canvas.delete(a)
            return False
        return True
    
class Enemy3(Enemy): #move as normal
    def __init__(self, xpos_e, ypos_e, col_e, canvas):
        Enemy.__init__(self, xpos_e, ypos_e, col_e, canvas)

    def move(self, ovalx, ovaly):
        obj = self.canvas.create_rectangle(self.xpos_e,self.ypos_e,self.xpos_e+30,self.ypos_e+30, fill='black' )
        self.segments.insert(0,obj)
        if self.xpos_e < ovalx:
            self.xpos_e+=30
        elif self.xpos_e > ovalx:
            self.xpos_e-=30
        elif self.ypos_e > ovaly:
            self.ypos_e-=30
        elif self.ypos_e < ovaly:
            self.ypos_e+=30

        if self.xpos_e != ovalx or self.ypos_e!=ovaly:
            a=self.segments.pop(-1)
            self.canvas.delete(a)
            return False
        return True

class Enemy4(Enemy): #move some fixed path
    def __init__(self, xpos_e, ypos_e, col_e, canvas):
        Enemy.__init__(self, xpos_e, ypos_e, col_e, canvas)
    def move(self, ovalx, ovaly):
        obj = self.canvas.create_rectangle(self.xpos_e,self.ypos_e,self.xpos_e+30,self.ypos_e+30, fill='white' )
        self.segments.insert(0,obj)
        
        if self.xpos_e==30:
            self.ypos_e+=30
        if self.ypos_e==600:
            self.xpos_e +=30
        if self.xpos_e == 600:
            self.ypos_e-=30
        if self.ypos_e ==30:
            self.xpos_e-=30
        if self.xpos_e != ovalx or self.ypos_e!=ovaly:
            a=self.segments.pop(-1)
            self.canvas.delete(a)
            return False
        return True
        
     
SnakeGUI()
tk.mainloop()

#how to make enemies not to go out?
