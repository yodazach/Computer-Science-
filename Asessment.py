import random as r
import re
from tkinter import *

f = open("addsubtract.txt","r+")
f.truncate(0)
question_number = 0
counter = 0
symbols = ["+","-","/","*"]

print(4*7)

#Question general generation, all level test 
for i in range(100):
     #plays around of chances of brackets
     brackets = r.randint(0,1) * r.randint(0,1) * r.randint(0,1)
     brackets2 = r.randint(0,1) * r.randint(0,1) * r.randint(0,1)
     #creates chance of brackets that include everything 
     if brackets == brackets2:
          brackets3 = r.randint(0,1)
     else:
          brackets3 = 1
     #actual generation
     #shitty bracket generation: f.write("("*brackets + "{}".format(r.randint(1, 10))+")"*brackets*brackets3 +"{}".format(r.choice(symbols))+"("*brackets2*brackets3+"{}".format(r.randint(1, 10))+")"*brackets2+"\n"*r.randint(-1,2))

     f.write("{}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+"{}".format(r.randint(1, 10))+"\n"*r.randint(-1,2))
     

#Question counter and grabber 
counter += 1 
f = open("addsubtract.txt","r+")
line = f.readline().rstrip("\n")
print(line) 
f.close()




#Gui 
class window_one:
     def __init__(self):
          Button(main_window,text="Quit",command=quit) .grid()
          text = canvas.create_text(200,200, text=line+"=")
          x1,y1,x2,y2 = canvas.bbox(text)
          width = x2-x1
          height=y2-y1
          Button(main_window,text="Text 2",command=self.text2) .grid()





          self.entry_left= Entry(main_window)
          canvas.create_window(250,200,window=self.entry_left,width=20)
          
          equal_button = Button(main_window,text="=",command=self.answers)
          canvas.create_window(350,80,window=equal_button)
          

          

     def quit():
          main_window.destroy()


     def answers(self):
          answer = self.entry_left.get()
          if eval(line)== int(answer):
               print("lmao")
          else:
               print("wrong lmao") 

          
     def text1(self):
          canvas.create_text(80,50,text="this is a sample of text")

     def text2(self):
          canvas.create_text(200,150,text="This is text")



          


main_window = Tk()
canvas = Canvas(main_window, width=400, height=300, bg='lightblue')
canvas.grid()

window_one()
          
