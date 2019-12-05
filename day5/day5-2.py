"""
--- Part Two ---

The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?
"""
import time

start_time = time.time()
f = open("../inputs/day5", "r")
numbers = [int(n) for n in f.readline().split(',')]
input = 5

n = 0
print(numbers)

def mode(mode, index):
    if mode == 0:
        return int(numbers[numbers[index]])
    elif mode == 1:
        return int(numbers[index])

while numbers[n] != 99:
    number = str(numbers[n])
    if len(number) > 1:
        opcode = int(number[-1:])
        first_mode_digit = int(number[-3:-2])
        if len(number) > 3:
            second_mode_digit = int(number[-4:-3])
        else:
            second_mode_digit = 0
    else:
        opcode = int(number)
        first_mode_digit = 0
        second_mode_digit = 0

    if opcode == 1:
        numbers[numbers[n+3]] = mode(first_mode_digit, n + 1) + mode(second_mode_digit, n + 2)
        n += 4

    elif opcode == 2:
        numbers[numbers[n+3]] = mode(first_mode_digit, n + 1) * mode(second_mode_digit, n + 2)
        n += 4

    elif opcode == 3:
        numbers[numbers[n + 1]] = input
        n += 2

    elif opcode == 4:
        print(mode(first_mode_digit, n + 1))
        n += 2

    elif opcode == 5:
        if mode(first_mode_digit, n + 1) != 0:
            n = mode(second_mode_digit, n + 2)
        else:
            n += 3

    elif opcode == 6:
        if mode(first_mode_digit, n + 1) == 0:
            n = mode(second_mode_digit, n + 2)
        else:
            n += 3

    elif opcode == 7:
        if mode(first_mode_digit, n + 1) < mode(second_mode_digit, n + 2):
            numbers[numbers[n + 3]] = 1
        else:
            numbers[numbers[n + 3]] = 0
        n += 4

    elif opcode == 8:
        if mode(first_mode_digit, n + 1) == mode(second_mode_digit, n + 2):
            numbers[numbers[n + 3]] = 1
        else:
            numbers[numbers[n + 3]] = 0
        n += 4


print("--- %s seconds ---" % (time.time() - start_time))