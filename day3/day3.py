
with open('day3.txt', 'r') as f:
    input_array = f.readlines()
    input_array = [s.strip() for s in input_array]

def get_most_common_for_idx(idx, input_array, default):
    print('Finding most common for idx {}'.format(idx))
    single_idx_array = [i[idx] for i in input_array]
    count_0 = ''.join(single_idx_array).count('0')
    count_1 = ''.join(single_idx_array).count('1')
    if count_0 == count_1:
        return default
    if count_0 > count_1:
        return '0'
    return '1'

def get_least_common_for_idx(idx, input_array, default):
    print('Finding Least common for idx {}'.format(idx))
    single_idx_array = [i[idx] for i in input_array]
    count_0 = ''.join(single_idx_array).count('0')
    count_1 = ''.join(single_idx_array).count('1')
    if count_0 == count_1:
        return default
    if count_0 < count_1:
        return '0'
    return '1'

def swap_binary(b):
    new_str = ''
    for c in b:
        if c == '0':
            new_str += '1'
        else:
            new_str += '0'
    return new_str


def solve_part_1(input_array):
    gamma = ''
    for i in range(len(input_array[0])):
        gamma += get_most_common_for_idx(i, input_array, '1')

    epsilon = swap_binary(gamma)
    print('Gamma: ', gamma)
    print('Epsilon: ', epsilon)
    print('Gamma * Epsilon: ', (int(gamma, 2) * int(epsilon, 2)))

def whittle_down(idx, prev_array, default):
    if default == '1':
        bit_filter = get_most_common_for_idx(idx, prev_array, default)
    else:
        bit_filter = get_least_common_for_idx(idx, prev_array, default)
    new_arr = [b for b in prev_array if b[idx] == bit_filter]
    print('Old length: {}\nNew length: {}'.format(len(prev_array), len(new_arr)))
    return new_arr


def find_o_rating(input_array):
    o_rating_arr = input_array
    while len(o_rating_arr) > 1:
        for i in range(len(input_array[0])):
            if len(o_rating_arr) == 1:
                break
            o_rating_arr = whittle_down(i, o_rating_arr, '1')
    return o_rating_arr[0]

def find_c_rating(input_array):
    c_rating_arr = input_array
    while len(c_rating_arr) > 1:
        for i in range(len(input_array[0])):
            if len(c_rating_arr) == 1:
                break
            c_rating_arr = whittle_down(i, c_rating_arr, '0')
    return c_rating_arr[0]


def solve_part_2(input_array):
    o_rating = find_o_rating(input_array)
    c_rating = find_c_rating(input_array)

    print('O2 Generator Rating: ', o_rating)
    print('CO2 Scrubber Rating: ', c_rating)
    print('Life Support Rating: ', (int(o_rating, 2) * int(c_rating, 2)))





if __name__ == "__main__":
    #solve_part_1(input_array)
    solve_part_2(input_array)
    #print(find_o_rating(input_array))
    #print(get_most_common_for_idx(0, input_array, '1'))
