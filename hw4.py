# PART A
"""
Q1
"""
def fibonacci_chars(n, k):  #  wrapper function
    return fibonacci_chars_rec(n)[k]  # returns the char at index k of the chars fibonacci string

def fibonacci_chars_rec(n):  # returns the chars fibonacci of n length
    if n == 0:  # first value of the sequence
        return 'a'
    if n == 1:  # second value of the sequence
        return 'bc'
    return fibonacci_chars_rec(n - 2) + fibonacci_chars_rec(n - 1)  # recursive classic fibonacci calculate

# PART B
"""
Q2
"""
def len_of_list(lst):  # instrumental method that recursively calculates length of a list
    if not lst:
        return 0
    return 1 + len_of_list(lst[1:])

def drainage_basins(elevation_histogram): # wrapper function
    return drainage_basins_rec(elevation_histogram, 0, len_of_list(elevation_histogram))

def drainage_basins_rec(elevation_histogram, first_index, original_len_of_list):
    # first_index - first element of elevation histogram list in the current recursion stage
    # original_len_of_list - length of the original elevation histogram list
    if len_of_list(elevation_histogram) == 1:  #  in case that the original list has 1 value.
        return []
    if original_len_of_list == 2:  # in case that the original list has 2 value.
        if elevation_histogram[0] < elevation_histogram[1]:  # if the first value is smaller than the second it is the drainage basin.
            return [0]
        elif elevation_histogram[1] < elevation_histogram[0]:  # if the second value is smaller than the first it is the drainage basin.
            return [1]
        else:  # in case they are even
            return []
    if first_index == 0:  # first value of the original list.
        if elevation_histogram[0] < elevation_histogram[1]:  # first value of a list (bigger than 2) is a drainage basin if the second is smaller.
            return [0] + drainage_basins_rec(elevation_histogram[1:], first_index + 1, original_len_of_list)  # recursive call to find all the rest of the basins further down the list.
    if first_index == original_len_of_list - 2:  # one value before the last value of the original list.
        if elevation_histogram[1] < elevation_histogram[0]:  # last value of a list (bigger than 2) is a drainage basin if its smaller to his previous.
            return [original_len_of_list - 1]  # returns the index of the basin (last value) as a list.
    if elevation_histogram[0] > elevation_histogram[1] and elevation_histogram[2] > elevation_histogram[1]:  # checks if value that has "neighbors" is a basin (smaller than them).
        return [first_index + 1] + drainage_basins_rec(elevation_histogram[2:], first_index + 2, original_len_of_list)  # returns the index of the basin as a list chained to the rest of the basins indexes (located further down the list).
    return drainage_basins_rec(elevation_histogram[1:], first_index + 1, original_len_of_list)  # returns the rest of the basins indexes (located further down the list).

# PART C
"""
Q1
"""
def is_legit_track(grid, i1, j1, i2, j2, current_weight):
    if (abs(i1 - i2) == 1 and (j1 - j2) == 0) or ((i1 - i2) == 0 and abs(j1 - j2) == 1):  # checks if movement is in one direction.
        return current_weight + grid[i2][j2] < 2 * grid[i2][j2]  # checks if player carry too much weight.
    return False

"""
Q2
"""
def get_number_legit_tracks(grid, i1, j1):  # wrapper function that adds 'current_weight' to original parameters.
    return get_number_legit_tracks_rec(grid, i1, j1, 0)

