def create_tree(num_nodes):
    tree = {}
    num_edges = num_nodes - 1
    for edge in xrange(num_edges):
        first, second = [int(x) for x in raw_input().split()]
        if tree.get(first):
            tree[first].append(second)
        else:
            tree[first] = [second]
    return tree


def has_odd_children(node, tree, children_count):
    if not tree.get(child): 
        return 1 if children_count % 2 != 0 else 0
    for child in tree.get(child):
        return 


def get_even_number_distance_count(tree):
    even_count = 0
    for node in tree.keys():
        even_count += paths_with_even_children(child, tree, 0):
    return even_count


cases = int(raw_input())

for case in xrange(cases):
    num_nodes = int(raw_input())
    tree = create_tree(num_nodes)
    print tree
    even_number_distance_count = get_even_number_distance_count(tree)
    print even_number_distance_count

