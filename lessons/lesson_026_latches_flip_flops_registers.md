# Lesson 026: Latches, Flip-Flops, Registers, and CPU Timing

## Goal

Understand how a computer moves from simple logic gates to controlled memory and synchronized CPU operations.

## 1. Feedback Creates Memory

A normal logic gate produces an output from its current inputs. A latch adds feedback by routing outputs back into the circuit.

```text
output → input path → output
```

Once the circuit settles into a stable state, the feedback keeps reinforcing that state. This allows the circuit to remember one bit.

**Key idea:** A latch stores one bit by feeding its output back into the circuit.

## 2. SR Latch

An SR latch has two control inputs:

- `S` means set the stored bit to `1`.
- `R` means reset the stored bit to `0`.
- `Q` is the stored output.
- `Q̅` is the opposite of `Q`.

For a NOR-based SR latch:

| S | R | Result |
|---|---|---|
| 0 | 0 | Hold the previous state |
| 1 | 0 | Set `Q` to `1` |
| 0 | 1 | Reset `Q` to `0` |
| 1 | 1 | Invalid or problematic state |

When `Q = 1` and `Q̅ = 0`, each output helps keep the other output in the opposite state. They remain locked until an external control signal changes the state.

**Key idea:** Set and reset choose the state; feedback preserves it afterward.

## 3. Enable Control

A gated latch adds an enable input.

- `Enable = 1`: the gate is open and inputs may change the stored bit.
- `Enable = 0`: the gate is closed and the latch keeps its current value.

Opening the gate does not automatically change the bit. It only gives the input permission to affect the stored value.

## 4. D Latch

A D latch replaces separate set and reset choices with one data input, `D`.

- `D = 1` means store `1`.
- `D = 0` means store `0`.
- While enabled, `Q` follows `D`.
- While disabled, `Q` holds its previous value.

Internally, the circuit can use `D` and `NOT D` so the dangerous SR-latch input combination cannot occur.

```text
Enable = 1 → Q follows D
Enable = 0 → Q remembers its previous value
```

**Key idea:** A D latch stores the value on `D` while enabled, then holds it when disabled.

## 5. Flip-Flop

A latch can change during an entire open enable window. A flip-flop changes only at a specific clock edge.

```text
Clock:  ___|‾‾‾|___|‾‾‾|___
           ↑       ↑
        capture  capture
```

At the selected edge, the flip-flop samples the input and stores it. After the edge, the output remains fixed until the next relevant edge.

- **Latch:** changes during an open window.
- **Flip-flop:** changes at one precise clock edge.

This timing prevents values from changing unpredictably while other CPU components are still working.

**Key idea:** A flip-flop stores the value present at its input when the clock edge arrives.

## 6. Registers

One flip-flop stores one bit. A register groups several flip-flops so multiple bits can be stored together.

```text
8 flip-flops = 8 bits = 1 byte
```

An 8-bit register might hold:

```text
10110010
```

That pattern could represent a number, instruction, memory address, character, or other data.

Registers commonly include a load control:

- `Load = 1` at the clock edge: capture the new value.
- `Load = 0` at the clock edge: preserve the old value.

**Key idea:** A register is a group of flip-flops that stores several bits together.

## 7. Buses Move Register Data

A bus is a shared group of wires that carries several bits at once. An 8-bit bus carries eight bits in parallel.

```text
Register A ──┐
Register B ──┼──> 8-bit bus ──> ALU or another register
Register C ──┘
```

The control unit selects one source to place data on the bus and one or more destinations to receive it.

Example:

```text
A_out = 1   → Register A places its value on the bus
B_load = 1  → Register B captures the bus value at the clock edge
```

Only one source should normally drive the same bus at a time, or components could attempt to force conflicting electrical values onto the wires.

**Key idea:** Choose a source, place its value on the bus, choose a destination, and capture it on the clock edge.

## 8. Control Unit and Clock

The control unit coordinates the registers, buses, ALU, and clock by activating control signals in the correct sequence.

For a register transfer:

```text
A_out = 1
B_load = 1
clock edge arrives
```

For an arithmetic instruction, the control unit selects the source values, tells the ALU which operation to perform, and enables a destination register to store the result.

The clock keeps these actions synchronized:

1. Inputs and control signals settle.
2. The clock edge arrives.
3. Enabled flip-flops and registers capture their new values.
4. The circuit works with those stable values until the next edge.

Not every component changes on every clock edge. Only components whose control signals permit an update will change.

## 9. Connection to Fetch, Decode, Execute

The CPU repeats three broad stages:

1. **Fetch:** retrieve the next instruction from memory.
2. **Decode:** determine whether the instruction means add, load, jump, or another operation.
3. **Execute:** activate the required registers, buses, ALU operation, and storage controls.

A simple instruction may require several smaller timed hardware actions.

```text
instruction command
        ↓
control signals
        ↓
register and bus movements
        ↓
ALU operation
        ↓
result stored at a clock edge
```

## Complete Mental Model

```text
logic gates
    ↓
feedback
    ↓
latches
    ↓
D latches
    ↓
flip-flops
    ↓
registers
    ↓
buses and ALU
    ↓
control unit and clock
    ↓
fetch-decode-execute
```

- Gates make decisions.
- Latches and flip-flops remember bits.
- Registers hold groups of bits.
- Buses move those bits.
- The ALU performs operations.
- The control unit coordinates the actions.
- The clock determines when state changes are committed.
- Fetch, decode, and execute repeat the process.

## Next Layer

The next lesson should connect this CPU skeleton to a running program through:

- the program counter,
- the instruction register,
- memory addresses,
- sequential instruction flow,
- and jump instructions.
