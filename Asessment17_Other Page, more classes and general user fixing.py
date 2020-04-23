#imports 
import random as r
import re
from tkinter import *
import sympy as sym
import time as t


global text
text = 0


#Gui 
class Window_one:
     def __init__(self):
          canvas.create_text(400,30, tag="Title", text="Math Tester 6000") 
          #Quit the program button 
          Button(main_window,text="Quit",command=quit) .grid()

          #User entry area 
          self.entry_left= Entry(main_window)
          canvas.create_window(400,290,window=self.entry_left,width=50)

          #Button for level one, that includes multiplication, subtraction, addition and division
          level_one = Button(main_window, text="Level One - Add, Subtract, Multiply and Devide",command=self.level_one)
          canvas.create_window(400,80,window=level_one,width=300)

          #Button for level two which includes basic integers
          level_two = Button(main_window, text="Level Two - Integers ",command=self.level_two)
          canvas.create_window(400,110,window=level_two,width=300)

          #Button for level three which includes brackets and powers 
          level_three = Button(main_window, text="Level Three - Brackets and Powers ",command=self.level_three)
          canvas.create_window(400,140,window=level_three,width=300)

          
          #Button level four which includes basic randomly generated algebra questions 
          level_four = Button(main_window, text="Level Four - Algebra ",command=self.level_four)
          canvas.create_window(400,170,window=level_four,width=300)

          #Button for level five which inlcudes randomly generated basic differentiation questions 
          level_five = Button(main_window, text="Level Five - Differentiation ",command=self.level_five)
          canvas.create_window(400,200,window=level_five,width=300)

          test = Button(main_window, text="Personal Test",command=self.level_Personal_Test)
          canvas.create_window(400,230,window=test,width=300)

          canvas.create_text(500,390, tag="Instructions", text="Instructions: \n Welcome to Math Tester 6000! \n Here we will test very basic skills using randomly generated questions according to your math level. \n All symbols used are the same as normal except * and ** which symbol times and power to respectively. \n Select a level to start. \n Level One will test you on Addition, Subtraction, Multipication and Division. \n Level Two will test you on Brackets and Powers. \n Level Three will test you on Integers. \n Level Four will test you on Algebra. \n Level Five will test you on Differentiation. \n The Personal test is a set of questions based on ones you have gotten wrong. \n Have fun and hopefully learn alot! ")
          
          #equals button
          equal_button = Button(main_window,text="=",command=self.answers)
          canvas.create_window(435,290,window=equal_button)


     #deletes both tags of text
     def deletetext(self):
          canvas.delete("text")
          canvas.delete("starting_text")
          
     #exits the gui when quit button is pressed 
     def quit():
          #Quits the GUI 
          main_window.destroy()
          #Quits the python shell
          exit() 
          
     #commands for their according levels, assigns their according value to be filtered within other functions e.g. answers
     # def x(self):
          #deletes all previous text to prevent stacking of question text when swapping between levels
          #assigns a value to the variable in order to be filtered accordingly in functions
          #runs the procedural generation function after getting their unique value so then they can be generated according to level 
     
     def level_one(self):
          self.level = 1
          self.procedural_generation()

     def level_two(self):
          self.level = 2
          self.procedural_generation()

     def level_three(self):
          self.level = 3
          self.procedural_generation()

     def level_four(self):
          self.level = 4
          self.procedural_generation()

     def level_five(self):
          self.level = 5
          self.procedural_generation()

     def level_Personal_Test(self):
          self.level = 5
          self.procedural_generation()




     def procedural_generation(self):
          self.deletetext()
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
          self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

          if self.level == 1:
          #Question general generation, all level test 
               for i in range(20):


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
                    #note: I don't use derived values/constants with r.randint(1,10) because I would have to create seperate variables for each iteration to create true randomisation. 
                    self.QUESTION_STORAGE_FILE.write("{}{}{}".format(r.randint(1, 10),r.choice(symbols),r.randint(1, 10))+"\n"*r.randint(-1,2))

                                                   
          #level 2, Integers
          if self.level == 2:
               for i in range(20):                   
                    self.QUESTION_STORAGE_FILE.write("-{}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+("-"*r.randint(-1,2))+"{}".format(r.randint(1, 10))+"\n"*r.randint(-1,2)) 

          #level 3, Brackets and Powers
          if self.level == 3:
               for i in range(20):
                    self.QUESTION_STORAGE_FILE.write("({}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+"{})".format(r.randint(1, 10))+"**{}".format(r.randint(0, 11))+"{}".format(r.choice(symbols))+"({}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+"{})".format(r.randint(1, 10))+"\n")
          #level 4 - Basic Algebra 
          if self.level == 4:
               for i in range(20):
                    number = r.randint(1,10)
                    symbol = r.choice(symbols)
                    self.letter = r.randint(1,10)
                    #contains every algebra answer 
                    self.algebra_answer_and_calculus_letter_list.append(self.letter)
                    print(self.algebra_answer_and_calculus_letter_list)
                    equals  = "{}".format(number) + "{}".format(symbol) + "{}".format(self.letter)
                    self.QUESTION_STORAGE_FILE.write("{}".format(number)+"{}".format(symbol)+"{}".format(r.choice(self.LETTERS))+' = {}'.format(eval(equals))+"\n")

          #Level 5- Differentiation 
          if self.level == 5:
               for i in range(20):
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
          self.question_counter_text = canvas.create_text(300,260, tag="text", text="Question {}".format(self.question_counter))
          if self.level < 4: 
               self.text = canvas.create_text(400,260, tag="starting_text", text=self.edit_line+" =")
          else:
               self.text = canvas.create_text(400,260, tag="starting_text", text=self.edit_line)
          print(line)

     #function that runs when the user gets the correct answer 
     def right(self):
          print("correct")
          self.marks.append(self.edit_line+'='+self.answer+':correct')
          #text that says that it is correct 
          incorrect_correct = canvas.create_text(500,260, tag="right_wrong", text="Correct!")
          '''
          incorrect_correct.grid() 
          incorrect_correct.config(fg = "green")
          '''

     #function that runs when the user gets the wrong answer
     def wrong(self): 
          print("wrong")
          self.marks.append(self.edit_line+'='+self.answer+':wrong')
          #text that says that it is incorrect 
          incorrect_correct = canvas.create_text(500,260, tag="right_wrong", text="Incorrect!")
          '''
          incorrect_correct.config(fg="red")

          '''

     #equals button command code 
     def answers(self):
          
          #initially deletes the previous text to make way for the new text (being questions)
          self.deletetext()
          
          #ups the question counter as when equals is pressed naturally you would want to go onto the next question 
          self.question_counter += 1

          #text for the question number to tell the user what question they are on 
          self.question_counter_text = canvas.create_text(300,260, tag="text", text="Question {}".format(self.question_counter))
          self.QUESTION_STORAGE_FILE = open("procedural_generation.txt","r+")
          line = self.QUESTION_STORAGE_FILE.readlines()
          print(line)
          print(self.counter)
          #tests if the line is empty or not to prevent errors 
          while True:
               try: 
                    if line[self.counter].rstrip("\n") == "":
                         self.counter += 1
                    else:
                         break     
               except IndexError:
                    self.procedural_generation()
          #removes the "\n" artifact from going onto the next line when done with randomising a question 
          self.edit_line = line[self.counter].rstrip("\n")
          print(self.edit_line)
          #gets the user answer 
          self.answer = self.entry_left.get()



          
          #different levels need different equal checks and this accounts for every level below 4. The levels below four utilise python's basic calculation in order to compare to user answers whereas the other levels use a third party library in order to differentiate the question or use a list of algebra answers that is generated. 
          try: 
               if self.level < 4: 
                    if float(("%.2f" % eval(self.edit_line))) == float(self.answer):
                         self.right()                   
                    else:
                         self.wrong()
          except ValueError:
                    if eval(self.edit_line)== self.answer:
                         self.right()                   
                    else:
                         self.wrong()
          
          #only applies to level 4, which is algebra. This is because algebra questions require that their answers are appended, Python cannot calculate the algebra in order to compare to a user's answer without use of a third party library. 
          if self.level == 4:
               print(self.algebra_answer_and_calculus_letter_list[self.question_counter-2])
               #checks if the according answer (identified through question_counter) that are appended as they are randomly generated is the same as the user's answer. Has to use -2 because the question counter intially starts with an index of two, therefore would normally give the answer as two ahead of the question
               print(self.answer)
               try: 
                    if self.algebra_answer_and_calculus_letter_list[self.question_counter-2] == int(self.answer):
                         self.right() 
                    else:
                         self.wrong()
               except ValueError:
                     if self.algebra_answer_and_calculus_letter_list[self.question_counter-2] == self.answer:
                         self.right() 
                     else:
                         self.wrong()

                    
          #only applies to level 5, being differentiation 
          if self.level == 5:
               #if differentiated form of equation = user response
               print(sym.diff(self.edit_line))
               #identifies 'x' as the symbol, so the sympy module can go through with differentiation 
               self.x = sym.Symbol("x")

               #sym expands the equation then differentiates
               if str(sym.diff(sym.expand((self.edit_line)))) == str(self.answer):
                    self.right() 
               else:
                    self.wrong()


                    
          #ticks up txt file question counter (which has to be seperate from question_counter as it counts empty lines as questions) 
          try:
               self.counter += 1
          except IndexError:
               self.procedural_generation()

          #error checks for empty lines and accordingly ups the self.counter to move the index onto the next question 
          while True:
               try: 
                    if line[self.counter].rstrip("\n") == "":
                         self.counter += 1
                    else:
                         break
               except IndexError:
                    self.procedural_generation()
          self.edit_line = line[self.counter].rstrip("\n")


          #The algebra question already creates their own '=' with answer and the differentiation doesn't require one so this only adds '=' to the levels that need it 
          if self.level < 4: 
               self.text = canvas.create_text(400,260, tag="text", text=self.edit_line+"=")

          else:
               self.text = canvas.create_text(400,260, tag="text", text=self.edit_line)


          


          

main_window = Tk()
canvas = Canvas(main_window, width=800, height=700, bg='lightblue')
canvas.grid()

Window_one()
          
