'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade = 95
passing = 65
if grade > passing:
    print("Student it passing")

'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
grade = 2
if grade > 65:
    print("Student it passing")
else:
    print ("Student is failing")
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age = 24
if age > 18:
    print("You can Vote!")
else:
    print ("You cannot vote")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
    
    
    
    
    
'''
I had to look up some extra stuff to learn this
'''
    
    
    
import re
    
weight= "4kgs"
pattern = "^[0-9]+kgs+$"
weightMatch =  re.match(pattern, weight)
if weightMatch:
    weight = weight.replace('kgs', '')
    weight = int(weight)*2.205
    weight = str(weight) + "lbs"
    print(weight)

'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
    
    
    
    
'''
I had to look up some extra stuff to learn this
'''
    
weight= "4lbs"
pattern = "^[0-9]+lbs+$"
weightMatch =  re.match(pattern, weight)
if weightMatch:
    weight = weight.replace('lbs', '')
    weight = int(weight)/2.205
    weight = str(weight) + "kgs"
    print(weight)
    
else:
    weight = weight.replace('kgs', '')
    weight = int(weight)*2.205
    weight = str(weight) + "lbs"
    print(weight)
