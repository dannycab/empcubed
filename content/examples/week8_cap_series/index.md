---
title: 'Example: Capacitors in Series'
weight: 14
---

*[Return to capacitors in series notes](/notes/week-08-capacitors-combinations/c_series/)*

Suppose you have the following circuit. Capacitors are labeled 1 and 2 for convenience of reference. You know that the circuit contains a 12-Volt battery, $Q_{1} = 4.5\mu\text{C}$, and $C_{2} = 0.5\mu\text{F}$. What is the capacitance of Capacitor 1? What happens to the charge on *both* of the capacitors if we insert a dielectric material with dielectric constant $k = 3$ into Capacitor 1?

<img src="./media/rId10.png" style="width:3.125in;height:3.14583in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

Circuit with Capacitors in Series

### Facts

- $\Delta V_{\text{bat}} = 12\text{~V}$​
- $Q_{1} = 4.5\mu\text{C}$​
- $C_{2} = 0.5\mu\text{F}$​
- $k = 3$​

### Lacking

- $C_{1}$​
- How the charges change when the dielectric is inserted.

### Approximations & Assumptions

- The wire has very very small resistance when compared to the other resistors in the circuit: Having wires with a very small resistance allows us to ignore any potential differences across the wires while also ensuring the initial current in the circuit isn't too high.
- We are measuring things like potential differences and charges when the circuit is in a steady state: As we know capacitors create a quasi-steady state while they are charging which can make things tough. It is easier to look at the final state when they are fully charged and the current in the circuit is not changing with time.
- Approximating the battery as a mechanical battery: This means the battery will supply a steady power source to the circuit to keep it in steady state.
- Capacitors are parallel plate capacitors: Assuming this geometry allows us to use the equation provided in the notes about the capacitance of a parallel plate capacitor. This Equation would change if we changed the shape of the capacitor.

### Representations

- We represent capacitance as

$$
C = \frac{Q}{\Delta V}
$$

- We represent the equivalent capacitance of multiple capacitors arranged in series as

$$
\frac{1}{C_{\text{equiv}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}} + \ldots
$$

- We represent the situation with diagram given above.

## Solution

### Part 1

Let's find $C_{1}$. In order to use the equation for equivalent capacitance of capacitors in series, as we have here, we first need the equivalent capacitance of the entire circuit. Remember that the [charge on the capacitors](/notes/week-08-capacitors-combinations/c_series/#node_rule_and_charge_in_series) in series should be the same, so $Q_{\text{equiv}} = Q_{1} = Q_{2}$. Now, we can write:

$$
C_{\text{equiv}} = \frac{Q_{\text{equiv}}}{\Delta V_{\text{bat}}} = 0.375\mu\text{F}
$$

Now we can solve for $C_{1}$ using

$$
\frac{1}{C_{\text{equiv}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}}
$$

This gives us $C_{1} = 1.5\mu\text{F}$

### Part 2

<img src="./media/rId20.png" style="width:3.125in;height:3.83333in" alt="[ALT TEXT NEEDED: figure-02.png -- describe this figure for screen readers]" />

Circuit with Capacitors in Series, one capacitor has a dielectric

Now we need to consider what happens when we insert a dielectric. It might look something like the circuit to the right. A description of what a dielectric does in a capacitor is [here](/notes/week-08-capacitors-combinations/cap_charging/#dielectrics). Its [effect on capacitance](/notes/week-08-capacitors-combinations/cap_in_cir/#finding_capacitance) is:

$$
C = \frac{k\epsilon_{0}A}{d}
$$

So when we insert the dielectric, we have a new capacitance for Capacitor 1: $C_{\text{1, new}} = kC_{1} = 4.5\mu\text{F}$. To find the new value that the capacitors are charged to, we return to the equivalent capacitance of the circuit:

$$
\frac{1}{C_{\text{equiv, new}}} = \frac{1}{C_{\text{1, new}}} + \frac{1}{C_{2}}
$$

This yields $C_{\text{equiv, new}} = 0.45\mu\text{F}$. Now, we can find the new charge:

$$
Q_{\text{new}} = C_{\text{equiv, new}}\Delta V_{\text{bat}} = 5.4\mu\text{C}
$$

**This is the charge on *both* capacitors** since the capacitors are in series. So even if we insert a dielectric in only one of the capacitors, the charge on both will increase.

In order for us to evaluate this solution and make sure it makes sense, we must understand what the dielectric is doing in the capacitor. The dielectric is an insulator which means its electrons are tied to the nuclei. When a dielectric is put between two charged plates it will polarize. This will create an electric field in the dielectric that opposes the electric field of the plates. This will allow more charges to be added to the plates before the capacitor will have an electric field that fully opposes that of the power source. This solution lines up with that perfectly.
