---
title: 'Plotting Electric Potential with Wolfram Alpha'
weight: 50
---

*[Return to Electric Potential](/empcubed/notes/week-01-charges-field-potential/pc_potential/)*

To make the 3D plots in Wolfram Alpha, first you need to create a free notebook with the Wolfram Cloud. [Starting here](https://www.open.wolframcloud.com/), click on the Wolfram Programming Lab for beginners. If you scroll down to the very bottom of the page, there is a link in blue on the left that says “Create a new notebook”. Click on this link, and it will open a new tab.

This is where we will enter in the code that we want. At the top of the notebook, you will see a faint grey line (this is kind of like a cursor). Copy and paste the following code:

ContourPlot3D\[V==5/(x^2+y^2)^(1/2),{x,-5,5},{y,-5,5},{V,-10,10}\]

Then press “Shift” and “Enter” together to have the computer evaluate the code (you may get some warnings, but the code will work). You should be able to rotate the 3D graph now to look at different angles.

Try to answer the following questions, based on what you read in the notes and the 3D plot:

- What does the (x^2+y^2)^(1/2) piece of the code represent?
- What do the {x,-5,5},{y,-5,5}, and {V,-10,10} pieces of the code do? What happens if you change those numbers?
- Where is the charge located? Can you change where the charge is located (i.e., move the charge to x=2, y=3)?
- How do you know the charge is positive? Can you change the code to be negative instead?
- How would you increase the amount of charge in the code? What changes about the graph?
