Here is an explanation of the different components and their functionalities:

1. `Pulse`: It is a named tuple that represents a pulse in the circuit. It has three fields: `source`, `target`, and `type`. The `source` and `target` represent the source and target modules of the pulse, and the `type` represents the type of the pulse, which can be either "+" (HIGH) or "-" (LOW).

2. `FlipFlop`: It represents a FlipFlop module in the circuit. When it receives a LOW pulse, it changes its state and sends a HIGH pulse to its target modules. When it receives a HIGH pulse, it ignores it.

3. `Conjunction`: It represents a Conjunction module in the circuit. It keeps track of the last received pulse from each of its source modules. If all the source pulses are HIGH, it sends a LOW pulse to its target modules; otherwise, it sends a HIGH pulse.

4. `Broadcaster`: It represents a Broadcaster module in the circuit. It simply forwards the received pulse to all its target modules.

5. `Circuit`: It represents the circuit itself, which consists of multiple modules. It keeps track of the active pulses in the circuit and counts the number of LOW and HIGH pulses. It provides methods to push the button (simulate a button push) and find the number of button pushes needed to generate a specific pulse.
