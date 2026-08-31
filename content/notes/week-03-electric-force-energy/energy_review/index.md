---
title: 'Review of Energy'
weight: 3
textbook_ref: 'Sections ??? of Matter and Interactions (4th edition)'
---

In addition to forces and accelerations, energy is an alternative tool we can use to understand how systems behave. We will spend a lot of time on energy, and the closely related idea of electric potential, in EMP-Cubed. This page contains brief reminders of the key ideas about energy from your mechanics course; for more details refer to the readings from Physics 183.

## What is Energy?

It's actually not easy to give a precise definition of energy that covers all of the situations in which it occurs. For our course, a reasonable way to think about it is that **energy is either motion, or the ability to produce motion**. (However, some forms of this motion, like random molecular motion associated with thermal energy produced by friction, may be difficult to see.)

There are two important types of energy we talk about: ***kinetic energy***, which is the energy associated with objects currently moving in a particular direction, and ***potential energy***, which is energy stored somehow in a system that could cause things to move in the future (like a compressed spring that could push a block and make it move). A third form of energy is *thermal energy*, which is associated with the random motion of atoms and molecules. Kinetic or potential energy can be turned into thermal energy, but thermal energy cannot easily be turned back into kinetic or potential energy.

A really nice feature of energy is that **energy is a scalar**, not a vector. Energy is just a number without any direction associated with it, which means there are no *x* and *y* components and no trigonometry to worry about.

Several symbols are commonly used to represent energy. $E$ is the most common symbol representing any kind of energy. If we want to remind ourselves that the energy is kinetic energy, we often use $K$, and $U$ is generally used to represent potential energy (sometimes with a subscript to specify what kind of potential energy, like $U_{g}$ for gravitational potential energy). Regardless of the type of energy, the SI unit of energy is the joule (J), which is equivalent to 1 kg m²/s². Using the definition of a newton, you can also write this as 1 J = 1 N m.

An alternative (non-SI) unit of energy that may be more convenient in this course is the electron-volt, eV, which has a value of 1 eV = $1.602 \times 10^{- 19}$ J.

## Why and When is Energy Useful?

Energy is important because **energy is a conserved quantity** – energy is never created or destroyed, it only changes form, for example from $K \rightarrow U$. This means that for any isolated system, if you compare two snapshots of the system at different times, the total amount of energy in the system has to be the same. Mathematically, we express this as

$$
E_{f} = E_{i},
$$

and then write down expressions that include all the types of energy that are present, such as $E_{f} = K_{f} + mgh_{f}$ for an object with kinetic and gravitational potential energy.

Often, this means that you can figure out the state of the system at some final $t_{f}$ based on what you know about some initial time $t_{i}$, without having to calculate anything about what happened in between: no tracking forces and accelerations, no worrying about vectors and trig components, and so on.

## Energy and Systems

The idea of a *system* is important for using energy correctly. When we set up a problem, we select the objects whose behavior we want to keep track of: these are our system. If all of the interactions/forces that the objects experience come from other objects in the system, then we say that this is an *isolated system*, and the total energy of the system cannot change: $E_{f} = E_{i}$.

But if the objects in our system experience forces or interactions coming from their surrounding environment – *external forces* – then the system isn't isolated and you need to keep track the energy flowing into or out of the system:

$$
E_{f} = E_{i} + \Delta E,
$$

where $\Delta E$ is the energy exchanged between the system and its environment. (Be careful of the sign! As written here, $\Delta E$ should be positive is energy is flowing in, and negative if energy is flowing out of the system.)

For example, if two blocks slide together and collide on a table, we might say that our system consists of the two blocks, and define the table to be outside the system, part of the environment. Then if we don't include any forces from the table in our model – maybe because it's an air table so that friction is negligible, or because we're only interested in comparing the moment just before the collision to the moment right afterward – we would say the blocks are isolated and their total energy is conserved: $E_{1,f} + E_{2,f} = E_{1,i} + E_{2,i}.$ But if we do include friction from the table in our model, then that friction is an external force that changes the energy of the system: $E_{1,f} + E_{2,f} = E_{1,i} + E_{2,i} - \Delta E_{fric}$.

It's a very good idea to make note of what you are defining as your system when setting up your model of the problem, such as with a circle on your free-body diagram or interaction diagram.

### External Forces and Work

