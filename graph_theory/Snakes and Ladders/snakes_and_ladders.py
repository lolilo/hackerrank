def get_graph(size):
    graph = {}
    num = 1
    while num < size ** 2:
        graph[num] = [num + 1]
        num += 1
    return graph


def mark_edge(starting_point, ending_point):
    graph[starting_point].append(ending_point)


def get_minimum_dice_rolls():
    dice_roll_count = 0
    for node in graph.keys():
        next_node = max(graph[node])
        dice_roll_count += 1


graph = get_graph(10)
cases = int(raw_input())
for case in xrange(cases):
    num_ladders = int(raw_input())
    for i in xrange(num_ladders):
        ladder_starting_point, ladder_ending_point = [int(x) for x in raw_input().split()]
        mark_edge(ladder_starting_point, ladder_ending_point)
    num_snakes = int(raw_input())
    for i in xrange(num_snakes):
        snake_starting_point, snake_ending_point = [int(x) for x in raw_input().split()]
        mark_edge(snake_starting_point, snake_ending_point)

    print get_minimum_dice_rolls()

    print graph

