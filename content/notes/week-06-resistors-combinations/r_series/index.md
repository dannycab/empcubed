---
title: 'Resistors in Series'
weight: 6
textbook_ref: 'Sections 19.2 and 19.3 in Matter and Interactions (4th edition)'
---

Up until now, we have talked about resistors from a very microscopic point of view and have introduced the idea of resistance, which helps us talk about resistors from a more macroscopic perspective. This week will be continuing to consider circuits from a macro-view and thinking about what happens when we combine multiple circuit elements in one circuit. These notes will focus on a particular way to combine resistors (in series) and what the effects of that would be on the circuit.

{{< youtube _j6jrTWTK7E >}}

## Circuit Diagrams

<img src="./media/rId13.png" style="width:2.08333in;height:1.03125in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

Resistor representation in a circuit diagram

Circuit diagrams are a simplified way to represent a circuit. In a circuit diagram, each element is represented by some kind of symbol and the wires are represented by lines. These diagrams are not very good for showing what is happening to surface charges or the electric field, but they do help visualize a circuit particularly for combinations of circuit elements and some of the more macroscopic properties.

[We have already briefly talked about the symbol for a battery](/notes/week-05-moving-charges-batteries/batteries/); we will begin to use this much more frequently this week. Any kind of resistor - whether it's a lightbulb, a thin resistor, a thick resistor, made from a different material, etc. - is represented by a squiggly line. As we said before, wires are generally just represented by lines.

## Node Rule and Current in Series

<img src="./media/rId19.png" style="width:2.08333in;height:1.9375in" alt="[ALT TEXT NEEDED: figure-02.png -- describe this figure for screen readers]" />

Current remains the same across resistors in series

When two circuit elements are in series this means that **all of the current that goes into the first element also goes into the second element**, *assuming a steady state current situation*. For example, consider two resistors that are in series with a battery. All of the current that comes out of the battery **must** travel through the wire and go through the first resistor. After the first resistor, all the current must then pass through the second resistor - there is no other path for electrons to travel along. Finally, all the current must then return to the battery. Note, we have drawn the conventional current coming from the positive plate of the battery (rather than the electron current which would come from the negative plate).

This means that **in series, circuit elements always have the same current with no alternate paths for current flow**. This conclusion follows naturally from the [node rule](/notes/week-06-resistors-combinations/current/), which is a mathematical statement of the conservation of charge in steady state. In terms of the circuit above, this means that the current that goes through the battery ($I_{bat}$) is equal to the current through the first resistor ($I_{1}$), which is equal to the current through the second resistor ($I_{2}$).

$$
I_{bat} = I_{2} = I_{1}
$$

## Loop Rule and Voltage in Series

<img src="./media/rId25.png" style="width:3.125in;height:2.17708in" alt="[ALT TEXT NEEDED: figure-03.png -- describe this figure for screen readers]" />

Potential differences (or voltage drops) throughout the circuit

For resistors in series, we can also say something about the difference in electric potential across each circuit element. Using the [loop rule](/notes/week-06-resistors-combinations/r_energy/), we know that **the sum of all of the changes in electric potential around a complete loop must equal zero.** Consider the same series circuit above with the battery and two resistors. If we think about the electric potential or energy per charge going around the circuit, we know that the highest electric potential will be on the positive side of the battery. As the current moves through the wire, there would be a small drop in electric potential along the wire (from the electron collisions with the nuclei), but a much larger change in potential would occur over the resistor. Then again, there would be another small drop over the next wire with a larger change over the second resistor, with a final small drop over the wire that connects back to the battery. If we move from the negative plate of the battery back to the positive plate, then there is now a large gain in electric potential (instead of a drop), and we have returned to where we started.

Oftentimes, the changes in potential in the wires are so small compared to those over the resistors, that we *assume the changes in electric potential across the wires are negligible*. You