If an external force acts on our system, **the energy it transfers in or out is the work** done by the force on an object in the system. The work is calculated as

$$
W = \Delta E = \int{\overset{\rightarrow}{F}}_{ext} \cdot d\overset{\rightarrow}{x},
$$

where $\Delta\overset{\rightarrow}{x}$ is the displacement the object experiences while the force acts on it. If the magnitude of the force is constant, this integral reduces to simply $W = \Delta E = {\overset{\rightarrow}{F}}_{ext} \cdot \Delta\overset{\rightarrow}{x}$.

A few things to note about this expression: if the object doesn't move, no work is done and so no energy is transferred to the system. Forces perpendicular to the object's velocity also do no work. (The force produces an acceleration changing the *direction* of the velocity, but the object's speed doesn't change.)

If the force is exactly parallel to the velocity, then work is just $W = F\,\Delta x$, but in general you need to take the dot product of the vectors and there is will a trig term: $W = F\,\Delta x\cos\theta$, where $\theta$ is the angle between the force and the velocity. If $\theta = 180^{\circ}$, meaning that the force is pushing in the direction opposite to the object's velocity, the dot product is negative because the force is reducing the object's energy (slowing it down).

## Forms of Energy

We say that energy is a **conserved quantity**, meaning that it is never created or destroyed (although it may flow in our out of your system). What energy can do is change form, such as from potential to kinetic energy, or vice versa. You've seen several forms of energy in your mechanics class, and we'll learn about some important new forms in EMP-Cubed.

### Kinetic Energy of Linear Motion

Kinetic energy, abbreviated $K$, is the energy of a macroscopic object in motion. (In a microscopic picture, it is the energy associated with particles moving in a single direction: coherent linear motion.) The kinetic energy of an object depends on its mass and its speed,

$$
K = \frac{1}{2}mv^{2}.
$$

Since the object's speed $v$ is squared in this formula, the kinetic energy is always a positive number.

### Rotational Kinetic Energy

Rotational energy, $K_{rot}$, is fundamentally the same kinetic energy as the $\frac{1}{2}mv^{2}$ of linear motion, but we usually calculate it separately since we usually measure rotation separately from linear velocity. If an object rotates with angular speed $\omega$, there is kinetic energy

$$
K_{rot} = \frac{1}{2}I\omega^{2}
$$

associated with the rotation, in addition to any kinetic energy related to its linear speed $v$.

In this formula, $I$ is a parameter called the object's *moment of inertia* around the rotation axis. In general,

$$
I = \sum_{i}^{}m_{i}r_{\bot,i},
$$

where the sum is over all of the separate pieces of mass in the object, and $r_{\bot}$ is the perpendicular distance of that piece of mass from the axis of rotation. For an object modeled as a collection of point masses, you can use this formula directly. Moments of inertia for many geometric shapes (spheres, rods, etc.) can be looked up online. As the formula suggests, moments of inertia add together: the moment of inertia of a ball on the end of a stick is the sum of the moments of the ball and the stick.

Remember that the moment of inertia depends on both the shape and mass of the object *and* the axis around which it rotates. A rectangular door, for example, has a different $I$ for rotation on its hinges than it would if it were rotating around its center. And it has a different moment for rotation along its long axis than its short axis.

### Potential Energy

Potential energy, generically denoted $U$, is the energy associated with forces between objects in our system. We call it “potential” energy because it may be used to set objects in motion, i.e., it can be transformed into kinetic energy. There is a fundamental equivalence between forces and potential energy, which we can write mathematically as

$$
F(x) = - \frac{dU}{dx}.
$$

This means that we can think of a force as the (negative) slope of a potential energy curve – saying that there is a potential energy that changes with position is the same thing as saying that a force exists.

The negative sign in this equation means that the force associated with a potential energy always pushes objects to lower $U$. If we think about $U$ as a curve or surface in space, objects always want to “roll down the hill”. This metaphor is quite literal for gravitational potential energy, but we can apply the same idea to any type of potential energy – this turns out to be a useful way to think about electric potential (energy), in particular.

### Gravitational potential energy

$U_{g}$ is the potential energy associated with the force of gravity. There are two expressions we use for $U_{g}$, depending on circumstances:

The most general expression is the Newtonian form,

$$
U_{g} = - \,\frac{G\, m_{1}\, m_{2}}{r}.
$$

