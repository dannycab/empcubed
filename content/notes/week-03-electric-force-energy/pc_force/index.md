---
title: 'Electric Force'
weight: 2
textbook_ref: 'Sections 3.7, 13.2 - 13.3 , and 13.6 of Matter and Interactions (4th edition)'
---

Last week, you have read about the [electric field](/notes/week-01-charges-field-potential/pc_efield/) and [electric potential](/notes/week-01-charges-field-potential/pc_potential/) that is created by a single point charge. Here you will read about what happens when you have two point charges that are near each other. [You have already read about the kind of interaction](/notes/week-01-charges-field-potential/charge/) you expect when you place two charges next to each other: either they are attracted to each other (charges have different signs) or repelled from each other (charges have the same sign). As you learned in your mechanics course, we can think about these kinds of pulls or pushes as a force acting on the charge(s). This force results from the interaction of a charge with the electric field produced by the other charge(s). We will call this new force the **electric force**.

In general, there are two ways to think about the electric force: either one charge interacts with another charge or one charge interacts with the electric field that is produced by another charge. We will usually favor thinking about how charges interact with the field (rather than how charges interact with other charges) because it is through that field that the interaction occurs. These notes will introduce the general relationship between electric force and electric field and discuss the example of a positive and negative point charges (which we will call an electric dipole).

{{< youtube 7KtC0dEjkMM >}}

## General Relationship

In general, the electric force on any charge (q) is equal to the charge times the net electric field (${\overset{\rightarrow}{E}}_{net}$) at the location of q. This is the most general way to write the electric force on a charge, which means **it is always true** - if you know what the electric field is at a location due to all the other charges (no matter what shape or type of charge produced that electric field), you can easily determine the electric force on a charge would be at that location.

$$
{\overset{\rightarrow}{F}}_{net \rightarrow q} = q*{\overset{\rightarrow}{E}}_{net}
$$

Where we are using the notation of $net \rightarrow q$ to show that this is the force *from* the net electric field *on* the charge q. Since electric field is a vector and charge is a scalar, when they are multiplied together, the result is a vector (electric force). This vector points in the same direction as the electric field for positive charges and in the opposite direction of the electric field in the case of negative charges. **Note that this is the electric force from the *external electric field* on the *charge***. A charge's own electric field cannot affect the charge itself (for the same reason that you can't lift a board while standing on it and fly). **Also note that electric force is not the same thing as electric field**, but they are related. The electric field is the *electric force per unit charge* at a given location; in a sense, it tells you how large (magnitude) and which way (direction) the force could be. *Note there is some ambiguity about the direction of the force as it would matter which kind of charge is placed in the field.*

The electric force works in the same way as any other force that you learned about in Mechanics:

