---
title: 'Example: Changing the Dimensions of a Wire'
weight: 15
---

*[Return to Energy in Circuits](/empcubed/notes/week-06-resistors-combinations/r_energy/)*

Suppose you have a simple circuit whose wire changes in thickness. The wire is 8 meters long. The first 2 meters of the wire are 3 mm thick. The next 2 meters are 1 mm thick. The last 4 meters are 3 mm thick. The wire is connected to a 12-Volt battery and current is allowed to flow. You use an ammeter and a voltmeter to find that the current through the first 2 meters of wire is $I_{1} = 5\text{~A}$, and the voltage across the first two meters is $\Delta V_{1} = 1\text{~V}$. In all three segments of the wire, determine the magnitude of the electric field inside and the power transmitted.

### Facts

- Segment lengths: $L_{1} = 2\text{~m}$, $L_{2} = 2\text{~m}$, and $L_{3} = 4\text{~m}$.
- Segment diameters: $d_{1} = 3\text{~mm}$, $d_{2} = 1\text{~mm}$, and $d_{3} = 3\text{~mm}$.
- Current: $I_{1} = 5\text{~A}$.
- Voltage: $\Delta V_{1} = 1\text{~V}$, $\Delta V_{battery} = 12\text{~V}$.

### Lacking

- Power and electric field in all segments

### Approximations & Assumptions

- The circuit is in a steady state: This allows the current should be the same in all three sections.
- Approximating the battery as a mechanical battery: Batteries normally dont keep their energy forever and slowly die over time. Using a mechanical battery means our battery produces a steady source of energy in this problem.
- No outside influence on the circuit: This simplifies the model and isolates our circuit from any outside sources of charge or energy that could effect our calculations.

### Representations

- We represent the situation with diagram below. We number the segments for simplicity of representing the quantities we are interested in (see above in “Facts”).

Circuit Diagram

## Solution

Let's start with segment 1. The electric field is constant since the wire is uniform with respect to the rest of the segment, so we get

$$
E_{1} = \frac{\Delta V_{1}}{L_{1}} = 0.5\text{~V/m}
$$

The power dissipated through the segment is just

$$
P_{1} = I_{1}\Delta V_{1} = 5\text{~W}
$$

Now, for segment 2. We can use [what we know](/empcubed/notes/week-06-resistors-combinations/r_energy/#conservation_of_charge_in_circuits) about charge in steady state circuits to determine the electric field (notice we divide diameter by 2 in order to get the radius of the circular cross-section):

$$
E_{2} = \frac{A_{1}}{A_{2}}E_{1} = \frac{\pi(d_{1}/2)^{2}}{\pi(d_{2}/2)^{2}}E_{1} = 9E_{1} = 4.5\text{~V/m}
$$

### Assumptions

In order to do this calculation there are two important assumptions that must be made

- The wires have a circular cross section: This allows us to use the formula for the area of a circle to come up with the correct proportion.
- The wires are made of the same material throughout: There are two terms in the electron current equation that are material propeties and these will cancel out for each segment of wire if they are made of the same material. This allows the electric field to only vary with cross sectional area.

A simple application of the [Current Node Rule](/empcubed/notes/week-06-resistors-combinations/current/#current_in_different_parts_of_the_wire) tells us that $I_{2} = I_{1}$. The voltage is easily found from the constant electric field: $\Delta V_{2} = E_{2}L_{2} = 9\text{~V}$. The power dissipated through the segment is then

$$
P_{2} = I_{2}\Delta V_{2} = 45\text{~W}
$$

For segment 3, we can reason based on the thicknesses of the segments that $E_{3} = E_{1}$. This yields

$$
E_{3} = 0.5\text{~V/m}
$$

We can use the same reasoning as before to say that $I_{3} = I_{2} = I_{1}$. We can also use the same equation to find voltage: $\Delta V_{3} = E_{3}L_{3} = 2\text{~V}$. The power is calculated as before.

$$
P_{3} = I_{3}\Delta V_{3} = 10\text{~W}
$$

Notice that we could have also used [Kirchoff's Loop Rule](/empcubed/notes/week-06-resistors-combinations/r_energy/#energy_around_the_circuit) to find the voltage of different segments. For now, it will serve as a nice check on our math. If we travel along the direction of conventional current (counterclockwise in our representation), voltage decreases, so $\Delta V_{1}$, $\Delta V_{2}$, $\Delta V_{3} < 0$, whereas we have $\Delta V_{battery} > 0$. These four potential differences form a loop, so by Kirchoff's Loop Rule they should add to 0:

$$
\Delta V_{battery} + \Delta V_{1} + \Delta V_{2} + \Delta V_{3} = 12\text{~V} - 1\text{~V} - 9\text{~V} - 2\text{~V} = 0
$$

Sometimes we will not have as much information as we did here, and using the Loop Rule will be required. For now, it serves as a nice check.
