"""
--- Part Two ---

Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)
"""
import time

start_time = time.time()
f = open("../inputs/day6", "r")
planets = {}

def find_steps(middle_planet, destination):
    p = middle_planet
    steps = 0
    hz = True
    while hz:
        hz = False
        print(p)
        for j in planets[p]:
            print(j)
            if j in planets and destination in planets[j]:
                print(j)
                p = j
                steps += 1
                hz = True
                break
    return(steps)

for line in f.read().splitlines():
    first, second = line.split(')')
    if first in planets:
        planets[first].append(second)
    else:
        planets[first] = [second]

total = 0
for p in planets:
    for j in planets:
        if p in planets[j]:
            planets[j] = planets[j] + planets[p]

for p in planets:
    total += len(planets[p])

minim = total
middle_planet = ""

for p in planets:
    if ("YOU" in planets[p]) and ("SAN" in planets[p]):
        if len(planets[p]) < minim:
            minim = len(planets[p])
            middle_planet = p

steps = find_steps(middle_planet, "YOU") + find_steps(middle_planet, "SAN")

print(steps)

print("--- %s seconds ---" % (time.time() - start_time))