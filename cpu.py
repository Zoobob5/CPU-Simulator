class CPU:
    def __init__(self):
        self.registers = [0] * 32
        self.pc = 0
        self.memo = [0] * 1024

    def prints(self):
        print(f'Program Counter (PC): {self.pc}')
        print('Registers:')
        for i in range(len(self.registers)):
            print(f"$r{i}: {self.registers[i]}")
        print("-" * 40)

    def load(self, memo):
        self.memo = memo

    def fetch(self, list):
        instruction = list[self.pc]
        self.pc += 1
        return instruction

    def execute(self,instruction):
        print(f"Executing instruction: {instruction}")
        # Example: parsing and executing MIPS instructions will be added later

cpu = CPU()
cpu.prints()
