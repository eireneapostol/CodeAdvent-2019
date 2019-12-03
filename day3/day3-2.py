"""
--- Part Two ---

It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?


"""


import time


start_time = time.time()
f = open("../inputs/day3", "r")

wire1_init = f.readline()
wire2_init = f.readline()

def create_wire(wire_init):
    wire = [(0, 0)]
    for direction in wire_init.split(","):
        for i in range(int(direction[1:])):
            if direction[0] == "R":
                wire.append((wire[-1][0], wire[-1][1] + 1))
            elif direction[0] == "L":
                wire.append((wire[-1][0], wire[-1][1] - 1))
            elif direction[0] == "U":
                wire.append((wire[-1][0] + 1, wire[-1][1]))
            elif direction[0] == "D":
                wire.append((wire[-1][0] - 1, wire[-1][1]))
    return wire

wire1_list = create_wire(wire1_init)
wire2_list = create_wire(wire2_init)

wire1 = set(wire1_list)
wire2 = set(wire2_list)

intersections = list(wire1.intersection(wire2))

minim = wire1_list.index(intersections[0]) + wire2_list.index(intersections[0])
for n in intersections:
    if (wire1_list.index(n) + wire2_list.index(n)) < minim and (wire1_list.index(n) + wire2_list.index(n)) != 0 :
        minim = wire1_list.index(n) + wire2_list.index(n)

print(minim)

print("--- %s seconds ---" % (time.time() - start_time))
