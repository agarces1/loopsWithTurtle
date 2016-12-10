#steps can be named anything it is like a variable
#plz no single letter variables, please give it a good name.
import turtle
#for steps in range(4):#only indented code runs
#    turtle.forward(100);
#    turtle.right(90);
#turtle.color('red');
#turtle.forward(200);
#You can have loops inside loops
#for steps in range(4):#everytime this runs once
#    turtle.forward(100);
#    turtle.right(90);
#    for moresteps in range(4): #this runs 4 times
#        turtle.forward(100);
#        turtle.right(90);
#we can use a variable to decide the number of sides our object will have
nbrSides = 6
for steps in range(nbrSides):
    turtle.forward(100);
    turtle.right(360/nbrSides);
    for moreSteps in range(nbrSides):
        turtle.forward(50);
        turtle.right(360/nbrSides);
#Accessing the loop value
for steps in range(4):
    print (steps);
#if you need to start counting from 1 you can specify numbers to count to and from
for steps in range(1,4):
    print(steps);
#you can also tell the loop to skip values by specifying a step
for steps in range(1,10,2):#basically jump by 2
    print(steps);
#you can specify what values it uses like a for each loop
for steps in [1,2,3,4,5]:
    print(steps);