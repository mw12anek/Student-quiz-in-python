"""
Program: Elementary School Math Quiz and Grading
Authors: Michael Wanek, Chris Zambesi, Halley Deleeuw
Psuedocode:
Enter user information
1. Student name
2. Grade level
Generate 4 quiz questions by grade level:
-1st grade, addition
-2nd grade, multiplication
-3rd grade, division
Use random numbers between 1 and 100
Choose the name of your favorite teacher
Use a while loop for each quiz
Score maintained as 1 point for correct and 0 points for incorrect
Create a grade for the number of correct answers
Upload data as a .txt file named quizScore
"""
#Gather student name and grade level
print("This program will quiz elementary grade children from 1st to 3rd grades. The quiz will cover addition, multiplication, and division for each grade respectively, then a grade will be assigned based on the number correct.")
print(" ")
studentName = input("What is your first and last name? ")
print(" ")
print("Greetings " + studentName)
print(" ")
gradeLevel = int(input("Can you please input your grade level: "))
print(" ")
print("Ok " + studentName + " we are now going to begin a short quiz on mathematical operations")
print(" ")
import random
if gradeLevel == 1: #quiz for first grade
    totalCorrect1 = 0
    for count1 in range(1, 5):  # creates a loop that starts at 1 and only runs 4 times
            print("Question", count1, "find the following sum: ")
            randomInt1_1 = random.randint(1,100)    #generates 2 random numbers from 1-100
            randomInt1_2 = random.randint(1,100)
            print(randomInt1_1, "+", randomInt1_2)
            answer1_1=int(input("Please input your answer: "))
            sum1_1 = randomInt1_1 + randomInt1_2
            if answer1_1 == sum1_1:
                print("Correct, great job!")
                correct1 = 1
                totalCorrect1 += correct1  #this adds 1 to the number correct every time
                print("You have answered: ", totalCorrect1, "correct")
                if count1 == 4:
                    print("Your precentage correct is: ", totalCorrect1/4*100, "%") #this shows them their score
                    if totalCorrect1 == 1:
                        f=open("gradeFile.txt",'w') #these next few lines open the text file and write their name and quiz grade
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a D! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 2: #same as above, except if they got 2 correct
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a C! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 3: #same as above except they got 3 correct
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a B! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 4: #same as above, except they got 4 correct
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was an A! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 0: #same as above except they got none 
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a F! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
            else:        #if they get it incorrect, this loop runs 
                 print("Sorry, incorrect..")
                 if count1 == 4:
                    print("Your precentage correct is: ", totalCorrect1/4*100, "%")
                    if totalCorrect1 == 1:
                        f=open("gradeFile.txt",'w') #same as the if statement above, this block is writing to the text file 
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a D! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 2:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a C! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 3:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a B! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 4:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was an A! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect1 == 0:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a F! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
if gradeLevel == 2: #quiz for second grade
    totalCorrect2=0
    for count2 in range(1, 5):
        print("Question", count2, "find the product: ")
        randomInt2_1 = random.randint(1,12) #produces 2 random integers from 1-12
        randomInt2_2 = random.randint(1,12)
        print(randomInt2_1, "x", randomInt2_2)
        answer2_1 = int(input("Please input your answer: "))
        sum2_1 = randomInt2_1 * randomInt2_2
        if answer2_1 == sum2_1:
            print("Correct, great job!")
            correct2 = 1
            totalCorrect2 += correct2
            print("You have answered: ", totalCorrect2, "correct") #same as grade level 1 but for grade 2
            if count2 == 4:
                    print("Your precentage correct is: ", totalCorrect2/4*100, "%")
                    if totalCorrect2 == 1:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a D! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect2 == 2:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a C! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect2 == 3:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a B! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect2 == 4:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was an A! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
                    elif totalCorrect2 == 0:
                        f=open("gradeFile.txt",'w')
                        f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a F! \nYour grade level is: "+str(gradeLevel))
                        f=open("gradeFile.txt",'r')
                        print(f.read())
                        f.close()
        else:
            print("Sorry, incorrect..")
            if count2 == 4:
                print("Your precentage correct is: ", totalCorrect2/4*100, "%")
                if totalCorrect2 == 1:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a D! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect2 == 2:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a C! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect2 == 3:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a B! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect2 == 4:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was an A! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect2 == 0:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a F! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
if gradeLevel == 3: #quiz for third grade
    totalCorrect3=0
    for count3 in range(1, 5):
        print("Question", count3, "find the quotient: ")
        randomInt3_1 = random.randint(1,144)
        randomInt3_2 = random.randint(1,144)
        floatvalue1 = float(randomInt3_1/randomInt3_2)
        while floatvalue1.is_integer()== False: #this makes sure that the answer is not a decimal and if it is, to produce 2 new numbers
            randomInt3_1 = random.randint(1,144) #since answer could include a decimal
            randomInt3_2 = random.randint(1,144)
            floatvalue1 = float(randomInt3_1/randomInt3_2)
        print(randomInt3_1, "/", randomInt3_2)
        answer3_1 = int(input("Please input your answer: "))
        sum3_1 = randomInt3_1 / randomInt3_2
        if answer3_1 == sum3_1:
            print("Correct, great job!")
            correct3 = 1
            totalCorrect3 += correct3
            print("You have answered: ", totalCorrect3, "correct")
            if count3 == 4:
                print("Your precentage correct is: ", totalCorrect3/4*100, "%")
                if totalCorrect3 == 1:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a D! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 2:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a C! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 3:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a B! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 4:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was an A! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 0:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a F! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
        else:
            print("Sorry, incorrect..")
            if count3 == 4:
                print("Your precentage correct is: ", totalCorrect3/4*100, "%")
                if totalCorrect3 == 1:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a D! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 2:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a C! \nYour grade level is: "+str(gradeLevel))
                    f.close()
                elif totalCorrect3 == 3:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a B! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 4:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was an A! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
                elif totalCorrect3 == 0:
                    f=open("gradeFile.txt",'w')
                    f.write(studentName+" thank you for taking this quiz!\nYour quiz grade was a F! \nYour grade level is: "+str(gradeLevel))
                    f=open("gradeFile.txt",'r')
                    print(f.read())
                    f.close()
print(" ")
print("Let's have a little fun, and I'm going to ask you riddle. You will have three tries to answer the riddle!") #this is the fun question
riddleAnswer = str(input("What is something that you must break before you eat it? "))
answerRiddle = str('egg')
for count4 in range(1, 3): #creates a definite loop of 3 tries
    if count4 == 3:
        break
    if riddleAnswer == answerRiddle:
        print("Wow! Your answer was correct...")
        break
    elif riddleAnswer != answerRiddle:
        riddleAnswer = str(input("Nice try, but incorrect. I'll let you try again (hint: the answer is three letters long). Please type in your answer again: "))
    



