---
title: 'Plotting Potential for Multiple Charges'
weight: 51
---

*[Return to Superposition](/notes/week-02-charges-superposition/superposition/)*

To make the 3D plots in Wolfram Alpha, first you need to create a free notebook with the Wolfram Cloud just like we did before. [Starting here](https://www.open.wolframcloud.com/), click on the Wolfram Programming Lab for beginners. If you scroll down to the very bottom of the page, there is a link in blue on the left that says “Create a new notebook”. Click on this link, and it will open a new tab.

Note that if you end up with an error that say “too much memory required” you may need to create a free account with Wolfram Alpha. You can do this by clicking the “sign in” red button in the top right corner and then click on the “don't have a wolfram ID” button. After you sign in, again click on the “create a new notebook” button to get started.

This is where we will enter in the code that we want. At the top of the notebook, you will see a faint grey line (this is kind of like a cursor).

## 3D Contour Plot

To make the 3D plot, copy and paste the following code:

ContourPlot3D\[V == 5/((x - 2)^2 + y^2)^(1/2) - 5/((x - 8)^2 + y^2)^(1/2), {x, 0, 10}, {y, -5, 5}, {V, -10, 10}\]

Then press “Shift” and “Enter” together to have the computer evaluate the code (it may take a few seconds and you may get some warnings, but the code will work). You should be able to rotate the 3D graph now to look at different angles.

Try to answer the following questions, based on what you read in the notes and the 3D plot:

- What does the ((x - 2)^2 + y^2)^(1/2) and the ((x - 8)^2 + y^2)^(1/2) pieces of the code represent?
- What do the {x,0,10},{y,-5,5}, and {V,-10,10} pieces of the code do? What happens if you change those numbers?
- Where are the charges located? How do you know that there are two charges? Can you change where the charges is located (i.e., move one of the charge to x=2, y=3)?
- Could you add a third charge to this plot?
- How do you know which charge is positive? Can you change the code to be all negative or all positive instead?
- What would happen if you increase the amount of charge on one of the charges? What changes about the graph?

## 2D Equipotential Plot

In the next line (click below the graph or push the down button until the faint grey line appears again), copy and paste the following code to make the 2D equipotential lines:

ContourPlot\[5/((x - 2)^2 + y^2)^(1/2) - 5/((x - 8)^2 + y^2)^(1/2), {x, 0, 10}, {y, -5, 5}, Contours → 15, ContourShading → None, ContourLabels → True\]

Then press “Shift” and “Enter” together to have the computer evaluate the code (you may get some warnings, but the code will work). You should be able to see the equipotential lines (that look like a topographical map).

Try to answer the following questions, based on what you read in the notes and the 3D plot:

- What is different about this line of code compared to the code 3D Contour Plot?
- Where are the charge located? How can you tell in the graph?
- Can you change where the charges are located (i.e., move the charge to x=2, y=3)?
- Can you add a third charge to the plot? What changes about the graph with the third charge?
- How do you know which charges are positive? Can you change the code to make them negative instead?
- What does the “Contours → 15” part of the code mean? What happens if you increase or decrease this number?
