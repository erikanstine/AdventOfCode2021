import re
import numpy as np


def clean_coords(coords):
    coords = [l.strip() for l in coords]
    clean = []
    for coord in coords:
        coord_regex = r'(\d+),(\d+) -> (\d+),(\d+)'
        matches = re.search(coord_regex, coord)
        a, b, c, d = matches.groups()
        clean.append([[int(a), int(b)],[int(c), int(d)]])

    return clean


def load_input(fn):
    with open(fn, 'r') as f:
        coords = f.readlines()

    return clean_coords(coords)

# Given coord pair, return list of points
def find_line_coords(coord):
    x_min = min(coord[0][0], coord[1][0])
    x_max = max(coord[0][0], coord[1][0])
    y_min = min(coord[0][1], coord[1][1])
    y_max = max(coord[0][1], coord[1][1])

    x_range = [n for n in range(x_min, x_max + 1)]
    y_range = [n for n in range(y_min, y_max + 1)]
    x_range *= len(y_range)
    y_range *= len(x_range)
    #print(x_range)
    #print(y_range)
    #print(zip(x_range, y_range))
    return zip(x_range, y_range)

def find_line_coords_diagonal(coord):
    x1, y1 = coord[0]
    x2, y2 = coord[1]

    if x1 > x2:
        x_range = [n for n in range(x1, x2 - 1, -1)]
    else:
        x_range =[n for n in range(x1, x2 + 1)]

    if y1 > y2:
        y_range = [n for n in range(y1, y2 - 1, -1)]
    else:
        y_range =[n for n in range(y1, y2 + 1)]
    coords = zip(x_range, y_range)
    print(coords)
    return coords

def map_single_vent(coord, v_map):
    x1, y1 = coord[0]
    x2, y2 = coord[1]
    # For now ignore diagonals
    if not (x1 == x2 or y1 == y2):
        return v_map
    updated_map = v_map
    line_coords = find_line_coords(coord)
    for c in line_coords:
        updated_map[c[1]][c[0]] += 1
        #print(''.join([str(x) for x in updated_map]))
    return updated_map


def map_single_vent_part_2(coord, v_map):
    x1, y1 = coord[0]
    x2, y2 = coord[1]

    if not (x1 == x2 or y1 == y2):
        line_coords = find_line_coords_diagonal(coord)
    else:
        line_coords = find_line_coords(coord)
    updated_map = v_map
    for c in line_coords:
        updated_map[c[1]][c[0]] += 1
        #print(''.join([str(x) for x in updated_map]))
    return updated_map

def print_map(m):
    for i in m:
        print(''.join([str(x) for x in i]))

def map_vents(coords, size):
    vent_map = np.zeros((size, size), dtype=int)

    for c in coords:
        vent_map = map_single_vent_part_2(c, vent_map)
        #print_map(vent_map)

    #print_map(vent_map)
    print('Num points greater than 1: ', count_multiples(vent_map))
    return count_multiples(vent_map)

def count_multiples(vent_map):
    return np.count_nonzero(vent_map > 1)


if __name__ == "__main__":
    #map_vents(load_input('day5-test.txt'), 10)
    map_vents(load_input('day5-input.txt'), 1000)


"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Your puzzle answer was 6856.

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

Your puzzle answer was 20666."""
