def find_min(enter, exit, width_array):
    curr_min = 5
    for i in xrange(enter, exit + 1):
        if width_array[i] < curr_min:
            curr_min = width_array[i]
    return curr_min

def find_largest_vehicle(enter, exit, width_array):
    return find_min(enter, exit, width_array)


_, cases = [int(x) for x in raw_input().split()]
width_array = [int(x) for x in raw_input().split()]

for _ in xrange(cases):
    enter, exit = [int(x) for x in raw_input().split()]
    print find_largest_vehicle(enter, exit, width_array)
