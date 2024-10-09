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

        else:
            print(f"Unknown instruction: {instruction}")

        self.prints()  # Print the state after each instruction execution

# Example usage
cpu = CPU()

# Sample instruction list (format: "OPCODE", Rd, Rs, Rt)
instructions = [
    ("ADDI", 1, 2, 5),  # $r1 = $r2 + 5
    ("SUBI", 3, 1, 2),  # $r3 = $r1 - 2
    ("SLT", 4, 1, 3),   # $r4 = ($r1 < $r3)
]

# Initialize registers with some values for testing
cpu.registers[2] = 10  # Set $r2 = 10
cpu.registers[3] = 5   # Set $r3 = 5

# Fetch and execute instructions
while True:  # Continuously fetch and execute until no more instructions
    instruction = cpu.fetch(instructions)  # Fetch without wrapping in a new list
    if instruction is None:  # Break if no more instructions
        break
    cpu.execute(instruction)
