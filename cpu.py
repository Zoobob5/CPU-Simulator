class CPU:
    def __init__(self):
        self.registers = [0] * 32
        self.pc = 0
        self.memo = [0] * 1024  # Memory (memo)

    def prints(self):
        print(f'Program Counter (PC): {self.pc}')
        print('Registers:')
        for i in range(len(self.registers)):
            print(f"$r{i}: {self.registers[i]}")
        print("-" * 40)

    def load(self, memo):
        self.memo = memo

    def fetch(self, instructions):
        if self.pc < len(instructions):  # Check if PC is within bounds
            instruction = instructions[self.pc]  # Fetch instruction based on PC
            self.pc += 1
            return instruction
        else:
            return None  # Return None if no more instructions

    def execute(self, instruction):
        if instruction is None:
            print("No more instructions to execute.")
            return

        opcode = instruction[0]
        if opcode == "ADD":
            rd, rs, rt = instruction[1], instruction[2], instruction[3]
            self.registers[rd] = self.registers[rs] + self.registers[rt]
            print(f"ADD: $r{rd} = $r{rs} + $r{rt} -> {self.registers[rd]}")

        elif opcode == "SUB":
            rd, rs, rt = instruction[1], instruction[2], instruction[3]
            self.registers[rd] = self.registers[rs] - self.registers[rt]
            print(f"SUB: $r{rd} = $r{rs} - $r{rt} -> {self.registers[rd]}")

        elif opcode == "LW":
            rt, offset, rs = instruction[1], instruction[2], instruction[3]
            address = self.registers[rs] + offset
            self.registers[rt] = self.memo[address]
            print(f"LW: $r{rt} = MEM[{address}] -> {self.registers[rt]}")

        elif opcode == "SW":
            rt, offset, rs = instruction[1], instruction[2], instruction[3]
            address = self.registers[rs] + offset
            self.memo[address] = self.registers[rt]
            print(f"SW: MEM[{address}] = $r{rt} -> {self.memo[address]}")

        elif opcode == "ADDI":
            rt, rs, immd = instruction[1], instruction[2], instruction[3]
            self.registers[rt] = self.registers[rs] + immd
            print(f"ADDI: $r{rt} = $r{rs} + {immd} -> {self.registers[rt]}")

        elif opcode == "SUBI":
            rt, rs, immd = instruction[1], instruction[2], instruction[3]
            self.registers[rt] = self.registers[rs] - immd
            print(f"SUBI: $r{rt} = $r{rs} - {immd} -> {self.registers[rt]}")

        elif opcode == "SLT":
            rd, rs, rt = instruction[1], instruction[2], instruction[3]
            self.registers[rd] = 1 if self.registers[rs] < self.registers[rt] else 0
            print(f"SLT: $r{rd} = ($r{rs} < $r{rt}) -> {self.registers[rd]}")

        elif opcode == "BNE":
            rs, rt, offset = instruction[1], instruction[2], instruction[3]
            if self.registers[rs] != self.registers[rt]:  # Branch if not equal
                self.pc += offset  # Update PC with offset
                print(f"BNE: Branching to PC = {self.pc}")
            else:
                print(f"BNE: Not branching. $r{rs} == $r{rt}.")

        else:
            print(f"Unknown instruction: {instruction}")

        self.prints()  # Print the state after each instruction execution

# Example usage
cpu = CPU()

# Sample instruction list with examples
instructions = [
    ("ADD", 1, 2, 3),  # $r1 = $r2 + $r3 (Assuming $r2 = 10, $r3 = 5)
    ("SUB", 4, 1, 2),  # $r4 = $r1 - $r2 (After ADD, $r1 = 15, $r2 = 10)
    ("ADDI", 5, 4, 5),  # $r5 = $r4 + 5 (After SUB, $r4 = 5, so $r5 = 10)
    ("SUBI", 6, 5, 3),  # $r6 = $r5 - 3 (After ADDI, $r5 = 10, so $r6 = 7)
    ("SLT", 7, 2, 3),   # $r7 = ($r2 < $r3) (Comparing $r2 = 10, $r3 = 5, $r7 should be 0)
    ("BNE", 1, 2, 2),   # If $r1 != $r2, branch to instruction 2
    ("SUBI", 3, 1, 2),  # $r3 = $r1 - 2 (Should be skipped if BNE is taken)
    ("BNE", 1, 2, -2),  # If $r1 != $r2, branch back to instruction 2 (loop)
    ("LW", 8, 0, 0),    # $r8 = MEM[$r0 + 0] (Load from address 0)
    ("SW", 8, 0, 0),    # MEM[$r0 + 0] = $r8 (Store $r8 at address 0)
]

# Initialize registers with some values for testing
cpu.registers[0] = 0  # $r0 is usually hardcoded to 0
cpu.registers[2] = 10  # Set $r2 = 10
cpu.registers[3] = 5   # Set $r3 = 5
cpu.registers[4] = 15  # Set $r4 = 15 (example value for ADD)
cpu.registers[5] = 10  # Set $r5 = 10 (example value for ADDI)

# Fetch and execute instructions
while True:  # Continuously fetch and execute until no more instructions
    instruction = cpu.fetch(instructions)  # Fetch without wrapping in a new list
    if instruction is None:  # Break if no more instructions
        break
    cpu.execute(instruction)
