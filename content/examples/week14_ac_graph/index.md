---
title: 'Analyzing an Alternating Current Graph'
weight: 2
---

*[Return to Changing Flux from an Alternating Current notes](/notes/week-14-induction/ac/)*

Suppose you are given the following graph of current over time. You can see that the first peak is at the point where $t = 0.01\text{~s}$, and $I = 0.3\text{~A}$. The graph is shown below. Find the amplitude, period, and frequency of the current, and give an equation that describes the alternating current.

<img src="./media/rId10.png" style="width:4.16667in;height:2.91667in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

Graph of Alternating Current

### Facts

- The first peak in the graph is at $(t = 0.01\text{~s},I = 0.3\text{~A})$.

### Lacking

- Amplitude, period, frequency.
- Equation for alternating current.

### Approximations & Assumptions

- The graph of the current is a sine wave.
- As indicated on the graph, at $t = 0$, we have $I = 0$.
- The current is centered about $I = 0$, that is, the sine wave has not been shifted vertically at all.

### Representations

- We represent the graph as given in the example statement.

## Solution

Since the graph has not been shifted vertically, we can say that the peak we see is also the amplitude of the graph. So the amplitude of the alternating current is simply $0.3\text{~A}$.

The period of the graph is given by the time between peaks. One can see that the graph can be split into vertical slices as shown below.

<img src="./media/rId18.png" style="width:4.16667in;height:3.47917in" alt="[ALT TEXT NEEDED: figure-02.png -- describe this figure for screen readers]" />

Vertical Time Slices

It should be easy to see based on the visual above that the time between peaks is just four times the time value at the first peak. So then the period is $0.04\text{~s}$.

The frequency is just the reciprocal of the period:

$$
f = \frac{1}{\tau} = \frac{1}{0.04\text{~s}} = 25\text{~Hz}
$$

We are also now equipped to write a equation for the alternating current. We will use a sine function rather than a cosine function, since the current begins at $I = 0$, and increases. The amplitude will provide the factor out front:

$$
I = I_{0}\sin(2\pi \cdot f \cdot t) = (0.3\text{~A}) \cdot \sin(2\pi \cdot 25\text{~Hz} \cdot t)
$$
