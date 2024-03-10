# Task 1: Simple Logic Puzzles

clear_sky = True
cold = False
warm = not cold

weather = clear_sky and cold
if weather == True:
   print("the weather is nice tody")

else:
   print("The weather in bad today")

weather = clear_sky or warm
if weather == True:
   print("the weather is nice today")
else:
   print("the weather is bad today")
   

# Task 2: Validating Calculations
   
A = 15
B = 20
Equation1 = A + B * A
Equation2 = (A + B) * A
print (Equation1)
print (Equation2)

if Equation1 == Equation2:
    print ("the equations have the same result")
else:
   print ("the equations have a different result")

# Task 3: Mix and Match

X = 10
Y = 20
Formula = (X <= Y) and (X % Y == 0)
if True: 
   print ("X is smaller and evenly divisable by Y") 
else:
   print ("OH NO! something has gone horribly wrong.") 


