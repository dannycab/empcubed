---
title: 'Energy around the Circuit'
weight: 4
textbook_ref: 'Sections 18.3, 18.8-18.10, and 19.4 in Matter and Interactions (4th edition)'
---

One of the consequences of adding a resistor in the circuit (with higher electron speed and a higher electric field) is that a large **energy transfer** occurs across the resistor. In thin wire resistors (sometimes referred to as filaments), this effect is particularly visible. The amount of energy transferred to a filament is sufficient to heat the thin wire to the point where it produces heat and light. This is actually how [incandescent light bulbs](https://en.wikipedia.org/wiki/Incandescent_light_bulb) work.

{{< youtube c4tAtICY2Co >}}

Let's continue to look at the simple circuit that we were using in the video above (a mechanical battery, wires, and a thin filament). To analyze the energy in our circuit, we can refer back to [the Energy Principle](https://www.msuperl.org/wikis/pcubed/doku.php?id=184_notes:three_principles). If we take everything to be in our system, including the battery, wires, filament, and the surrounding air or materials, then we know that:

$$
\Delta E_{sys} = 0
$$

If we breakdown what is in our system, this means that

$$
\Delta E_{bat} + \Delta E_{wires} + \Delta E_{filament} + \Delta E_{surr} = 0
$$

From this statement of energy conservation, this would tell us that any energy provided by the battery must be used in the wires, heating up the filament, or providing light and heat to the surroundings.

## Energy per unit charge: Electric Potential

We could also consider what is happening to the energy of a single electron as it makes a complete trip around the circuit. The energy gained by the electron as it is transported across the mechanical battery is dissipated by the collisions the electron has as it moves around the wire, particularly with the positive nuclei in the wire. While this is certainly true, it becomes cumbersome to think about every single electron that is moving around the circuit. Instead, we will often think about energy in circuits in terms of the energy per charge that is moving around the circuit. [As we talked about before](/notes/week-03-electric-force-energy/pc_energy/#general_relationship_-_energy_and_potential), **electric potential *is* the energy per charge**, which is something that you have been working with over the last few weeks. So rather than talk about changes in energy around the circuit, we will generally be talking about changes in electric potential around the circuit.

This means we can rewrite our energy conservation statement in terms of the energy per charge instead. This is called ***The Loop Rule*** or sometimes Kirchhoff's Loop Rule. This Loop Rule says that if you follow a complete, round-trip path in a circuit, the total change in electric potential across all of the circuit elements (i.e., batteries, wires, resistors, capacitors) should be zero.

$$
\Delta V_{1} + \Delta V_{2} + \Delta V_{3} + ... = 0
$$

*We will refer back to the Loop Rule and the [Current Node Rule](/notes/week-06-resistors-combinations/current/) frequently in circuits as they are the way we talk about energy conservation and charge conservation in circuits.*

## Power in Circuits

Another way to talk about energy in circuits is to look at how much energy (aka, heat or light) is used up per second by a lightbulb or more generally by a resistor (in contrast to voltage which is energy per charge). When you are talking about the change in energy per change in time, this is called **power**:

$$
P = \frac{\Delta U}{\Delta t} = \frac{dU}{dt}
$$

Power is a scalar quantity that has **units of watts or joules per second** ($W = \frac{J}{s}$). For reference, a typical lightbulb in your house is a 60 W lightbulb. On the other hand, a large power plant that produces electricity for a city generally produces $1 - 5$ MW $= 1 - 5 \cdot 10^{6}$W. In circuits, it is fairly easy to calculate the power if you know the potential difference across a circuit element and the current that passes through that element. To get power, you multiply current times the potential difference since current has units of amps or coulombs per second, and electric potential has units of volts.

$$
\frac{C}{s}*V = \frac{J}{s}
$$

since a volt\*coulomb is a joule, we get units of energy per second, which is what we want. In other words,

$$
P = I\Delta V
$$

Note we are using conventional current here, not the electron current.

## Examples

- [Changing the Dimensions of a Wire](/examples/week7_wire_dimensions/)
  - Example Video: Changing the Dimensions of a Wire

{{< youtube uRIzyLqRtRU >}}
