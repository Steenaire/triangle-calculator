#This script takes user input and uses trig to calculate a triangle, then draws the triangle in turtle

import math
import turtle

def AngleLarge():
    angle = int(input("I'm sorry, that angle is too large, all 3 angles must add up to exactly 180 degrees. Enter a new angle:"))
    return angle

def AngleZero():
    angle = int(input("I'm sorry, your angle cannot be zero. Enter a new angle:"))
    return angle

def SideZero():
    side = int(input("I'm sorry, your side cannot be zero. Enter a new side:"))
    return side

def TriangleInequalityTheorem():
    print("I'm sorry, the Triangle Inequality Theorem states that the sum of any 2 sides of a triangle must be greater than the measure of the third side. This is an impossible triangle :)")
    sidea = int(input("Enter your first side:"))
    sideb = int(input("Enter your second side:"))
    sidec = int(input("Enter your third side:"))
    return sidea, sideb, sidec

def ThirdAngleCalc(angleA, angleB):
    angleC = (180-(angleA+angleB))
    return angleC

def LawOfSines(side, angleA, angleC):
    newSide = abs(side*(math.sin(math.radians(angleA)))/math.sin(math.radians(angleC)))
    return newSide

#Defining a triangle with two angles and a side not in-between them:
def AAS():
    angleA = int(input("Enter your first angle:"))
    
    #Checks that the angle is not too large to be possible:
    while angleA>178:
        angleA = AngleLarge()
        
    #Checks that the angle is non-zero
    while angleA==0:
        angleA = AngleZero()
        
    #Makes the angle positive, if it was entered as a negative:
    if angleA<0:
        angleA = abs(angleA)
        
    else:
        angleC = int(input("Enter your second angle:"))

        #Checks that the angle is not too large to be possible:
        while (angleA+angleC)>179:
            angleC = AngleLarge()

        #Checks that the angle is non-zero
        while angleC==0:
            angleC = AngleZero()

        #Makes the angle positive, if it was entered as a negative:
        if angleC<0:
            angleC = abs(angleC)

    #Calculating the third angle
    angleB = ThirdAngleCalc(angleA,angleC)
        
    sidec = int(input("Enter your side:"))

    #Calculate remaining sides using the law of sines:
    sidea = LawOfSines(sidec, angleA, angleC)
    sideb = LawOfSines(sidec, angleB, angleC)

    drawing(sidea, sideb, sidec, angleA, angleB, angleC)

#Defining a triangle with two angles and a side in-between them:
def ASA():
    angleA = int(input("Enter your first angle:"))
    while angleA>=178:
        angleA = AngleLarge()
    while angleA == 0:
        angleA = AngleZero()

    angleB = int(input("Enter your second angle:"))
    while (angleA+angleB)>=179:
        angleB = AngleLarge()
    while angleB == 0:
        angleB = AngleZero()

    angleC = ThirdAngleCalc(angleA,angleB)
        
    sidec = int(input("Enter your side:"))
    while sidec == 0:
        sidec = SideZero()
    
    sidea = LawOfSines(sidec, angleA, angleC)
    sideb = LawOfSines(sidec, angleB, angleC)

    drawing(sidea, sideb, sidec, angleA, angleB, angleC)

#Defining an angle with three sides only
def SSS():
    
    sidea = int(input("Enter your first side:"))
    while sidea == 0:
        sidea = SideZero()
    sideb = int(input("Enter your second side:"))
    while sideb == 0:
        sideb = SideZero()
    sidec = int(input("Enter your third side:"))
    while sidec == 0:
        sidec = SideZero()
    
    while sidea+sideb<=sidec or sideb+sidec<=sidea or sidea+sidec<=sideb:
        sidea, sideb, sidec = TriangleInequalityTheorem()

    angleA = math.degrees(math.acos(((sideb*sideb)+(sidec*sidec)-(sidea*sidea))/(2*sideb*sidec)))

    angleB = math.degrees(math.acos(((sidec*sidec)+(sidea*sidea)-(sideb*sideb))/(2*sidec*sidea)))

    angleC = ThirdAngleCalc(angleA,angleB)
    
    drawing(sidea, sideb, sidec, angleA, angleB, angleC)

#Defining a right-triangle by its hypotenuse and a leg
def HL():
    #Hypotenuse-Leg is only for right-triangles
    angleC = 90

    sidec = int(input("Enter the length of the hypotenuse:"))
    while sidec == 0:
        sidec = SideZero()
    sideb = int(input("Enter the length of a leg:"))
    while sideb == 0:
        sideb = SideZero()

    sidea = math.sqrt((sidec*sidec)-(sideb*sideb))

    angleA = math.degrees(math.acos(((sideb*sideb)+(sidec*sidec)-(sidea*sidea))/(2*sideb*sidec)))

    angleB = math.degrees(math.acos(((sidec*sidec)+(sidea*sidea)-(sideb*sideb))/(2*sidec*sidea)))
    
    drawing(sidea, sideb, sidec, angleA, angleB, angleC)

#Drawing the triangle that the user has defined:
def drawing(sidea, sideb, sidec, angleA, angleB, angleC):

    angleA = round(angleA,2)
    angleB = round(angleB,2)
    angleC = round(angleC,2)
    sidea = round(sidea,2)
    sideb = round(sideb,2)
    sidec = round(sidec,2)

    print("Your sides are:")
    print(sidea, sideb, sidec)
    print("And your angles are:")
    print(angleA, angleB, angleC)

    if sidea==sideb and sideb==sidec:
        print("You made an equillateral triangle!")
    elif angleA==90 or angleB==90 or angleC==90:
        print("You made a right triangle!")
    elif angleA==angleB or angleB==angleC or angleC==angleA:
        print("You made an isoceles triangle!")
    elif sidea!=sideb and sideb!=sidec and sidec!=sidea:
        print("You made a scalene triangle!")

    triWin = turtle.Screen()
    triDraw = turtle.Turtle()
    turtle.bgcolor("pink")
    triDraw.speed(5)

    triDraw.forward(sidea)
    triDraw.left(180-angleC)
    if angleC==90:
        square(triDraw, ((sidea+sideb)/20))
    triDraw.forward(sideb)
    triDraw.left(180-angleA)    
    if angleA==90:
        square(triDraw, ((sideb+sidec)/20))
    triDraw.goto(0,0)
    if angleB==90:
        triDraw.left(90)
        square(triDraw, ((sidea+sidec)/20))

    triWin.exitonclick()

#Makes a little square in the right angle of any right triangles the user might make:
def square(T, S):
    for k in range(0,4):
        T.forward(S)
        T.left(90)
    
def main():
    query = "Y"
    while query=="Y" or query=="y" or query=="Yes" or query=="yes":
        query = input("Would you like to draw a triangle? (Y/N)")
        if query=="Y" or query=="y" or query=="Yes" or query=="yes":
            defType = input("How would you like to define your triangle? AAS, ASA, SSS, or HL?")

            while defType!="AAS" and defType!="aas" and defType!="ASA" and defType!="asa" and defType!="SSS" and defType!="sss" and defType!="HL" and defType!="hl":
                print("I'm sorry, please only choose AAS, ASA, SAS, SSS, or HL.")
                defType = input("How would you like to define your triangle?")

            if defType=="AAS" or defType=="aas":
                AAS()
            elif defType=="ASA" or defType=="asa":
                ASA()
            elif defType=="SSS" or defType=="sss":
                SSS()
            elif defType=="HL" or defType=="hl":
                HL()
        else:
            print("Maybe next time :)")
    
main()
