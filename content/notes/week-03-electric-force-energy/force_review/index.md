---
title: 'Review of Forces'
weight: 1
textbook_ref: 'Sections ??? of Matter and Interactions (4th edition)'
---

One of the core ideas from your mechanics course is that objects accelerate in response to forces. We will apply the same ideas in this course to understand electricity and magnetism, so it's important that you remember how forces work. This page is a brief review of the key ideas about forces from mechanics. If your recollection of any of these concepts isn't clear, you may want to go back and review the details in the readings from Physics 183.

## What is a Force?

A force is anything that pushes or pulls on an object. Since we push an object in a specific direction, a force has a direction associated with it: **force is a vector** quantity, $\overset{\rightarrow}{F}$, with three separate components $F_{x}$, $F_{y}$, and $F_{z}$. If you are adding forces together, you need to add the components separately. If we are only talking about the magnitude of the force, irrespective of its direction, we leave off the little vector arrow and just write $F$ (like we did for the three individual components).

The SI unit of force is the newton (N), which is defined as the force needed to accelerate a mass of 1 kg at a rate of 1 m/s². In other words, 1 N = 1 kg m / s².

## Net Force and Acceleration

The effect of a force is to cause an object to accelerate, that is, to *change* its velocity. An object can have a velocity even when no forces are acting on it, and conversely an object may remain at rest with zero velocity even when forces are acting on it (this is Newton's First Law).

In general, an object may be acted on by several forces at the same time, but it can only accelerate at one rate in one direction. The acceleration of an object depends on the (vector) sum of the forces acting on it, which we call the net force:

$$
{\overset{\rightarrow}{F}}_{net} = m\overset{\rightarrow}{a}.
$$

This equation is called Newton's Second Law.

To add multiple forces together to calculate the net force, you need to first break each force into its separate $x$, $y$, and $z$ components. (This usually requires a bit of trigonometry.) Then you add the components together separately.

For example, if you have two forces ${\overset{\rightarrow}{F}}_{1}$ and ${\overset{\rightarrow}{F}}_{2}$, then the net force is

$$
{\overset{\rightarrow}{F}}_{net} = {\overset{\rightarrow}{F}}_{1} + {\overset{\rightarrow}{F}}_{2}.
$$

This vector equation is really three separate equations:

$$
F_{net,x} = F_{1,x} + F_{2,x}F_{net,y} = F_{1,y} + F_{2,y}F_{net,z} = F_{1,z} + F_{2,z}.
$$

You *cannot* just add the total magnitudes of $F_{1}$ and $F_{2}$ together to get the magnitude of $F_{net}$.

Acceleration is a vector with three components $a_{x}$, $a_{y}$, and $a_{z}$, just like force. So Newton's Second Law is also really a set of three equations:

$$
F_{net,x} = ma_{x}F_{net,y} = ma_{y}F_{net,z} = ma_{z}.
$$

You can calculate the magnitude of the net force or acceleration vector from the individual components using the Pythagorean Theorem:

$$
a = \sqrt{a_{x}^{2} + a_{y}^{2} + a_{z}^{2}},
$$

and similarly for $F_{net}$.

## Interactions, External Forces, and Systems

Forces are the means by which objects interact with each other. There are two sides to every interaction, which means that every force is part of a pair, sometimes called an interaction pair or an action-reaction pair. In other words, if object A exerts a force on object B, then object B is also exerting a force on object A.

Newton's Third Law tells us that the magnitude of the force experienced by each object is the same – it's a single interaction, and the two forces on the two different objects are just two sides of the same coin. But the directions of the two forces are opposite: if I push you forward, then the rebound force pushes me backward. Mathematically, we represent this as

$$
{\overset{\rightarrow}{F}}_{\text{A on B}} = - {\overset{\rightarrow}{F}}_{\text{B on A}}.
$$

Although every force *has* an interaction partner, we don't always *care* about the partner force. If both of the interacting objects are part of our system, such as two small charged particles exerting electric forces on each other, then we generally need to keep track of both sides of the interaction and we will write down two forces. We sometimes say that these forces are internal to our system.

But if an object in our system interacts with something outside of our system, we usually don't keep track of the reaction force. For example, if I drop a ball, I say that the ball experiences a gravitational force from the Earth. But I usually ignore the gravitational pull that my ball exerts on the Earth (even though it is just as big as the force on my ball!), because I'm thinking of the Earth as part of the external environment rather than part of my system, and I'm not trying to track the Earth's motion. In this case, we say that the Earth's gravitational pull is an external force and not part of an interaction pair.

## Types of Forces

Several types of forces were introduced in your mechanics course. We will be introducing several more forces in EMP-Cubed.

### Gravity

*Near the Earth's surface*, every object experiences a force with magnitude

$$
F_{g} = mg,
$$

pulling downward (toward the center of the Earth). In this equation, $m$ is the object's mass and $g$ = 9.8 m/s² is the gravitational acceleration, which is the same for every object. This formula is an approximation which is usually good enough for dealing with objects at ground level or low altitude (planes, balloons, etc).

A more general formula for the magnitude of the gravitational force is

$$
F_{g} = \frac{GMm}{r^{2}},
$$

where $G = 6.674 \times 10^{- 11}\mspace{6mu} m^{3}/\text{kg s}^{2}$ is called Newton's constant, $M$ and $m$ are the masses of the two objects interacting, and $r$ is the distance between them. The force always pulls the two objects directly toward each other.

### Spring force

Any object attached to a spring has an equilibrium position where it experiences zero net force. *Most springs obey Hooke's “Law”*: if the object is moved away from its equilibrium position by a distance $\Delta x$, it experiences a force

$$
F_{sp} = - k\Delta x
$$

pushing it back toward the equilibrium position. Here $k$ is the spring constant of that particular spring, which has units N/m, and the minus sign indicates that the force is in the opposite direction of the object's displacement. That is, if the object is in front of its equilibrium position, the spring forces pulls backward, and vice versa.

### Normal force

If an object rests on a surface, the surface exerts a force on it which prevents it from sinking into the surface. This is called the “normal” force because the direction of the force is always perpendicular (i.e., normal) to the plane of the surface. The surface never actually pushes the object away, so it only exerts as much force as it needs to keep the object from penetrating the surface. This means there's no general formula for the magnitude of the normal force, it can only be calculated based on the other forces acting on the object. The **weight** of the object is the interaction-pair Newton's 3rd Law partner force to the normal force.

### Friction

If two surfaces try to slide across each other, they experience a frictional force. This is not a fundamental force like gravity, but a model representing the effects of surface roughness, van der Waals interactions, and other complicated things happening at the molecular level. *We usually model friction as having two different modes: static friction and kinetic friction.* In both cases, the frictional forces depend on characteristics of the surfaces, which we model with *coefficients of friction*, and also on the normal force acting between the objects whose surfaces are in contact.

**Static friction** occurs when two surfaces are in contact and some other (external) force is trying to make them slide along each other, but they are *not* actually moving. Static friction will prevent the surfaces from moving past each other, as long as it can, so it will provide a force with exactly the same magnitude as the external force, but acting in the opposite direction in order to keep the object stationary. This means there is no general formula for the magnitude of the static frictional force, and it can only be calculated based on the other forces acting on the object. But there is a *maximum* force that static friction can supply before the surfaces start sliding, which is given by

$$
F_{s,max} = \mu_{s}N,
$$

where $\mu_{s}$ is a pure number (no units) called the coefficient of static friction, and $N$ is the normal force between the surfaces.

**Kinetic friction**, sometimes called dynamic friction or sliding friction, takes over once the surfaces start to slide past each other. Unlike static friction, the magnitude of the kinetic frictional force can always be calculated with a formula:

$$
F_{k} = \mu_{k}N,
$$

where $\mu_{k}$ is the coefficient of kinetic friction (a pure number without units), and $N$ is the normal force between the two surfaces. The kinetic frictional force always acts in the direction opposite the current motion of the objects.

## Common Mistakes

- **Not bothering draw a free-body diagram** to keep track of the different forces, which object they act on, and which direction they push. This is a great way to get confused, and often leads to the next error:
- **Adding the magnitudes of forces together**, as if they were plain numbers instead of vectors. This gives you the correct result *only* if the forces point in the same direction. Usually, you need to add forces together component by component.
- **Assuming the force on an object has a constant magnitude**. Sometimes forces *are* constant, like gravity near the Earth's surface, and in those situations you can use tools like the kinematic equations ($x_{f} = \frac{1}{2}a(\Delta t)^{2} + v_{0}(\Delta t) + x_{0}$ and so on). But more often the magnitude or direction of a force changes during a problem, like with springs, and then you *can't* use these equations. You also can't solve an equation for a force at one point in time and assume it will have the same magnitude at a later time.
