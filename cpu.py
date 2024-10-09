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

        else:
            print(f"Unknown instruction: {instruction}")

        self.prints()  # Print the state after each instruction execution

# Example usage
cpu = CPU()

# Sample instruction list (format: "OPCODE", Rd, Rs, Rt)
instructions = [
    ("ADD", 1, 2, 3),  # $r1 = $r2 + $r3
    ("SUB", 1, 2, 3),  # $r1 = $r2 - $r3
]

# Initialize registers with some values for testing
cpu.registers[2] = 10  # $r2 = 10
cpu.registers[3] = 5   # $r3 = 5

# Fetch and execute instructions
while True:  # Continuously fetch and execute until no more instructions
    instruction = cpu.fetch(instructions)  # Fetch without wrapping in a new list
    if instruction is None:  # Break if no more instructions
        break
    cpu.execute(instruction)