This form depends on the masses $m_{1}$ and $m_{2}$ of the two interacting objects, the distance $r$ between them, and Newton's constant $G = 6.674 \times 10^{- 11}\mspace{6mu} N\mspace{6mu} m^{2}/{kg}^{2}$. This expression can always be used, but in practice we normally only use it when thinking about masses on orbital or planetary scales. Note that this expression is always negative, and goes to zero as $r$ becomes very large. This convention means that the gravitational potential energy is the *binding energy* holding the two objects together; i.e., the amount of energy that must be added to the system to let the objects escape from each other.

For masses close to the Earth's surface, we use a simpler approximation that combines the values of $G$, $m_{Earth}$ and $r_{Earth}$ into a single constant $g = 9.8\mspace{6mu} m/s^{2}$, leading to the expression

$$
U_{g} = mgy.
$$

When using this approximation, we often set $y = 0$ to the lowest position we're interested in, but that choice is completely arbitrary and negative values of $U_{g}$ are perfectly valid.

### Spring Potential Energy

A spring prefers to have a particular length, sometimes called its *relaxed* or *equilibrium* length. If a spring is stretched or compressed away from its relaxed length, then it exerts a restoring force pulling it back to equilibrium. The potential energy associated with this force is

$$
U_{sp} = \frac{1}{2}k(\Delta x)^{2},
$$

where $\Delta x$ is how far the spring is stretched or compressed relative to its equilibrium, and $k$ is a material property of the spring measured in N/m, called the **spring constant**. Graphically, $U_{sp}$ is a quadratic curve, like a bowl, with the equilibrium position at the bottom.

### Thermal Energy

Thermal energy, $E_{th},$ is a term we use as a macro-scale description of the energy of *random* motion of microscopic particles, including their linear motion, rotational motion, and the compression and extension of molecular bonds that act very much like springs. The difference between kinetic and thermal energy is that kinetic energy is associated with the *coherent motion* of particles moving in the same direction, while thermal energy is associated with random motion. This distinction matters because of entropy: coherent motion has very low entropy, and so kinetic energy $K$ can easily be transformed into potential energy $U$ or transferred to other objects. But random motion has very high entropy, so it's difficult to transform $E_{th}$ into $K$ or $U$: it never happens spontaneously, and the 2nd Law of Thermodynamics limits how much thermal energy can be transformed even with specially designed engines.

Forces such as friction which transform energy from $K$ (or $U$) into $E_{th}$ are called ***dissipative forces***, since that transformation is a one-way trip. The work done on the moving object by the frictional force is equal to the increase in thermal energy of the system, $W = F_{fr}\,\Delta x = \Delta E_{th}$. When thermal energy is generated or transferred between objects, we call the change $\Delta E_{th}$ the *heat* that is generated or transferred.

Although thermal energy is difficult to utilize, it can be measured through an object's temperature. Every object has a parameter called its *heat capacity,* $C$, which relates the heat flowing into or out of the object to the change in its temperature:

$$
\Delta E_{th} = C\,\Delta T.
$$

The heat capacity can be related to the object's properties, such as its mass and the specific heat of the material it's made of.

## Common Mistakes

\* **Setting one type of energy equal to another, such as** $K = U$. Energy conservation relates the total energy at one time to the total energy at some other time. If the initial energy and the final energy are each entirely one type you may get something like $K = U$, but that is a special case, not a universal principle. It's a good idea to always start by writing down $E_{f} = E_{i} + \Delta E$ to remind yourself of the correct structure.

\* **Sign errors.** If energy is transferred, it's flowing into one object but out of another. The magnitude of $\Delta E$ is the same for both objects, but one has a positive sign (gains energy) while the other is negative (loses energy), so it's easy to make a sign error. Always be sure the sign of a change in energy makes physical sense for the object you're looking at, don't assume equations will always be written with the right sign for your problem.

\* **Forgetting that** $U$ **can be negative.** There's no absolute scale for potential energy; only changes in potential energy matter, so you can set the zero of $U$ to be whatever reference point you want. (There are situations where a particular choice may be useful, though.) You may have a problem where an object has $E_{tot} = 0$ but has positive $K$ and negative $U$ at some point in time. This is perfectly valid but a but counter-intuitive, so it's easy to make sign errors or make bad assumptions, like “if $E = 0$, then $K$ must be zero too.”
