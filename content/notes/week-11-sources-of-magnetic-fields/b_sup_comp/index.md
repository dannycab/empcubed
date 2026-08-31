---
title: 'Using Superposition of Magnetic Field and the Computer'
weight: 1
---

In the [previous page of notes](/notes/week-10-magnetic-field-of-a-wire/b_current/), we talked about how you can use superposition to calculate the magnetic field from a current rather than thinking about each individual moving charge. We ended up with an equation for the magnetic field where

$$
{\overset{\rightarrow}{B}}_{tot} = \int\frac{\mu_{0}}{4\pi}\frac{I \cdot d\overset{\rightarrow}{l} \times \widehat{r}}{r^{2}}
$$

This equation tells us that if we split a line of current ($I$) into small chunks of length ($d\overset{\rightarrow}{l}$), we can calculate the magnetic field at an observation point from that chunk of length (using the $\overset{\rightarrow}{r}$). The integral then allows us to add the magnetic field from each little chunk to find the net magnetic field at the observation point.

While calculating the integral will give you an exact value for the magnetic field, it is possible to end up with an integral that is difficult or impossible to solve. Instead we can use the fact that the magnetic field obeys the principle of superposition to define a powerful algorithm for computing the magnetic field at any given location from any shape of current/wire. This is very similar to what we did with the [electric field from a line before](/notes/week-02-charges-superposition/comp_super/). In these notes, you will read about how you can structure code to calculate the magnetic field from any shape of current-carrying wire.

## The Superposition Principle

[As we said before](/notes/week-10-magnetic-field-of-a-wire/b_current/), the principle of superposition states that the magnetic field at any given location in space is determined by vector sum of the magnetic field due to the current in each part of wire.

$$
{\overset{\rightarrow}{B}}_{net} = \sum{\overset{\rightarrow}{B}}_{i} = {\overset{\rightarrow}{B}}_{1} + {\overset{\rightarrow}{B}}_{2} + {\overset{\rightarrow}{B}}_{3} + \ldots
$$

where ${\overset{\rightarrow}{B}}_{1}$ would be the magnetic field from one piece of the wire, ${\overset{\rightarrow}{B}}_{2}$ would be the magnetic field from a second piece of the wire, and so on. This idea of adding together the magnetic field from each chunk of the wire will form the basis of what we want the computer to calculate for us.

## How can we use a computer for this?

For most real-world situations, the magnetic field integral cannot be solved analytically. That is, you could most likely write down the integral, but it cannot be computed because there's no anti-derivative for the function that you would be trying to integrate. So we have to think of another approach – one that makes use of the principle of superposition, which we know the magnetic field obeys.

Let's think through the process for computing the magnetic field due to the current in any kind of wire:

1.  Split the total length of the wire into small chunks of length (this is the equivalent of setting the $d\overset{\rightarrow}{l}$)
2.  Compute the magnetic field due to that chunk at the observation location
3.  Write down or otherwise keep track of that value
4.  Move to the another chunk of the wire
5.  Compute the magnetic field due to the new chunk at the observation location
6.  Add that new value to the old value from steps 3 and 4
7.  Repeat steps 5-7 for another chunk; and continue repeating until you've done this for all chunks of the wire

These somewhat monotonous steps will give us an approximate value for the magnetic field at the point of interest. **The smaller the chunks, the better the approximation.** You can probably see why setting up a computer to do this makes a lot of sense. Computers are really good at doing the same calculation over and over again!

So if we want to compute the magnetic field at a given location due to any length/shape of wire, the algorithm is just splitting the wire into chunks, computing the magnetic field of each chunk, and adding all the contributions together. This is a form of [numerical integration](https://en.wikipedia.org/wiki/Numerical_integration), which is a powerful technique in computational science. As a tool for thinking through these computational algorithms, we will sometimes write out the steps we want the computer to take in plain words rather than code - this is called **pseudocode**. The pseudocode for the magnetic field algorithm above is the following:

    Choose an observation location (or locations)
    Choose size of chunks
    Choose starting chunk
    Set net magnetic field to zero

    For all the chunks in the current-carrying wire:
       
       Determine vector distance between chunk and observation location
       Compute magnetic field due to that chunk
       Add contribution of chunk to net magnetic field

You can also use pseudocode (and may have already) to help you plan and understand the code you are writing.
