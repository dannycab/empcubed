---
title: 'Magnetic Field near a Moving Charge'
weight: 47
---

*[Return to Moving Charges make Magnetic Fields notes](/notes/week-09-magnetic-field-moving-point-charge/moving_q/)*

You are a collector of magnetic field detectors. A fellow detector collector is trying to trim down her collection, and so it's your job to see if an old detector is still working properly, in which case it's yours! Today, you are a magnetic field detector collector, inspector, and hopefully a selector. First, you run a test in which a charged particle ($q = 15\text{~nC}$) is sent through the detector, and you look at the detector's readings to see if the detector seems to be working properly. The particle is travelling at $2\text{~m/s}$ and you need to predict the magnetic field's magnitude and direction at the points shown below. Be careful! – You'll be using vectors.

<img src="./media/rId10.png" style="width:4.16667in;height:1.85417in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

Detector Setup

### Facts

- $\overset{\rightarrow}{v} = 2\text{~m/s~}\widehat{x}$​
- The locations of interest are indicated above (Locations 1, 2, and 3), if the particle is at the origin.
- ${\overset{\rightarrow}{r}}_{1} = - 0.5\text{~m~}\widehat{x}$ (vector pointing from q to Location 1)
- ${\overset{\rightarrow}{r}}_{2} = 0.5\text{~m~}\widehat{y}$ (vector pointing from q to Location 2)
- ${\overset{\rightarrow}{r}}_{3} = - 0.5\text{~m~}\widehat{x} + 0.5\text{~m~}\widehat{y}$ (vector pointing from q to Location 3)
- $q = 15\text{~nC}$​

### Lacking

- ${\overset{\rightarrow}{B}}_{1}$, ${\overset{\rightarrow}{B}}_{2}$, ${\overset{\rightarrow}{B}}_{3}$

### Approximations & Assumptions

- We are only interested in the $B$-field at this specific moment in time: As the particle moves some its parameters may change (i.e. velocity, charge…). This assumption gives use fixed variables to work with at this snapshot in time, simplifying down the complexity of the model.

### Representations

- We represent the Biot-Savart Law for magnetic field from a moving point charge as

$$
\overset{\rightarrow}{B} = \frac{\mu_{0}}{4\pi}\frac{q\overset{\rightarrow}{v} \times \overset{\rightarrow}{r}}{r^{3}}
$$

### Approximation

We must approximate the particle as a point particle in order to use the magnetic field equation above. Since the problem doesn't say anything otherwise and it is a necessary approximation to solve the problem, this is an approximation we will make.

- We represent the situation with diagram given above.

## Solution

We begin by cracking open the Biot-Savart Law. In order to find magnetic field, we will need to take a cross product $\overset{\rightarrow}{v} \times \overset{\rightarrow}{r}$. Notice that $\overset{\rightarrow}{r}$ indicates a separation vector, directed from source (point particle) to observation (location 1, 2, or 3). Since our source is at the origin of our axes, then the separation vectors are actually just ${\overset{\rightarrow}{r}}_{sep} = {\overset{\rightarrow}{r}}_{obs} - 0 = {\overset{\rightarrow}{r}}_{obs}$, which are just the r-vectors listed in our “Facts”. Below, we have calculated the cross product for each of our three locations:

Note that for the first cross-product, Location 1 is situated perfectly in line with the straight-line path of the particle. This means that the ${\overset{\rightarrow}{r}}_{1}$ points in the same direction as $\overset{\rightarrow}{v}$ (so the angle between them is 0 degrees). When we take the cross product, then:

$$
\overset{\rightarrow}{v} \times {\overset{\rightarrow}{r}}_{1} = |\overset{\rightarrow}{v}||{\overset{\rightarrow}{r}}_{1}|sin(0) = 0
$$

This means there is no magnetic field at Location 1 at all!

For Location 2, the ${\overset{\rightarrow}{r}}_{2}$ is perpendicular to the velocity vector $\overset{\rightarrow}{v}$ (the angle between them is 90 degrees). When we take this cross product, then:

$$
\overset{\rightarrow}{v} \times {\overset{\rightarrow}{r}}_{2} = |\overset{\rightarrow}{v}||{\overset{\rightarrow}{r}}_{2}|sin(90) = 2*0.5*1 = 1\text{~m}^{2}\text{s}^{- 1}\ \widehat{z}
$$

Note that the $\widehat{z}$ comes from using the right hand rule (or rather from taking the cross product of a vector in the $\widehat{x}$ and a vector in the $\widehat{y}$). If you point your fingers in the direction of the velocity and curl them toward location 2 your thumb would point out of the page (or in the $+ \widehat{x}$ direction).

Finally, for Location 3, we can think about ${\overset{\rightarrow}{r}}_{3}$ in terms of it's components - the part that is parallel to the velocity (which would be the same as ${\overset{\rightarrow}{r}}_{1}$) and the part that is perpendicular to the velocity (which would be the same as ${\overset{\rightarrow}{r}}_{2}$). We just learned if the vectors are parallel, the cross product will give zero - so the horizontal component of ${\overset{\rightarrow}{r}}_{3}$ will not contribute to the magnetic field at Location 3. The only part that will contribute will be the vertical component (which is the same as what we just calculated for magnetic field at Location 2). So, we know already that this cross product will give:

$$
\overset{\rightarrow}{v} \times {\overset{\rightarrow}{r}}_{3} = 1\text{~m}^{2}\text{s}^{- 1}\widehat{z}
$$

Next, we find the magnitudes of $r^{3}$, since that is another quantity we need to know in the Biot-Savart Law. Note that even though the cross products were the same for Locations 2 and 3, the separation distances are not! Location 3 is still further away from q when compared to Location 2.

$$
\begin{matrix}
{r_{2}}^{3} & = 0.125\text{~m}^{3} \\
{r_{3}}^{3} & = 0.354\text{~m}^{3}
\end{matrix}
$$

We don't including location 1 above since we already know the magnetic field is 0 at that location! Below, we give the magnetic field at all three locations by plugging what we found in the Biot-Savart equation from the Representations list above.

$$
\begin{matrix}
{\overset{\rightarrow}{B}}_{1} & = \frac{\mu_{0}}{4\pi}\frac{q\overset{\rightarrow}{v} \times {\overset{\rightarrow}{r}}_{1}}{{r_{1}}^{3}} = 0 \\
{\overset{\rightarrow}{B}}_{2} & = \frac{\mu_{0}}{4\pi}\frac{q\overset{\rightarrow}{v} \times {\overset{\rightarrow}{r}}_{2}}{{r_{2}}^{3}} = 12\text{~nT~}\widehat{z} \\
{\overset{\rightarrow}{B}}_{3} & = \frac{\mu_{0}}{4\pi}\frac{q\overset{\rightarrow}{v} \times {\overset{\rightarrow}{r}}_{3}}{{r_{3}}^{3}} = 4.2\text{~nT~}\widehat{z}
\end{matrix}
$$

Observation location 3 is the furthest away from our moving point charge and we would expect it to have a smaller magnetic field than location 2, this is reflected in our solution. We also expected the magnetic field at location 1 to be 0 since the velocity and separation vector are parallel for this point (this is always a good thing to look for when approaching a problem with cross products).
