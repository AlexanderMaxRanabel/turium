class TuringMachineInterpreter:
    def __init__(self, program):
        self.program = program
        self.tape = [0]
        self.position = 0

    def interpret(self):
        current_instruction = self.program["start"]
        while True:
            instruction_parts = current_instruction.split(" ")
            instruction_name = instruction_parts[0]
            instruction_args = instruction_parts[1:]

            if instruction_name == "move":
                direction = instruction_args[0]
                self.move_tape_head(direction)
            elif instruction_name == "write":
                symbol = int(instruction_args[0])
                self.write_to_tape(symbol)
            elif instruction_name == "branch":
                symbol = int(instruction_args[0])
                branch_to = instruction_args[1]
                if self.tape[self.position] == symbol:
                    current_instruction = self.program[branch_to]
                    continue
                else:
                    break

            if current_instruction == "halt":
                break

            current_instruction = self.get_next_instruction(current_instruction)

    def move_tape_head(self, direction):
        if direction == "left":
            self.position -= 1
            if self.position < 0:
                self.tape.insert(0, 0)
                self.position = 0
        elif direction == "right":
            self.position += 1
            if self.position == len(self.tape):
                self.tape.append(0)

    def write_to_tape(self, symbol):
        self.tape[self.position] = symbol

    def get_next_instruction(self, current_instruction):
        instruction_names = list(self.program.keys())
        current_index = instruction_names.index(current_instruction)
        next_index = current_index + 1
        return instruction_names[next_index]

