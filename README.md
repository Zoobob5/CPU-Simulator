# CPU Simulator in Python

## Overview

This project is a simple CPU simulator built in Python as part of a portfolio project for **CS104: Computer Architecture**. The simulator mimics basic CPU functionalities such as loading instructions, executing them, and simulating memory and register interactions.

## Features

- Simulates a basic CPU with 32 (but didnt use all 32) general-purpose registers.
- Supports common MIPS-like instructions:
  - `ADD`: Add two registers and store the result.
  - `ADDI`: Add an immediate value to a register.
  - `SUB`: Subtract one register from another.
  - `SUBI`: Subtract an immediate value from a register.
  - `SLT`: Set a register to 1 if a comparison between two registers is true.
  - `LW`: Load a word from memory.
  - `SW`: Store a word in memory.
  - `BNE`: Branch to a specific instruction if two registers are not equal.
- Instructions are loaded from an external file (`instructions.txt`).
- Includes support for handling comments and formatting in the instructions file which formats:
```
ADDI 1 0 5    # $r1 = $r0 + 5 (After this instruction, $r1 = 5)
ADDI 2 0 10   # $r2 = $r0 + 10 (After this instruction, $r2 = 10)
ADD 3 1 2     # $r3 = $r1 + $r2 (After the above, $r3 = 15)
```

## How to Run
-written and ran on VScode
### Prerequisites

- Python 3.x installed on your machine.
