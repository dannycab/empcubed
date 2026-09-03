---
title: 'Energy Stored in a Parallel Plate Capacitor'
weight: 9
---

*[Return to Capacitors in Circuit](/notes/week-08-capacitors-combinations/cap_in_cir/)*

Suppose you have a parallel plate capacitor with a capacitance of $16\text{~mF}$. You connect it to a 15-Volt battery and leave it to charge. After a while, you suddenly double the area of the plates and wait for another while. What is the energy stored in the capacitor? What would be the energy stored if you had disconnected the capacitor before doubling the area?

### Facts

- Originally, the capacitor has capacitance $C = 16\text{~mF}$.
- The battery has $\Delta V_{\text{battery}} = 15\text{~V}$.
- The capacitor is a parallel plate capacitor.
- The area of the plates is doubled.
- The capacitor is either connected always or disconnected before changing the area (two cases).

### Lacking

- For both situations in the problem statement, energy stored in the capacitor.

### Approximations & Assumptions

- Whenever we measure energy, the capacitor is charged and and there is no longer current in the circuit: As a capacitor charges energy gets stored in the capacitor and this happens over time. We are only looking at the fully charged capacitor in this case.
- There is negligible resistance in the circuit: The voltage across the capacitor is the same as in the battery with this assumption, as no energy is lost over the wires.
- In the case that we disconnect the capacitor, it does not discharge at all: In reality capacitors are not perfect and lose their charge in a multitude of ways, but we will assume that is not happening in this problem.

### Representations

- We represent the capacitance of a parallel plate capacitor as

$$
\begin{matrix}
C = \frac{\epsilon_{0}A}{d} & & & & & & (1)
\end{matrix}
$$

- We represent the capacitance of a capacitor in general as

$$
\begin{matrix}
C = \frac{Q}{\Delta V} & & & & & & (2)
\end{matrix}
$$

- We represent the energy stored in a capacitor as

$$
\begin{matrix}
U = \frac{1}{2}\frac{Q^{2}}{C} & & & & & & (3)
\end{matrix}
$$

## Solution

We assumed that in the capacitor, $\Delta V = \Delta V_{\text{battery}} = 15\text{~V}$, which is a good assumption if the capacitor has been connected to the battery for a long time. At this point we can find the energy stored in the capacitor before changing its area. All we need to do is rewrite the equation for the energy stored using the general equation for capacitance. We can rearrange equation (2) and sub in an expression for $Q$ into equation (3):

$$
U = \frac{1}{2}C\Delta V^{2}
$$

We have a capacitance and a potential difference which correspond to the charged capacitor before changing the area. The problem statement didn't ask for this quantity, but it will be useful for comparisons:

$$
U_{\text{original}} = 1.8\text{~J}
$$

In the first case, we simply double the area of the capacitor without changing anything else or disconnecting it. Equation (1) tells us that doubling the area will in turn double the capacitance of the capacitor to $32\text{~mF}$. The voltage across the battery does not change. When the area of the plates is suddenly doubled, charge on the plates spreads out and allows more charge to flow onto the plates (also making current pick up again in the wire). Eventually equilibrium is reached again, current stops flowing, and the voltage across the capacitor will be $15\text{~V}$, as before. Our calculation for the energy stored will also be the same, but with the new value for capacitance now:

$$
U_{\text{new, connected}} = \frac{1}{2}C_{\text{new}}\Delta V^{2} = 3.6\text{~J}
$$

In the second case, we disconnect the capacitor before doubling the area. Since the power source is no longer in play, it is a little more difficult to know the potential difference between the plates. However, if the battery is disconnected this also means that the charge on the plates will not change. It is worth expressing the energy stored in terms of $Q$ and $C_{\text{new}}$ (instead of C and V as before), for which equation (3) is set up perfectly. We refrain from subbing in numbers until the end, so until the last expression we write $C_{\text{new}} = 2C_{\text{original}}$

$$
U_{\text{new, disconnected}} = \frac{1}{2}\frac{Q^{2}}{C_{\text{new}}} = \frac{1}{2}\frac{Q^{2}}{2C_{\text{original}}} = \frac{1}{2}U_{\text{original}} = 0.9\text{~J}
$$

This is an interesting result! In one case, the energy doubles, and in the other case, it halves. And all we changed was whether we kept the circuit connected or not. If we think about each situation it can make sense intuitively. In the first case we have the same driving potential and larger plates, which would allow more charge to be put on the plates and allowing more energy to be stored in the capacitor. In the second case, we no longer have the same driving potential when we increase the area of the plates. This just means you will have the same charge distributed over a larger area. We would expect that to decrease the amount of energy in the capacitor.
