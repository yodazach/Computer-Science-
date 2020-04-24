#imports
#random allows me to randomise various things 
import random as r
#tkinter allows me to display a GUI
from tkinter import *
#Sympy allows me to do complex calculations such as differentiation. To use it you probobally have to pip install it.
import sympy as sym


class Main_window_and_program:
     def __init__(self):
          canvas.create_text(400,30, tag="Title", text="Math Tester 6000", font=("Helvetica", 30, "bold italic")) 
          #Quit the program button 
          Button(main_window,text="Quit",command=quit) .grid()

          #User entry area 
          self.USER_INPUT_AREA = Entry(main_window)
          canvas.create_window(400,290,window=self.USER_INPUT_AREA,width=50)

          #Button for level one, that includes multiplication, subtraction, addition and division
          LEVEL_ONE_BUTTON = Button(main_window, text="Level One - Add, Subtract, Multiply and Devide",font=("Helvetica", 9, "bold"),command=self.level_one_condition)
          canvas.create_window(400,80,window=LEVEL_ONE_BUTTON,width=300)

          #Button for level two which includes basic integers
          LEVEL_TWO_BUTTON = Button(main_window, text="Level Two - Integers ",font=("Helvetica", 9, "bold"),command=self.level_two_condition)
          canvas.create_window(400,110,window=LEVEL_TWO_BUTTON,width=300)

          #Button for level three which includes brackets and powers 
          LEVEL_THREE_BUTTON = Button(main_window, text="Level Three - Brackets and Powers ",font=("Helvetica", 9, "bold"), command=self.level_three_condition)
          canvas.create_window(400,140,window=LEVEL_THREE_BUTTON,width=300)

          
          #Button level four which includes basic randomly generated algebra questions 
          LEVEL_FOUR_BUTTON = Button(main_window, text="Level Four - Algebra ",font=("Helvetica", 9, "bold"),command=self.level_four_condition)
          canvas.create_window(400,170,window=LEVEL_FOUR_BUTTON,width=300)

          #Button for level five which inlcudes randomly generated very basic introductory differentiation questions 
          LEVEL_FIVE_BUTTON = Button(main_window, text="Level Five - Differentiation ",font=("Helvetica", 9, "bold"),command=self.level_five_condition)
          canvas.create_window(400,200,window=LEVEL_FIVE_BUTTON,width=300)

          #Button for the user's personal test 
          PERSONAL_TEST_BUTTON = Button(main_window, text="Personal Test",font=("Helvetica", 9, "bold"),command=self.level_personal_test_condition)
          canvas.create_window(400,230,window=PERSONAL_TEST_BUTTON,width=300)

          #creates the instruction text. Sorry that it goes off screen. 
          canvas.create_text(500,440, tag="Instructions", text="Instructions: \n Welcome to Math Tester 6000! \n Here we will test very basic skills using randomly generated \n questions according to your math level. \n All symbols used are the same as normal except * and ** which represent \n multipication and exponents, respectively. \n Another thing to note is that questions that requre an answer that has decimal places will be rounded \n to two decimal places. \n \n Select a level to start. \n Level One will test you on Addition, Subtraction, Multipication and Division. \n Level Two will test you on Brackets and Powers. \n Level Three will test you on Integers. \n Level Four will test you on Algebra. \n Level Five will test you on Differentiation. \n The Personal test is a set of questions based on ones you have gotten wrong. \n Have fun and hopefully learn a lot! ")
          
          #equals button, pretty self explanatary 
          EQUALS_BUTTON = Button(main_window,text="=",command=self.answers)
          canvas.create_window(435,290,window=EQUALS_BUTTON)

          #both of these are initially set to [] to stop the attribute error 
          self.question_marks = []
          self.joined_personal_test_question_list = []

          #initial defining of level to prevent attribute error
          self.level = 0
          
     #function for creating the end results menu when a test is completed by the user 
     def create_results_window(self):
          #toplevel() widget is used to display this as an extra window
          RESULTS_WINDOW = Toplevel(main_window)
          #adds a canvas widget to it, give it height and a color 
          RESULTS_WINDOW_CANVAS = Canvas(RESULTS_WINDOW, width=300, height=400, bg='lightblue')
          #assigns the canvas to a grid 
          RESULTS_WINDOW_CANVAS.grid()
          RESULTS_WINDOW_CANVAS.create_text(150,20, text="Results:", font=("Helvetica", 9, "bold"))
          RESULTS_WINDOW_CANVAS.create_text(150,200, text="{} \n {} out of {} Correct! ".format("".join(self.test_results),self.results_right_answer_counter, len(self.test_results))) 

          
     #deletes both tags of text so then it stops stacking of text 
     def delete_text(self):
          #deletes text with the tag "text" 
          canvas.delete("text")
          #deletes text with the tag "starting_text")
          canvas.delete("starting_text")
          
     #exits the gui when quit button is pressed 
     def quit():
          #Quits the GUI 
          main_window.destroy()
          #Quits the python shell
          exit()


          
     """ commands for their according levels, assigns their according value to be filtered within other functions e.g. answers. 
      def x(self):
          makes personal_test_chosen_or_not = false to stop attribute error 
          resets/sets personal test question list to stop attribute error 
          assigns a value to the variable in order to be filtered accordingly in functions
          runs the procedural generation function after getting their unique value so then they can be generated according to level """

     
     def level_one_condition(self):
          self.personal_test = False 
          self.personal_test_question_list = [] 
          self.level = 1
          self.procedural_generation()

     def level_two_condition(self):
          self.personal_test = False 
          self.personal_test_question_list = [] 
          self.level = 2
          self.procedural_generation()

     def level_three_condition(self):
          self.personal_test = False 
          self.personal_test_question_list = [] 
          self.level = 3
          self.procedural_generation()

     def level_four_condition(self):
          self.personal_test = False 
          self.personal_test_question_list = [] 
          self.level = 4
          self.procedural_generation()

     def level_five_condition(self):
          self.personal_test = False 
          self.personal_test_question_list = [] 
          self.level = 5
          self.procedural_generation()

     def level_personal_test_condition(self):
          #makes it so the personal test is usable if they have completed atleast one question 
          if len(self.joined_personal_test_question_list) > 0:
               #runs specific lines of code in procedural generation 
               self.personal_test = True
               #runs procedural generation 
               self.procedural_generation()

     def procedural_generation(self):
          self.right_answer_counter = 0
          self.delete_text()
          #opens the file at which I generate the level one math questions
          self.QUESTION_STORAGE_FILE = open("question_storage_file.txt","r+")

          #deletes the contents of the randomly generated math problems on the file 
          self.QUESTION_STORAGE_FILE.truncate(0)

          #this will allow for a detailed history of his marks 
          self.question_marks = []

          #symbols variable, contains the symbols in order to randomise them 
          symbols = ["+","-","/","*"]
          #letters variable, contains the letters in order to randomise them for algebra questions 
          self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

          #if level == 1 run the according randomisation for level 1
          if self.level == 1 and self.personal_test == False :
          #Question general generation, all level test 
               for i in range(20):
                    #this is to prevent index errors when the symbols list becomes empty from using all the symbols in the random generation 
                    if symbols == []:
                         symbols = ["+","-","/","*"]
                    
                    """ line that writes the randomised questions to the file and randomises the questions 
                    note: I don't use derived values/constants with r.randint(1,10) because I would have to create seperate variables for each iteration to create true randomisation.
                    in order to decrease the chance of stupidly low or high numbers I made it so every symbol can usually only appear once through popping the symbol used off of the list. The -len is to get the index of the symbol
                    list so I can properly randomise this. Next time I could improve upon this a huge amount because I thought that r.randint was r.randint(x<,>x). This would improve my code a whole lot because I wouldn't need
                    empty line error trapping. I would normally fix this but I don't have enough time and I don't want something to stop working. It works fine without this improvement however."""
                    self.QUESTION_STORAGE_FILE.write("{}{}{}".format(r.randint(1, 10),symbols.pop(r.randint(-len(symbols),0)),r.randint(1, 10))+"\n"*r.randint(-1,2))
                    print(symbols)
                    
          #level 2, Integers
          if self.level == 2 and self.personal_test == False:
               for i in range(20):
                    self.QUESTION_STORAGE_FILE.write("-{}{}\n".format(r.randint(1, 10),r.choice(symbols)+"-"*r.randint(-1,1)+"{}".format(r.randint(1, 10))+"\n"))
                    

          #level 3, Brackets and Powers
          if self.level == 3 and self.personal_test == False:
               for i in range(20):
                    #randomises brackets and powers questions, could format this better alike the generation above but I got the error message: IndexError: Replacement index 7 out of range for positional args tuple.
                    self.QUESTION_STORAGE_FILE.write("({}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))
                                                     #I use r.randint 0,4 to prevent too large of numbers because of too high exponents
                                                     +"{})".format(r.randint(1, 10))+"**{}".format(r.randint(0, 4))+"{}".format(r.choice(symbols))
                                                     +"({}".format(r.randint(1, 10))+"{}".format(r.choice(symbols))+"{})".format(r.randint(1, 10))+"\n")

          #level 4 - Basic Algebra 
          if self.level == 4 and self.personal_test == False:
               #acts as a list of answers for algebra
               self.algebra_answer_list = []
               #resets personal test answer list, so wrong answers can be appended 
               self.algebra_personal_test_answer_list = []
               for i in range(20):
                    number = r.randint(1,10)
                    symbol = r.choice(symbols)
                    self.letter = r.randint(1,10)
                    #contains every algebra answer 
                    self.algebra_answer_list.append(self.letter)
                    equals  = "{}".format(number) + "{}".format(symbol) + "{}".format(self.letter)
                    self.QUESTION_STORAGE_FILE.write("{}".format(number)+"{}".format(symbol)+"{}".format(r.choice(self.LETTERS))+' = {}'.format(("%.2f" % eval(equals)))+"\n")

          #Level 5- Differentiation 
          if self.level == 5 and self.personal_test == False:
               for i in range(20):
                    number = r.randint(1,10)
                    symbol = r.choice(symbols)
                    self.letter = r.randint(1,10)
                    self.QUESTION_STORAGE_FILE.write("{}*x**{}+{}".format(r.randint(0,11),r.randint(1,11),r.randint(1,11))+"\n")
                    
          if self.personal_test == True:
               #writes the questions that the user got wrong to the question storage file to create the personal test
               self.QUESTION_STORAGE_FILE.write(self.joined_personal_test_question_list)
               if self.level == 4:
                    self.algebra_answer_list = []
                    self.algebra_answer_list.extend(self.algebra_personal_test_answer_list)
               
          #question self.counter and grabber
          self.question_counter = 0
          self.counter = 0
          self.QUESTION_STORAGE_FILE = open("question_storage_file.txt","r+")
          line = self.QUESTION_STORAGE_FILE.readlines(self.counter)
          self.edit_line = line[self.counter].rstrip("\n")
          self.question_counter += 1
          self.question_counter_text = canvas.create_text(260,260, tag="text", text="Question {}".format(self.question_counter),font=("Helvetica", 9, "bold"))
          if self.level < 4: 
               self.text = canvas.create_text(400,260, tag="starting_text", text=self.edit_line+" =")
          if self.level == 4:
               self.text = canvas.create_text(400,260, tag="starting_text", text=self.edit_line)
          if self.level == 5:
               self.text = canvas.create_text(400,260, tag="starting_text", text=self.edit_line+" = f(x)")

     #function that runs when the user gets the correct answer 
     def right(self):
          self.right_answer_counter += 1
          #creates the question results for the results page and appends them
          self.question_marks.append("{}.    ".format(self.question_counter-1)+self.edit_line+'='+self.answer+' : CORRECT \n')
          #text that says that it is correct 
          incorrect_correct = canvas.create_text(540,260, tag="text", text="Correct!",font=("Helvetica", 9, "bold"))

     #function that runs when the user gets the wrong answer
     def wrong(self): 
          self.QUESTION_STORAGE_FILE = open("question_storage_file.txt","r+")
          line = self.QUESTION_STORAGE_FILE.readlines()
          self.question_marks.append("{}.    ".format(self.question_counter-1)+self.edit_line+'='+self.answer+' : WRONG \n')
          #stops appending questions if the personal test is running, this can get out of hand quite quickly
          if self.personal_test == False:
               #appends the question that was wrong (line[self.counter]) into a list containing the personal test questions
               self.personal_test_question_list.append(line[self.counter])
          #joins it into one whole string to be subsequently written to the txt file normally like the other levels 
          self.joined_personal_test_question_list = "".join(self.personal_test_question_list)
          #appends the answers for the questions that the user got wrong into another list to be used on the personal test
          if self.level == 4:
               self.algebra_personal_test_answer_list.append(self.algebra_answer_list[self.question_counter-2])
          #text that says that it is incorrect 
          incorrect_correct = canvas.create_text(540,260, tag="text", text="Incorrect!",font=("Helvetica", 9, "bold"))

     #equals button command code 
     def answers(self):
          if self.level > 0: 
               #initially deletes the previous text to make way for the new text (being questions)
               self.delete_text()
               
               #ups the question counter as when equals is pressed naturally you would want to go onto the next question 
               self.question_counter += 1

               #text for the question number to tell the user what question they are on 
               self.question_counter_text = canvas.create_text(260,260, tag="text", text="Question {}".format(self.question_counter),font=("Helvetica", 9, "bold"))
               self.QUESTION_STORAGE_FILE = open("question_storage_file.txt","r+")
               line = self.QUESTION_STORAGE_FILE.readlines()
               #tests if the line is empty or not to prevent errors 
               #removes the "\n" artifact from going onto the next line when done with randomising a question 
               self.edit_line = line[self.counter].rstrip("\n")
               #gets the user answer 
               self.answer = self.USER_INPUT_AREA.get()

               """ different levels need different equal checks and this accounts for every level below 4. The levels below four utilise python's basic calculation in order to compare to user answers whereas the other levels
               use a third party library in order to differentiate the question or use a list of algebra answers that is generated. """
               try: 
                    if self.level < 4:
                         """ checks if answer = python answer to two decimal places (with the %.2f) without that differences between python calculation and individual calculation may be different and would decrease user
                         functionality having to enter in so many decimal places """
                         if float(("%.2f" % eval(self.edit_line))) == float(self.answer):
                              self.right()                   
                         else:
                              self.wrong()
               except ValueError:
                         if eval(self.edit_line)== self.answer:
                              self.right()                   
                         else:
                              self.wrong()
               
               """ only applies to level 4, which is algebra. This is because algebra questions require that their answers are appended, Python cannot calculate the algebra in order to compare to a
               user's answer without use of a third party library. """
               if self.level == 4:
                    """ checks if the according answer (identified through question_counter) that are appended as they are randomly generated is the same as the user's answer. Has to use -2 because the
                    question counter intially starts with an index of two, therefore would normally give the answer as two ahead of the question. """
                    try: 
                         if self.algebra_answer_list[self.question_counter-2] == int(self.answer):
                              self.right() 
                         else:
                              self.wrong()
                    except ValueError:
                          if self.algebra_answer_list[self.question_counter-2] == self.answer:
                              self.right() 
                          else:
                              self.wrong()

                         
               #only applies to level 5, being differentiation 
               if self.level == 5:
                    #identifies 'x' as the symbol, so the sympy module can go through with differentiation
                    self.x = sym.Symbol("x")
                    #sym differentiates, then sees if it equals user answer 
                    if str(sym.diff((self.edit_line))) == str(self.answer):
                         self.right() 
                    else:
                         self.wrong()

               #ticks up txt file question counter (which has to be seperate from question_counter as it counts empty lines as questions) 
               self.counter += 1

               #error checks for empty lines and accordingly ups the self.counter to move the index onto the next question 
               while True:
                    try: 
                         if line[self.counter].rstrip("\n") == "":
                              self.counter += 1
                         else:
                              break
                    except IndexError:
                         """ since procedural generation resets my question_marks and right_answer_counter I have to append them to other variables for use in my results window which is called after procedural generation. Without this the
                         results window is subsequently blank. I know that there is a more efficient way to do this but I can't think of it. """
                         #right answer counter for results reset, so it doesn't keep adding all past results onto the test
                         self.results_right_answer_counter = []
                         #appends the right answer counter for use in the results menu 
                         self.results_right_answer_counter.append(self.right_answer_counter)
                         #overall test results reset 
                         self.test_results = []
                         #extends the individual question marks into a non-reset on procedural generation call variable for use in result window 
                         self.test_results.extend(self.question_marks)
                         self.procedural_generation()
                         self.create_results_window()
                         return 
               self.edit_line = line[self.counter].rstrip("\n")

               #The algebra question already creates their own '=' with answer and the differentiation doesn't require one so this only adds '=' to the levels that need it 
               if self.level < 4: 
                    self.text = canvas.create_text(400,260, tag="text", text=self.edit_line+"=")

               if self.level == 4:
                    self.text = canvas.create_text(400,260, tag="text", text=self.edit_line)

               if self.level == 5:
                    self.text = canvas.create_text(400,260, tag="text", text=self.edit_line+" = f(x)")


          
#creates the window in order to be edited 
main_window = Tk()
#canvas size and color 
canvas = Canvas(main_window, width=800, height=700, bg='lightblue')
#assigns the canvas to a grid layout 
canvas.grid()
#runs the 
Main_window_and_program()
          
