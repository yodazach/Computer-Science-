#imports 
import random as r
import re
from tkinter import *
import sympy as sym




global text
text = 0


#Gui 
class Window_one:
     def __init__(self):
          #quit button 
          Button(main_window,text="Quit",command=quit) .grid()
          
          #extra button 
          Button(main_window,text="Text 2",command=self.text2) .grid()


          #entry 
          self.entry_left= Entry(main_window)
          canvas.create_window(200,230,window=self.entry_left,width=50)

          #button for level one, that includes multiplication, subtraction, addition and division
          level_one = Button(main_window, text="Level One - Add, Subtract, Multiply and Devide",command=self.level_one)
          canvas.create_window(200,20,window=level_one)


          level_two = Button(main_window, text="Level Two - Add, Subtract, Multiply and Devide",command=self.level_two)
          canvas.create_window(200,50,window=level_two)


          level_three = Button(main_window, text="Level three - Add, Subtract, Multiply and Devide",command=self.level_three)
          canvas.create_window(200,80,window=level_three)

          level_four = Button(main_window, text="Level four - Add, Subtract, Multiply and Devide",command=self.level_four)
          canvas.create_window(200,110,window=level_four)

          level_five = Button(main_window, text="Level Five - Add, Subtract, Multiply and Devide",command=self.level_five)
          canvas.create_window(200,140,window=level_five)

          test = Button(main_window, text="Personal Test",command=self.level_four)
          canvas.create_window(200,170,window=test)

          
          
          #equals button
          equal_button = Button(main_window,text="=",command=self.answers)
          canvas.create_window(350,80,window=equal_button)

     def deletetext(self):
          canvas.delete("text")
          canvas.delete("starting_text")
          

     def quit():
          main_window.destroy()

     def level_one(self):
          self.deletetext()
          self.level = 1
          self.procedural_generation_level_modifier = 1 
          self.procedural_generation()

     def level_two(self):
          self.deletetext()
          self.level = 2
          self.procedural_generation_level_modifier = 1 
          self.procedural_generation()

     def level_three(self):
          self.deletetext()
          self.level = 3
          self.procedural_generation_level_modifier = 1 
          self.procedural_generation()

     def level_four(self):
          self.deletetext()
          self.level = 4
          self.procedural_generation_level_modifier = 1 
          self.procedural_generation()

     def level_five(self):
          self.deletetext()
          self.level = 5
          self.procedural_generation_level_modifier = 1 
          self.procedural_generation()




     def procedural_generation(self):
          #opens the file at which I generate the level one math questions
          self.QUESTION_STORAGE_FILE = open("procedural_generation.txt","r+")

          #deletes the contents of the randomly generated math problems on the file 
          self.QUESTION_STORAGE_FILE.truncate(0)

          #this will allow for a detailed history of his self.marks
          self.marks = []

          #acts as a list of answers for algebra 
          self.algebra_answer_and_calculus_letter_list = []


          #symbols variable
          symbols = ["+","-","/","*"]
          self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

          if self.level == 1:
          #Question general generation, all level test 
               for i in range(100):


                    #shitty bracket generation 
                    '''
                    #plays around of chances of brackets
                    brackets = r.randint(0,1) * r.randint(0,1) * r.randint(0,1)
                    brackets2 = r.randint(0,1) * r.randint(0,1) * r.randint(0,1)
                    #creates chance of brackets that include everything 
                    if brackets == brackets2:
                         brackets3 = r.randint(0,1)
                    else:
                         brackets3 = 1
                    '''
                    #actual generation
                    #shitty bracket generation: QUESTION_STORAGE_FILEwrite("("*brackets + "{}".format(r.randint(1, 10))+")"*brackets*brackets3 +"{}".format(r.choice(symbols))+"("*brackets2*brackets3+"{}".format(r.randint(1, 10))+")"*brackets2+"\n"*r.randint(-1,2))

                    self.QUESTION_STORAGE_FILE.write("{}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+"{}".format(r.randint(1, 10))+"\n"*r.randint(-1,2))


          #level 2, Integers
          if self.level == 2:
               for i in range(100):                   
                    self.QUESTION_STORAGE_FILE.write("-{}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+("-"*r.randint(-1,2))+"{}".format(r.randint(1, 10))+"\n"*r.randint(-1,2)) 

          #level 3, Brackets and Powers 
          
          #level 4 - Basic Algebra 
          if self.level == 4:
               for i in range(100):
                    number = r.randint(1,10)
                    symbol = r.choice(symbols)
                    self.letter = r.randint(1,10)
                    #contains every algebra answer 
                    self.algebra_answer_and_calculus_letter_list.append(self.letter)
                    print(self.algebra_answer_and_calculus_letter_list)
                    equals  = "{}".format(number) + "{}".format(symbol) + "{}".format(self.letter)
                    self.QUESTION_STORAGE_FILE.write("{}".format(number)+"{}".format(symbol)+"{}".format(r.choice(self.letters))+' = {}'.format(eval(equals))+"\n")

          #Level 5- Differentiation 
          if self.level == 5:
               for i in range(100):
                    number = r.randint(1,10)
                    symbol = r.choice(symbols)
                    self.letter = r.randint(1,10)
                    self.QUESTION_STORAGE_FILE.write("{}".format(number)+"{}".format(symbol)+"({}*x**{})".format(r.randint(0,11),r.randint(1,11))+"\n")
          #question self.counter and grabber
          self.question_counter = 0
          self.counter = 0
          self.QUESTION_STORAGE_FILE = open("procedural_generation.txt","r+")
          line = self.QUESTION_STORAGE_FILE.readlines(self.counter)
          self.edit_line = line[self.counter].rstrip("\n")
          self.question_counter += 1
          self.question_counter_text = canvas.create_text(100,200, tag="text", text="Question {}".format(self.question_counter))
          if self.level < 4: 
               self.text = canvas.create_text(200,200, tag="starting_text", text=self.edit_line+"=")
          else:
               self.text = canvas.create_text(200,200, tag="starting_text", text=self.edit_line)
          print(line)



     def answers(self):

          self.deletetext()
          self.question_counter += 1     
          self.question_counter_text = canvas.create_text(100,200, tag="text", text="Question {}".format(self.question_counter))
          self.QUESTION_STORAGE_FILE = open("procedural_generation.txt","r+")
          line = self.QUESTION_STORAGE_FILE.readlines()
          print(line)
          print(self.counter)
          while True:
               if line[self.counter].rstrip("\n") == "":
                    self.counter += 1
                    break 
               else:
                    break
          self.edit_line = line[self.counter].rstrip("\n")
          print(self.edit_line) 
          answer = self.entry_left.get()

          if self.level < 4: 
               if eval(self.edit_line)== int(answer):
                    print("correct")
                    self.marks.append(self.edit_line+'='+answer+':correct')
                    
               else:
                    print("wrong")
                    self.marks.append(self.edit_line+'='+answer+':wrong')
          if self.level == 4:
               print(self.algebra_answer_and_calculus_letter_list[self.question_counter])
               if self.algebra_answer_and_calculus_letter_list[self.question_counter] == int(answer):
                    print("correct")
                    self.marks.append(self.edit_line+'='+answer+':correct') 


               else:
                    print("wrong")
                    self.marks.append(self.edit_line+'='+answer+':wrong')

          if self.level == 5:
               #if differentiated form of equation = user response
               print(sym.diff(self.edit_line))
               self.x = sym.Symbol("x")

               #sym expands the equation then differentiates
               if sym.diff(sym.expand((self.edit_line))) == answer:
                    print("correct")
                    self.marks.append(self.edit_line+'='+answer+':correct') 


               else:
                    print("wrong")
                    self.marks.append(self.edit_line+'='+answer+':wrong')
               
          self.counter += 1
          while True:
               if line[self.counter].rstrip("\n") == "":
                    self.counter += 1
                    break 
               else:
                    break
          print(self.counter)
          self.edit_line = line[self.counter].rstrip("\n")
          if self.level < 4: 
               self.text = canvas.create_text(200,200, tag="text", text=self.edit_line+"=")

          else:
               self.text = canvas.create_text(200,200, tag="text", text=self.edit_line)



     def text1(self):
          canvas.create_text(80,50,text="this is a sample of text")

     def text2(self):
          canvas.create_text(200,150,text="This is text")

main_window = Tk()
canvas = Canvas(main_window, width=400, height=300, bg='lightblue')
canvas.grid()

Window_one()
          
