---
title: 'Defining Current'
weight: 1
---

In the last few pages of notes, we have talked about how the surface charges are arranged to create a constant electric field in the wire. This electric field is responsible for pushing the electrons through the wire from one side of the battery to the other - creating a flow of electrons, which we called **electron current**. Building on this idea, these notes will go into how we mathematically define electron current and introduce what we call “conventional current.”

{{< youtube TS2cwuWNi3A >}}

## Electron Current

Before, we defined the electron current as the flow of electrons through the wire. We can make this more specific by defining electron current as the **number of electrons passing through a point per second**. Because the electron current is made up of negative charges, **the electron current will always flow opposite to the electric field**. (This is a more general rule that you may remember from before - electrons will always move opposite to the direction of the electric field.) We will use a lower-case “i” to represent the electron current:

$$
i = \frac{\# electrons}{second}
$$

Since it is very difficult to actually count the number of electrons that pass a location, we generally write the electron current in terms of the **electron density** in the wire ($n$), the cross-sectional area of the wire ($A$), and the average speed of the electrons through the wire ($v_{avg}$).

$$
i = nAv_{avg}
$$

Electron density ($n$) is a property of the material, which represents the number of electrons per volume of the wire that are free to move. For example, copper has a high electron density ($8.4 \cdot 10^{28}\frac{electrons}{m^{3}}$), which is part of what makes copper an ideal conductor. Electron density is typically a number that you can look up (online or in a table) for a given material. The cross-sectional area ($A$) depends on what kind of wire you have, but will typically be the area of a circle (in the case of a cylindrical wire). [The next page of notes](/notes/week-06-resistors-combinations/current/) will go into more details about how we find the average speed of the electrons ($v$) in the wire.

If we check the units of this equation we see that:

$$
\frac{\# electrons}{s} = \frac{\# electrons}{m^{3}}*m^{2}*\frac{m}{s}
$$

which is what we would expect for the electron current.

## Conventional Current

Conventional current is then defined as the amount of charge to pass a point per second (rather than the number of electrons). Because we already know the number of electrons passing a location, we can find the amount of charge per second simply by multiplying the electron current by the magnitude of the charge of a single electron. If the charge carriers aren't electrons (e.g., some kind of ion), then you will need to use the charge of the charge carrier. In the context of most circuits though, the electrons are almost always the charge that is moving. We will use an upper-case “$I$” to represent the conventional current and to distinguish it from the electron current.

$$
I = \frac{\# Coulombs}{second} = |q|i
$$

The conventional current is now positive (number of electrons times the magnitude of the charge). By “convention”, the conventional current flows in the opposite direction of the electron current. In other words, **the conventional current will flow in the *same* direction as the electric field.** The units of conventional current are $\frac{Coulombs}{second} = \frac{C}{s} = A$, which we call an **Ampere or an Amp** for short. It is this conventional current that we measure with ammeters and multimeters in the laboratory.

For historical reasons, much of what we work with in circuits is based off of conventional current rather than the electron current (much of what we know was established before we discovered it was the electrons that were free to move; you can thank [Ben Franklin](https://en.wikipedia.org/wiki/Benjamin_Franklin#Electricity) for that). However, remember that physically, the electrons are what move in a circuit.
