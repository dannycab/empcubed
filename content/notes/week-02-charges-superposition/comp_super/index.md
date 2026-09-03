---
title: 'Superposition and the Computer'
weight: 7
textbook_ref: 'Section 15.9 in Matter and Interactions (4th edition)'
---

The principle of [superposition](/notes/week-02-charges-superposition/superposition/) is an overarching and powerful tool in much of physics. It is useful well beyond the electric field as you will see with the magnetic field (and as you might see in future physics courses in quantum mechanics). The fact that the electric field obeys the principle of superposition means we can define a powerful algorithm for computing the electric field at any given location from any distribution of charge. In these notes, you will read about how you can structure code to calculate the electric field from many sources of charge (though you could apply this procedure to electric potential as well).

## The Superposition Principle

The principle of superposition states that the electric field at any given location in space is determined by vector sum of the electric field due to each charge that contributes.

$$
{\overset{\rightarrow}{E}}_{net} = \sum{\overset{\rightarrow}{E}}_{i} = {\overset{\rightarrow}{E}}_{1} + {\overset{\rightarrow}{E}}_{2} + {\overset{\rightarrow}{E}}_{3} + \ldots
$$

where ${\overset{\rightarrow}{E}}_{1}$ would be the electric field from one point charge, ${\overset{\rightarrow}{E}}_{2}$ would be the electric field from a second point charge, and so on. During this week, we will focus on superposition of point charges and how we can model a line of charge using points. (Next week we will use the idea of superposition to model a continuous line of charge and other distribution of charges.)

## How can we use a computer for this?

For most real-world situations, the electric field integral cannot be solved analytically. That is, you could most likely write down the integral, but it cannot be computed because there's no anti-derivative for the function that you would be trying to integrate. So we have to think of another approach – one that makes use of the principle of superposition, which we know the electric field obeys.

Let's think through the process for computing the electric field due to a distribution of charges:

1.  Identify the “chunks” of charge that you will treat as point charges
2.  Compute the electric field due to that chunk at the specified location
3.  Write down or otherwise keep track of that value
4.  Move to the another chunk, which you treat as a point charge
5.  Compute the electric field due to the new chunk at the specified location
6.  Add that new value to the old value from steps 3 and 4
7.  Repeat steps 5-7 for another chunk; and continue repeating until you've done this for all chunks

These somewhat monotonous steps will give us an approximate value for the electric field at the point of interest. The smaller the chunks, the better the approximation. You can probably see why setting up a computer to do this makes a lot of sense. Computers are really good at doing the same calculation over and over again!

So if we want to compute the electric field at a given location due to a distribution of charges, the algorithm is just cutting the distribution into chunks, computing the electric field of each chunk as a point charge, and adding all the contributions together. This is a form of [numerical integration](https://en.wikipedia.org/wiki/Numerical_integration), which is a powerful technique in computational science. As a tool for thinking through these computational algorithms, we will sometimes write out the steps we want the computer to take in plain words rather than code - this is called **pseudocode**. The pseudocode for the electric field algorithm above is the following:

    Choose location of interest
    Choose size of chunks
    Choose starting chunk
    Set net electric field to zero

    For all the chunks in the distribution:
       
       Determine vector distance between chunk and location of interest
       Compute point charge electric field due to chunk
       Add contribution of chunk to net electric field

*You can also use pseudocode (and may have already) to help you plan and understand the code you are writing.*
