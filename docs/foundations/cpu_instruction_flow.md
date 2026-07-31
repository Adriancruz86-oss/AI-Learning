# CPU Instruction Flow: From Machine Code to Register Update

## Purpose

This note records a supporting computer-foundations lesson that connects logic gates, registers, buses, decoders, the ALU, and the fetch-decode-execute cycle.

It is not part of the numbered AI lesson sequence. The deeper hardware path belongs in the companion repository **Atom-to-Intelligence**, but this foundation helps explain what the machine is doing underneath future AI code.

## A Simple LOAD Instruction

Using a made-up instruction format:

```text
0001 01 00001000
```

The fields mean:

```text
0001      = LOAD opcode
01        = destination register R1
00001000  = value 8
```

The opcode tells the CPU what action to perform. The register field tells it where to store the value. The final field contains the immediate data.

To complete the instruction:

1. The value `00001000` is placed on the data bus.
2. R1's write-enable signal turns on.
3. At the clock edge, R1 captures the value.

Afterward:

```text
R1 = 8
```

## Reading From and Writing To a Shared Bus

A shared bus can be heard by many destinations at once, but normally only one source should drive it at a time.

- Multiple registers may capture the same bus value if their write-enable lines are active.
- Two registers driving different values onto the same bus can cause bus contention.

For a register transfer:

```text
R1 → bus → R2
```

R1 drives the bus. R2 captures the value at the clock edge. R1 keeps its original value; the transfer copies rather than empties it.

## Register Selection With a Decoder

With four registers, a two-bit selector can choose which register drives the bus:

```text
00 → R0
01 → R1
10 → R2
11 → R3
```

A decoder converts the selector bits into one active output-enable signal.

For example:

```text
source selector = 10       → R2 drives the bus
destination selector = 11  → R3 write-enable turns on
```

At the next clock edge, R3 copies R2.

## Sending Values Through the ALU

Suppose:

```text
R1 = 8
R2 = 5
```

The instruction:

```text
ADD R3, R1, R2
```

means:

> Add the values in R1 and R2, then store the result in R3.

A made-up binary form could be:

```text
0010 11 01 10
```

The fields mean:

```text
0010 = ADD opcode
11   = destination R3
01   = source R1
10   = source R2
```

The CPU then performs this flow:

```text
R1 and R2 → ALU
ALU operation = ADD
ALU output = 13
13 → bus → R3
clock edge → R3 stores 13
```

Afterward:

```text
R1 = 8
R2 = 5
R3 = 13
```

The source registers remain unchanged.

## Fetch, Decode, Execute

The full instruction cycle is:

### Fetch

Retrieve the instruction bits from memory.

### Decode

Separate the fields and determine:

- the opcode
- the destination register
- the source registers
- the control signals required

For the ADD example, decoding produces actions equivalent to:

```text
Read R1
Read R2
Set ALU to ADD
Enable R3 write
```

### Execute

Route the source values into the ALU, perform the operation, place the result on the bus, and store it in the destination register at the clock edge.

## Current Mental Model

```text
machine-code fields
→ decoder and control signals
→ source registers selected
→ values move through buses
→ ALU performs the operation
→ destination write-enable activates
→ clock edge stores the result
```

This connects the major CPU components into one complete instruction flow instead of treating them as isolated parts.