def get_number_legit_tracks_rec(grid, i1, j1, current_weight):
    if i1 == len(grid) -1 and j1 == len(grid[0]) - 1:  # if player reached end point.
        return 1
    num_of_tracks = 0  # tracks counter.
    if i1 + 1 < len(grid):  # getting out of the board is not a track.
        if is_legit_track(grid, i1, j1, i1 + 1, j1, current_weight + grid[i1][j1]):  # checks whether move is legit or not using previous function.
            num_of_tracks += get_number_legit_tracks_rec(grid, i1 + 1, j1, current_weight + grid[i1][j1])  # sums all legit tracks that can be reached from this move.
    if j1 + 1 < len(grid[0]):  # getting out of the board is not a track.
        if is_legit_track(grid, i1, j1, i1, j1 + 1, current_weight + grid[i1][j1]):  # checks whether move is legit or not using previous function.
            num_of_tracks += get_number_legit_tracks_rec(grid, i1, j1 + 1, current_weight + grid[i1][j1])  # sums all legit tracks that can be reached from this move.
    if i1 > 0:  # getting out of the board is not a track.
        if is_legit_track(grid, i1, j1, i1 - 1, j1, current_weight + grid[i1][j1]):  # checks whether move is legit or not using previous function.
            num_of_tracks += get_number_legit_tracks_rec(grid, i1 - 1, j1, current_weight + grid[i1][j1])  # sums all legit tracks that can be reached from this move.
    if j1 > 0:  # getting out of the board is not a track.
        if is_legit_track(grid, i1, j1, i1, j1 - 1, current_weight + grid[i1][j1]):  # checks whether move is legit or not using previous function.
            num_of_tracks += get_number_legit_tracks_rec(grid, i1, j1 - 1, current_weight + grid[i1][j1])  # sums all legit tracks that can be reached from this move.
    return num_of_tracks

# PART D
"""
Q1
"""
def optimize_flowers_selection(flowers, budget):  # wrapper function
    return optimize_flowers_selectio_rec(flowers, budget, 0)

def optimize_flowers_selectio_rec(flowers, budget, aesthetic_res):
    # aesthetic_res represents level of aesthetic we reached until current stage of recursion.
    if budget < 0:  # if there is a budget overrun.
        return -1,0  # return negative value of aesthetic (that wouldn't be selected if lower than 0).
    if not flowers:  # means that there is no more to take/not to take.
        return aesthetic_res, budget
    take_option = optimize_flowers_selectio_rec(flowers[1:], budget - flowers[0][2], aesthetic_res + flowers[0][1])  # calculates the option of taking the first flower on the flowers list.
    not_take_option = optimize_flowers_selectio_rec(flowers[1:], budget, aesthetic_res)  # calculates the option of not taking the first flower on the flowers list.
    if take_option[0] > not_take_option[0]:  # checks which option is better
        return take_option  # returns the better option.
    return not_take_option  # returns the better option.

"""
Q2
"""
def get_plants_to_buy_faster(flowers, budget):  # wrapper function
    return get_plants_to_buy_faster_rec(flowers, budget, 0, {})

def get_plants_to_buy_faster_rec(flowers, budget, aesthetic_res, flower_buy_dict):
    # aesthetic_res is same as it is on optimize_flowers_selectio_rec.
    # flower_buy_dict is a dictionary that saves results of optimize_flowers_selectio_rec and prevents recalculatings.
    if budget < 0:  # same as it is on optimize_flowers_selectio_rec.
        return -1, 0  # same as it is on optimize_flowers_selectio_rec.
    if not flowers:  # same as it is on optimize_flowers_selectio_rec.
        return aesthetic_res, budget  # same as it is on optimize_flowers_selectio_rec.
    key = (aesthetic_res, budget)  # uses tuples of aesthetic level and budget as keys of the dictionary.
    if key not in flower_buy_dict:  # checks whether calculated before.
        take_option = get_plants_to_buy_faster_rec(flowers[1:], budget - flowers[0][2], aesthetic_res + flowers[0][1], flower_buy_dict)  # same as it is on optimize_flowers_selectio_rec.
        not_take_option = get_plants_to_buy_faster_rec(flowers[1:], budget, aesthetic_res, flower_buy_dict)  # same as it is on optimize_flowers_selectio_rec.
        if take_option[0] > not_take_option[0]:  # same as it is on optimize_flowers_selectio_rec.
            flower_buy_dict[key] = take_option  # inserts the better option to the dictionary.
        else:
            flower_buy_dict[key] = not_take_option  # inserts the better option to the dictionary.
    return flower_buy_dict[key]  # returns the better option.