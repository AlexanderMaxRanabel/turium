## Turium Programming Language

Turium is a simple programming language inspired by Turing machines. The language consists of a set of instructions that manipulate a tape of symbols, similar to a Turing machine tape. The language has three types of instructions: move, write, and branch.
Move Instruction

The move instruction moves the tape head left or right by one position. The instruction has a single argument that specifies the direction to move (either "left" or "right").

Syntax: move <direction>

Example: move left
Write Instruction

The write instruction writes a symbol to the current tape position. The instruction has a single argument that specifies the symbol to write.

Syntax: write <symbol>

Example: write 1
Branch Instruction

The branch instruction branches to a different instruction based on the current tape symbol. The instruction has two arguments: the symbol to match and the name of the instruction to branch to if the match succeeds. If there is no match, the program terminates.

Syntax: branch <symbol> <instruction name>

Example: branch 0 loop
Instruction Names

Each instruction must have a unique name that can be used in branch instructions.

Syntax: <instruction name>: <instruction>

Example:

start:
write 1
move right
branch 0 loop
halt:

# Program Structure

A program consists of a series of instructions, each with a unique name. The program starts execution at the first instruction.

Example program to increment a binary number:

start:
branch 0 increment
halt:
increment:
write 1
move right
branch 0 increment
write 0
move left
branch B halt

In this program, the current tape symbol is checked for a match with 0 at the start instruction. If there is a match, the program branches to the increment instruction, which writes a 1 to the current tape position and moves right. The program then checks for a match with 0 again and repeats the increment instruction until there is no match. When there is no match, the program branches to the halt instruction and terminates.
Using the Interpreter

To use the Turium interpreter, you first need to define a program as a dictionary of instructions. Each instruction should be a string in the format <instruction name>: <instruction>. The keys of the dictionary should be the instruction names, and the values should be the corresponding instruction strings

program = {
    "start": "branch 0 increment",
    "increment": "write 1\nmove right\nbranch 0 increment\nwrite 0\nmove left\nbranch B halt",
    "halt": ""
}

Next, you can create a TuringMachineInterpreter object and pass in the program dictionary as an argument. Then, you can call the interpret method on the interpreter object to execute the program.

interpreter = TuringMachineInterpreter(program)
interpreter.interpret()

The interpreter executes the program by interpreting each instruction in turn, until it reaches the "halt" instruction. The tape is represented as a list of integers, with the current tape position stored as an index into the list. The interpreter updates the tape and position as it executes each instruction.
Conclusion

Turium is a simple programming language that can be used to explore the concepts of Turing machines and tape-based computation. While the language is limited in its features, it can be extended with additional instructions and features to create more complex programs.
