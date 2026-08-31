---
title: 'Resistance of a Wire'
weight: 53
---

*[Return to resistors and conductivity](/empcubed/notes/week-06-resistors-combinations/resistivity/)*

Suppose you have a wire whose resistance is 60 m$\Omega$. The wire has a length of 2 cm, and has a cross-sectional area of 1 mm$^{2}$. What would be the resistance if you increase the length of the wire to 6 cm (keeping the area the same)? What would be the resistance if you increase the cross-sectional area to 3 mm$^{2}$ (keeping the original length of wire)?

### Facts

- The original wire has $L = 2\text{~cm}$, $A = 1\text{~mm}^{2}$, and $R = 60\text{~m}\Omega$.
- The length could be increased to $L_{new} = 6\text{~cm}$.
- The cross-sectional area could be increased to $A_{new} = 3\text{~mm}^{2}$.

### Lacking

- Resistances of new wires.

### Approximations & Assumptions

- The conductivity of the wire does not change.
- The wire's material is uniform.

### Representations

- We represent the resistance of a simple wire with:

$$
R = \frac{L}{\sigma A}
$$

## Solution

All we need here is our representation for the resistance of the wire. In the first change to the wire, we triple it's length ($2\text{~cm} \rightarrow 6\text{~cm}$). Our new resistance then is found by

$$
R_{new} = \frac{L_{new}}{\sigma A} = \frac{3L}{\sigma A} = 3R = 180\text{~m}\Omega
$$

If instead, we made the other change, we would have tripled the cross-sectional area ($1\text{~mm}^{2} \rightarrow 3\text{~mm}^{2}$). Our new resistance would then be

$$
R_{new} = \frac{L}{\sigma A_{new}} = \frac{L}{\sigma 3A} = \frac{1}{3}R = 20\text{~m}\Omega
$$

These answers should make sense physically. The longer the wire, the more material there is for the electrons to push through, so the resistance is higher. The bigger the area, the more electrons are able to flow through the wire in at a given time so the resistance should be smaller.
