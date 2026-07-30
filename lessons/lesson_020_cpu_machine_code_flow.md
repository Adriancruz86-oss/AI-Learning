# Lesson 008: From Code to Machine Instructions

## Overview

This lesson explains how a simple instruction moves from human-readable code to electrical activity inside a computer.

The basic flow is:

1. Source code
2. Assembly language
3. Machine code
4. CPU instruction cycle
5. Memory and hardware activity

## Source Code

Source code is written for humans to read.

Example:

```python
result = 2 + 3
The CPU does not directly understand Python.
A programming language must be translated or interpreted into lower-level instructions.
Assembly Language
Assembly language represents CPU instructions using short human-readable names.
Example:
MOV
ADD
SUB
JMP
CMP
Common instructions include:
MOV — move data
ADD — add values
SUB — subtract values
CMP — compare values
JMP — jump to another instruction
LOAD — load data from memory
STORE — write data to memory
Assembly language depends on the CPU architecture.
An Intel processor and an ARM processor may use different instruction sets.
Machine Code
Machine code is the binary representation of CPU instructions.
Example:
10110000 00000101
The exact meaning depends on the processor architecture.
Some bits may represent:
The operation
The register
A memory location
A number
The instruction format
Machine code is not just random binary.
It is structured according to the CPU’s instruction set architecture.
Registers
Registers are tiny, extremely fast storage locations inside the CPU.
They hold information the processor is actively using.
Examples include:
Numbers being calculated
Memory addresses
Current instructions
Intermediate results
Registers are much faster than RAM, but they hold far less data.
Program Counter
The program counter stores the memory address of the next instruction.
After an instruction is processed, the program counter usually moves to the next instruction.
A jump instruction can change it to another address.
Instruction Register
The instruction register holds the instruction currently being decoded or executed.
Fetch, Decode, Execute
The CPU repeatedly performs the instruction cycle.
Fetch
The CPU uses the program counter to locate the next instruction in memory.
The instruction is copied from RAM into the CPU.
Decode
The control unit examines the instruction.
It determines:
What operation is requested
Which registers are involved
Whether memory must be accessed
Where the result should go
Execute
The CPU performs the instruction.
This may involve:
Arithmetic
Comparison
Moving data
Reading memory
Writing memory
Changing the program counter
Example Flow
Consider a simplified instruction:
ADD register_A, register_B
The CPU may:
Fetch the instruction from RAM.
Place it in the instruction register.
Decode the operation as addition.
Read the values in both registers.
Send the values to the arithmetic logic unit.
Add the values.
Store the result in a register.
Advance the program counter.
Arithmetic Logic Unit
The arithmetic logic unit, or ALU, performs operations such as:
Addition
Subtraction
AND
OR
XOR
Comparisons
Bit shifting
Control Unit
The control unit coordinates the processor.
It directs:
Which registers should be read
Which operation the ALU should perform
Whether memory should be accessed
Where results should be stored
RAM and the CPU
RAM stores active programs and data.
The CPU communicates with RAM using electrical pathways called buses.
Important bus functions include:
Address bus — identifies where data should be read or written
Data bus — carries the actual data
Control bus — carries commands such as read or write
Binary and Electrical States
Binary values are physically represented by voltage states.
A simplified model is:
Low voltage  = 0
High voltage = 1
Transistors act like tiny electronic switches.
Large groups of transistors form:
Logic gates
Registers
Memory cells
Arithmetic circuits
Control circuits
Security+ Connection
This foundation helps explain:
Buffer overflows
Malware execution
Memory corruption
CPU architecture
Code injection
Privilege escalation
Exploit development
Data execution prevention
Key Takeaway
The CPU does not understand Python, English, or abstract commands.
It processes machine instructions defined by its architecture.
Those instructions are fetched from memory, decoded by the control unit, and executed using registers, logic circuits, and 
electrical signals.
