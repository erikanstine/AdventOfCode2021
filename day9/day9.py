def load_input(fn):
    with open(fn, 'r') as f:
        input_data = f.readlines()
    cleaned = [i.strip() for i in input_data]
    formatted = [[int(d) for d in r] for r in cleaned]
    return formatted

def find_local_minima(fn):
    input_data = load_input(fn)
    local_minima = []
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            # check neighbors
            curr = input_data[i][j]

            is_minimum = []

            if i != 0:
                is_minimum.append(input_data[i-1][j] > curr)
            if j != 0:
                is_minimum.append(input_data[i][j-1] > curr)
            if i != len(input_data) - 1:
                is_minimum.append(input_data[i+1][j] > curr)
            if j != len(input_data[i]) - 1:
                is_minimum.append(input_data[i][j+1] > curr)



            #print('Val {} at position [{},{}]:  {}'.format(input_data[i][j], i, j, is_minimum))

            if all(is_minimum):
                #local_minima.append(curr)
                local_minima.append([i, j])

    return local_minima, input_data


def get_basin_size(local_minimum, input_data, basin_coords=[]):
    i, j = local_minimum
    if input_data[i][j] == 9:
        return basin_coords
    if i != 0 and input_data[i-1][j] > input_data[i][j]:
        basin_coords = get_basin_size([i-1, j], input_data, basin_coords)
    if j != 0 and input_data[i][j-1] > input_data[i][j]:
        basin_coords = get_basin_size([i, j-1], input_data, basin_coords)
    if i != len(input_data) - 1 and input_data[i+1][j] > input_data[i][j]:
        basin_coords = get_basin_size([i+1, j], input_data, basin_coords)
    if j != len(input_data[i]) - 1 and input_data[i][j+1] > input_data[i][j]:
        basin_coords = get_basin_size([i, j+1], input_data, basin_coords)
    if local_minimum not in basin_coords:
        basin_coords.append(local_minimum)
    return basin_coords

def day9(fn='day9-test.txt'):
    local_minima, input_data = find_local_minima(fn)
    basin_sizes = []
    for m in local_minima:
        basin = get_basin_size(m, input_data, [])
        size = len(basin)
        basin_sizes.append(size)
        print('Basin found at point {}. Size: {}\nCoords: {}'.format(m, size, basin))
    basin_sizes = sorted(basin_sizes)[-3:]

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]



#def total_risk_level(fn='day9-test.txt'):
 #   local_minima = find_local_minima(fn)
  #  risk_levels = [i + 1 for i in local_minima]

   # return sum(risk_levels)

# Find basin size
    # Per low point, go horizontal/vertical while point height increases, not including 9
# Find 3 largest sizes and multiply

if __name__ == '__main__':
    #print('Total risk level: {}'.format(total_risk_level()))
    #print('Total risk level: {}'.format(total_risk_level('day9-input.txt')))
    print('3 Largest basins multiplied is {}'.format(day9('day9-input.txt')))



"""--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 535.

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

Your puzzle answer was 1122700."""
