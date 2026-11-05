---
title: 'Making Models with VPython'
weight: 5
---

Computers and computational modeling provide a powerful (and almost necessary) tool in modern scientific research and engineering work. While analytic (i.e., paper and pencil) solutions do exist for some problems, computational modeling allows you to create 3D visualizations, incorporate more complex behavior, model millions of particles at the same time, analyze massive amounts of data, or simply solve repetitive calculations. In addition to solving analytic problems, this course will have you working with simple computational models in VPython (a Python-based programming language that specializes in visualization). You will develop these computational models in class with the help of your classmates and the guidance of instructors. In these notes, you will read about how to write your programs so that they follow a common structure, which will make it easier to write new programs in the future.

## Structuring your programs

There are 5 major components that you will repeat in each program that you write:

1.  **Objects** - Each program that you write is modeling some physical object(s). In setting up your objects, you are telling the computer what shape, size, and color to make the object as well as where to put the object. A big list of objects is [available online](http://vpython.org/contents/docs/primitives.html). Simplicity is key for choosing your objects; for example, a river can be modeled as a large, blue rectangle.
2.  **Parameters & initial conditions** - You will then need your program to associate physical quantities with one or more of the objects in the scene. These might be the object's mass, momentum, charge, etc. These parameters and initial conditions depend on the problem you are trying to solve and are often informed by the problem statement or analytical calculations.
3.  **Step variable and step size** - In every program you also need to answer two questions: What variable do I want to change? And how much do I want to change it by? These are the step variable and step size. In Mechanics, the step variable is often time because you want to calculate how the object's position and velocity change as time changes. Another common step variable is distance because sometimes how the force or energy changes as you get farther away from the object is more important (as you will see this semester). Typically, [the smaller the step size, the more accurate the program will be](https://pcubed.msuperl.org/notes/week-04-05-springs-contact-interactions/springmotion/#modeling_motion_with_spring_forces), but there's a tradeoff: the computer has to do more calculations – making the program run longer.
4.  **Calculation loop** - A loop is a programming structure that will repeat certain lines of code multiple times. You get to choose the number of repetitions based on what step variable you chose. When you have a loop like this, particularly if the loop calculates new values based on old values and a step size, it is called an [iterative loop or iterative process](https://pcubed.msuperl.org/notes/week-02-modeling-motion-net-force/iterativepredict/). In general, a calculation loop needs to:
    - Have a limit on how many times to run (i.e., repeat this code as long as t \< 10 or d \< 1)
    - Calculate the fundamental physical parameters (i.e., [calculate all the forces acting on the system, and determine the net force](https://pcubed.msuperl.org/notes/week-02-modeling-motion-net-force/momentum_principle/#net_force))
    - Update any physical parameters that depend on those (i.e., [update the momentum using that net force](https://pcubed.msuperl.org/notes/week-02-modeling-motion-net-force/motionpredict/) and [update the position using this new momentum](https://pcubed.msuperl.org/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#predicting_the_motion_of_objects))
    - Update the step variable by adding 1 step size (i.e., move a little forward in time or move a little farther away from the object)
5.  **Comments** - Comments are lines of code that the computer will ignore. In VPython this is done by starting a line with a \# symbol. Comments serve as notes to yourself or others about what that piece of code is supposed to do. These are particularly useful if someone else is going to read your code or if you look back on your code at some later date. Commenting your code is a good habit to get into.

## Example of VPython Code

### Video Example

This video will walk you through how to model a fancart on a track in VPython.

{{< youtube IEA2hgB6bdE >}}

### VPython Code

Below is the code that was written in the lecture video above.

<div class="Definition-Term">

fancartModel.py

</div>

    from visual import *
    from physutil import *

    #Set up windows
    scene.width = 1024
    scene.height = 768

    #Objects
    track = box(pos=vector(0,0,0), size=vector(10,0.1,1), color=color.white)
    fancart = box(pos=vector(-4.75,0.15,0), size=vector(0.5,0.19,0.3), color=color.red)
    fancartMotionMap = MotionMap(fancart, 10, 10, markerScale=2)

    #Parameters and Initial Conditions
    fancart.mass = 0.3
    fancart.p = vector(0.15,0,0)

    #Time and time step
    dt = 0.5
    t = 0

    #Calculation loop
    while t < 10:

        rate(25)

        Ffan = vector(0.025,0,0)

        fancart.p = fancart.p + Ffan*dt
        fancart.pos = fancart.pos + (fancart.p/fancart.mass)*dt
        fancartMotionMap.update(t, fancart.p)

        t = t + dt
