---
title: 'Moving Charges Make Magnetic Fields'
weight: 2
textbook_ref: 'Section 17.3 in Matter and Interactions (4th edition)'
---

Just like we did with electric fields, we will start with magnetic fields by looking at the simplest source: a single moving point charge. When we are talking about this moving charge and the corresponding magnetic field, there are intuitive qualities that we want to make sure our mathematical model includes: (1) the farther away the observation point is from the moving charge, the smaller that we expect the magnetic field to be; (2) the larger the amount of charge, the larger we expect the magnetic field to be; and (3) the faster the charge is moving, the larger we expect the magnetic field to be. The final piece that is perhaps not so intuitive is that the direction of the magnetic field is actually perpendicular to observation point and to the velocity vector. However, each of these demands is consistent with experimental observations of moving charges. These notes will detail the mathematical equation that we use for the magnetic field (only for a single moving point charge) and explain a new tool called the [Right Hand Rule](/notes/week-09-magnetic-field-moving-point-charge/rhr/) that we can use to find the direction.

{{< youtube A4Nfu5r0eyU >}}

## Mathematical Model for Magnetic Field

We have already stated that the magnetic field is a vector field, meaning it has both *magnitude* and *direction*. As you will read soon, the magnetic field can also be related to the magnetic force. Again, we will start by making the *point particle assumption - meaning that we will take our charged object and crush it down to single small point that has some mass and charge*. Only this time, *we will be considering the case where the point charge is moving with a **constant** velocity*, rather than being fixed in one place.

## Magnetic Field Equation for a Moving Point Charge

The general equation for the magnetic field ($\overset{\rightarrow}{B}$), with units of Tesla ($T$), at some Point $P$ due to a moving charge is given by:

$$
\overset{\rightarrow}{B} = \frac{\mu_{0}}{4\pi}\frac{q\overset{\rightarrow}{v} \times \widehat{r}}{r^{2}}
$$

which you may hear referred to as the [Biot-Savart Law](https://en.wikipedia.org/wiki/Biot%E2%80%93Savart_law) in other resources or textbooks. This equation has several pieces to it:

- **Constant** - the first part of this equation $\frac{\mu_{0}}{4\pi}$ is a constant value, where $\mu_{0} = 4\pi*10^{- 7}$ $\frac{T \cdot m \cdot s}{C}$. The $\mu_{0}$ constant (also called the [permeability of free space](https://en.wikipedia.org/wiki/Vacuum_permeability)) plays a similar role
