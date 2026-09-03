---
title: 'Common Commands and Tips for Python'
weight: 6
---

In this class, we are often going to use VPython to create computational models, which will serve as a powerful tool to help us create visualizations and apply the ideas in this course to more real-world contexts. Below are some of the common Python commands that we will use in this course and some coding tips compiled by previous EMP-Cubed students. (Note: we do not expect you to have any coding experience prior to this course, and we will not expect you to write a program from scratch. We will primarily be asking you to interpret chunks of code with your group members and adjust/modify pieces of code that you will be given.)

## Tips for Coding

- **Check your parentheses** - the computer will very strictly follow the order of operations (PEMDAS - Parentheses Exponents Multiplication Division Addition Subtraction). When writing out equations, make sure you have parentheses in the correct places. For example in the code below, the computer would say A = 6 but B = 4 – so these are not the same thing! Parentheses errors can be especially tricky because the program will likely run perfectly fine. Also, make sure that each of your parentheses match up – in other words every bracket has to have a buddy.

<!-- -->

    A=4+4/2
    B=(4+4)/2

- **Watch upper/lower cases** - coding is case sensitive - meaning that lowercase and uppercase letters mean something different in coding. If I had two different variables named Num_1 and num_1, Python would treat these as two distinct objects. If you initially set your variable name to be Num_1 but wrote num_1 throughout the rest of your code, Python would not know what num_1 was. Just be conscious that when you are naming or using different elements in your code, that you are writing it the same way every time.
- **Comments** - comments are informational statements that are not read or used by the program, but help you when analyzing the code. In Python, you can turn any line or part of a line in the code into a comment by putting a “#” or “##” in that line (see the examples below). You can use comments in several different ways:
  - **Notating units** - especially in long equations or calculations, keeping track of the units can help you evaluate whether your solution or equation is right. After any variable, you can add the units of that variable with a comment (see the example below).
  - **Denoting what specific lines of code do** - before a chunk of code it's often helpful to write out what the purpose of those lines of code are in plain English. This is especially helpful when trying to use code that is quite long and complicated or if you’re trying to share code with a team member. This can also be helpful when working with others communicate any misunderstanding of the code or suggest potential changes.
  - **Fixing errors in your code** - if you are not sure which line is giving you trouble, instead of deleting the entire line, just comment it out. This way if you find that that line was not the problem later, you don’t have to rewrite it, you just have to uncomment it (uncommenting is done by deleting the \#). A suggestion is to never delete lines of code unless you are 100% positive that either 1: you don’t need it or 2: it’s wrong. Basically, comments let you erase lines of code without actually erasing them.

<!-- -->

    ## Set the radius (this line would be ignored by the program)
    R=20 #cm (Everything in this line before the # would run in the program, everything after the # is ignored)

## Common Commands

- **Exponents** - to write an exponent in Python you have to use a “$**$” rather than “^”. For example, to write $A = 5.43*10^{4}$ in code you would write:

<!-- -->

    A=5.42*10**4

- **Creating Objects** - in the code we often want to create an object as a visual for the model. For example, we might want to create a sphere to represent a cloud or an arrow to represent the electric field. Python has the objects built in, but you have to tell it the characteristics of the object you want to create. For example, in the following code, the command sphere tells Python to make a sphere, pos=vec(0,3500,0) says where the center of the sphere should be positioned, color=color.white says to make the sphere white, and radius=100 sets the radius of the sphere.

<!-- -->

    cloud = sphere(pos=vec(0,3500,0), color=color.white, radius=100)

- **Object characteristics** - depending on what object you are creating there may be different characteristics that you want to define (pos, length, width, radius, color, etc). You can also change the characteristics of an object later in the code. This can be particularly useful for the updating the position of an object, which can let you simulating a moving object. In the example below, the first line of code creates a green, 2×2 box that is centered at the origin (0,0,0). In the second line of code, the box position is changed to (3,4,5) without changing the other characteristics of the box.

<!-- -->

    object1=box(pos=vec(0,0,0), length=2, width=2,color=color.green)
    object1.pos=vec(3,4,5)

- **Vectors** - In Python, you can define a variable as a vector using the “vec()” command. In this command, you simply have to define the three components of the vector (x, y, and z): vec($v_{x}$,$v_{y}$,$v_{z}$). Python will then automatically use vector subtraction/addition if you try to add two vectors. However, it will create an error if you try to add/subtract a scalar and a vector.

<!-- -->

    position1=vec(3,4,5)
    position2=vec(2,1,0)
    separation=position2-position1  #This will give separation=vec(-1,-3,-5)
    testing=separation-4 #This will give an error

- **Vector magnitude** - the “mag()” command will calculate the [magnitude of any vector](/notes/week-01-charges-field-potential/math_review/#vector_notation).

<!-- -->

    vector1=vec(1,2,3)
    mag1=mag(vector1) #This will calculate sqrt(1^2+2^2+3^2)

- **Printing values** - The command “print()” will give whatever value you place inside the print parenthesis. If you place a variable inside the parentheses, then it will print the value associated with that variable. Printing can be especially useful if you want to check a calculation that the code is running - you can then compare what the computer calculation is to what you do by hand. This helps you check your code for errors.

<!-- -->

    A=7*9/3
    print(A) #This will then print out the number 21

- **Dot Product** - the dot product is a way to [multiply two vectors](/notes/week-01-charges-field-potential/math_review/#vector_multiplication). Python has this command already programmed in:

<!-- -->

    A=vec(1,2,3)
    B=vec(4,5,6)
    AB=dot(A,B)  #This will calculate (1*4)+(2*5)+(3*6)
    print(AB)  #This will print out 32

- **Cross Product** - the cross product is another way to [multiply two vectors](/notes/week-01-charges-field-potential/math_review/#vector_multiplication). Python has this command already programmed in:

<!-- -->

    C=vec(5,6,7)
    D=vec(3,2,1)
    CD=cross(C,D)  #This will calculate (6*1-2*7)i-hat - (5*1-7*2)j-hat + (5*2-6*3)k-hat
    print(CD)  #This will print out the vector (-8, 9, -8)
