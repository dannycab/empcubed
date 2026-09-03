---
title: 'Example: Electric Potential from a Negatively Charged Balloon'
weight: 21
---

*[Return to Electric Potential](/notes/week-01-charges-field-potential/pc_potential/)*

Suppose we have a negatively charged balloon with total charge $Q = - 5.0 \cdot 10^{- 9}\text{~C}$. What is the electric potential (also called voltage) at a point $P$, which is a distance $R = 20\text{~m}$ from the center of the balloon?

### Facts

- The balloon has total charge $Q = - 5.0 \cdot 10^{- 9}\text{~C}$.
- The point $P$ is a distance $R = 20\text{~m}$ away from the center of the balloon.
- The electric potential due to a point charge can be written as

$$
V = \frac{1}{4\pi\epsilon_{0}}\frac{q}{r},
$$

- where $q$ represents the charge and $r$ is the distance.

### Representations

### Assumption

We assume $P$ lies outside of the balloon. This is obvious, as $P$ is a distance $R = 20\text{~m}$ away from the center of the balloon.

<img src="./media/rId13.png" style="width:1.5625in;height:1.41667in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

Charged Balloon, and Point P

### Goal

- Find the electric potential at $P$.

## Solution

### Approximation

We approximate the balloon as a point charge. We do this because we have the tools to find the electric potential from a point charge. This seems like a reasonable approximation because the balloon is not too spread out, and we are interested in a point very far from the balloon, so the balloon would “look” like a point charge from the perspective of an observation location that is $20\text{~m}$ away.

### Assumption

The electric potential infinitely far away from the balloon is $0\text{~V}$. Read [here](/notes/week-02-charges-superposition/superposition/#superposition_of_electric_potential) for why this is important.

The electric potential at $P$ is given by

$$
\begin{matrix}
V & = \frac{1}{4\pi\epsilon_{0}}\frac{q}{r} \\
 & = \frac{1}{4\pi \cdot 8.85 \cdot 10^{- 12}\frac{\text{C}}{\text{Vm}}}\frac{- 5.0 \cdot 10^{- 9}\text{~C}}{20\text{~m}} \\
 & = - 2.2\text{~V}
\end{matrix}
$$

Notice how the magnitude of charge on the balloon is the same as in the “positively charged balloon” [example](/examples/week2_electric_potential_positive_point/). The reason the magnitude of the voltage is so much smaller, is because the distance is so much greater. [The closer you get to a point charge, the higher the magnitude of electric potential](/notes/week-01-charges-field-potential/pc_potential/#potential_vs_distance_graphs).