- **The electric force has units of newtons (N).**
- The electric force can be combined with any other forces acting on an object to find the [net force](/pcubed/notes/week-02-modeling-motion-net-force/momentum_principle/#net_force) on that object.
- The electric force can contribute to a [change in the object's momentum](/pcubed/notes/week-02-modeling-motion-net-force/momentum_principle/) (in other words the electric force can accelerate a charge).
- You can still use [free-body diagrams](/pcubed/notes/week-04-05-springs-contact-interactions/freebodydiagrams/) (or force diagrams) to determine the net force on an object. The electric force would simply be one of the arrows in the diagram.
- [Newton's third law](https://en.wikipedia.org/wiki/Newton's_laws_of_motion#Newton.27s_3rd_Law) still applies - The electric force from one charge on a second charge is equal and opposite to the electric force from the second charge on the first.

## The electric force is a conservative force

In addition to the general results above, the electric force is also a [\*\*conservative force\*\*](https://en.wikipedia.org/wiki/Conservative_force). A conservative force is a force:

1.  for which we can define a potential energy and
2.  for which changes in that potential energy are path-independent (only the initial and final states matter - not how you went from the initial to final state).

Two examples of conservative forces from mechanics include: the gravitational force and the spring force. It doesn't matter how you go from $y = 3m$ to $y = 5m$, the change in gravitational energy ([which is defined as PE=mgh](/pcubed/notes/week-07-energy-transfer/grav_and_spring_pe/)) is the same. This is in contrast to **non-conservative force**, which result in changes to the system energy that depend on the path the system takes. You cannot define a potential energy for non-conservative forces. Examples of non-conservative forces that you may know from mechanics are: the friction force and air drag. In these cases we cannot define what the “energy of friction” would be, in part because it depends on what path you take (e.g., the thermal energy change due to friction on a squiggly path between two points would be much higher than on a straight path between those same points).

## Two Point Charges

<img src="./media/rId24.png" style="width:2.08333in;height:0.30208in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

Negative and positive point charges, with the separation vector from the negative charge to the positive charge.

As an example of electric force, we will talk about an electric dipole - two charges (one positive and one negative) located a small distance apart. For an electric dipole, we can find the electric force from the negative charge on the positive charge and vice versa. Starting with the electric force on the positive charge, we can write the general relationship:

$$
{\overset{\rightarrow}{F}}_{net \rightarrow q} = q{\overset{\rightarrow}{E}}_{net}
$$

where $q$ here is the positive charge and ${\overset{\rightarrow}{F}}_{q}$ is then the force on the positive charge. In this case, ${\overset{\rightarrow}{E}}_{net}$ is the net electric field at the location of $q_{+}$. Since the negative charge $q_{-}$ is the only other charge around $q_{+}$, the net electric field at $q_{+}$ is equal to the electric field from the negative charge ${\overset{\rightarrow}{E}}_{net} = {\overset{\rightarrow}{E}}_{q -}$.

$$
{\overset{\rightarrow}{F}}_{q - \rightarrow + q} = q_{+}{\overset{\rightarrow}{E}}_{q -}
$$

When we make the *point charge assumption*, [we know from last week](/notes/week-01-charges-field-potential/pc_efield/) that electric field for a negative point is given by:

$$
E_{q -} = \frac{1}{4\pi\epsilon_{0}}\frac{q_{-}}{r^{3}}{\overset{\rightarrow}{r}}_{- \rightarrow +}
$$

where ${\overset{\rightarrow}{r}}_{- \rightarrow +}$ points from the charge producing the field ($q_{-}$ in this case) to the location of interest (where $q_{+}$ is). If we plug this electric field into our equation for the force on the positive charge, we get:

$$
{\overset{\rightarrow}{F}}_{q - \rightarrow + q} = q_{+}{\overset{\rightarrow}{E}}_{q -} = q_{+}\frac{1}{4\pi\epsilon_{0}}\frac{q_{-}}{r^{3}}{\overset{\rightarrow}{r}}_{- \rightarrow +} = \frac{1}{4\pi\epsilon_{0}}\frac{q_{+}q_{-}}{r^{3}}{\overset{\rightarrow}{r}}_{- \rightarrow +}
$$

By following the same process, we can find the electric force on the negative charge to be:

$$
{\overset{\rightarrow}{F}}_{q + \rightarrow q -} = q_{-}{\overset{\rightarrow}{E}}_{q +} = q_{-}\frac{1}{4\pi\epsilon_{0}}\frac{q_{+}}{r^{3}}{\overset{\rightarrow}{r}}_{+ \rightarrow -} = \frac{1}{4\pi\epsilon_{0}}\frac{q_{-}q_{+}}{r^{3}}{\overset{\rightarrow}{r}}_{+ \rightarrow -}
$$

The only thing that is different between the ${\overset{\rightarrow}{F}}_{+ q}$ and ${\overset{\rightarrow}{F}}_{- q}$ is the direction that the $\overset{\rightarrow}{r}$ points. (Here ${\overset{\rightarrow}{F}}_{+ q}$=-${\overset{\rightarrow}{F}}_{- q}$ and they are describing the same electric interaction so these forces are a [Newton's third law](https://en.wikipedia.org/wiki/Newton's_laws_of_motion#Newton.27s_3rd_Law) pair.)

The general equation for the force between two point charges is then:

$$
{\overset{\rightarrow}{F}}_{1 \rightarrow 2} = \frac{1}{4\pi\epsilon_{0}}\frac{q_{1}q_{2}}{(r_{1 \rightarrow 2})^{3}}{\overset{\rightarrow}{r}}_{1 \rightarrow 2} = \frac{1}{4\pi\epsilon_{0}}\frac{q_{1}q_{2}}{(r_{1 \rightarrow 2})^{2}}{\widehat{r}}_{1 \rightarrow 2}
$$

Where here we have used the [definition of the unit vector](/notes/week-01-charges-field-potential/math_review/#unit_vectors) ($\widehat{r} = \frac{\overset{\rightarrow}{r}}{r}$) to get the two different versions of the equation. There are a few things to notice about this equation. First, this equation is **only true for the electric force between two point charges**. Second, this force is **not a constant force** - it depends on the separation distance between the two charges. **The closer the two charges are, the stronger the push/pull will be.** Finally, this equation may look familiar from mechanics - if you change the charges into masses and change the constant, you will get the equation for [Newtonian gravity](/pcubed/notes/week-03-newtonian-gravitation/gravitation/) that describes the gravitational interaction between two large masses. It turns out that there are many parallels between the gravitational force and the electric force.

## Examples

[Ballon Stuck to a Wall](/examples/week3_balloon_wall/)
