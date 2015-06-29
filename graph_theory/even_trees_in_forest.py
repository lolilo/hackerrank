import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.graph_simple = {
            1: set([2]),
            2: set([1])
        }
        self.graph = {
            1: set([2, 3, 6]), 
            2: set([1, 5, 7]), 
            3: set([1, 4]), 
            4: set([3]), 
            5: set([2]), 
            6: set([8, 1]), 
            7: set([2]), 
            8: set([9, 10, 6]), 
            9: set([8]), 
            10: set([8])
        }
        self.graph_2 = {
            1: set([8, 19, 2, 3, 7]), 
            2: set([1, 5, 9]), 
            3: set([1, 4, 12]), 
            4: set([3]), 
            5: set([2, 6]), 
            6: set([16, 17, 5]), 
            7: set([1, 10, 13]), 
            8: set([1, 20, 14]), 
            9: set([2]), 
            10: set([18, 11, 7]), 
            11: set([10]), 
            12: set([3, 15]), 
            13: set([7]), 
            14: set([8]), 
            15: set([12]), 
            16: set([6]), 
            17: set([6]), 
            18: set([10]), 
            19: set([1]), 
            20: set([8])
        }

    def test_is_root_of_even_subtree(self):
        self.assertEqual(is_root_of_even_subtree(self.graph_simple, 1, 2), False)
        self.assertEqual(is_root_of_even_subtree(self.graph, 1, 2), False)

    def test_create_even_trees(self):
        self.assertEqual(create_even_trees(self.graph), 2)
        self.assertEqual(create_even_trees(self.graph_2), 4)


def add_nodes_to_graph(graph, node1, node2):
    if graph.get(node1):
        graph[node1].add(node2)
    else:
        graph[node1] = set([node2])

    if graph.get(node2):
        graph[node2].add(node1)
    else:
        graph[node2] = set([node1])
    return graph


def parse_graph(edges_count):
    graph = {} # keys = int, value = set
    for edge in xrange(edges_count):
        node1, node2 = [int(x) for x in raw_input().split()]
        graph = add_nodes_to_graph(graph, node1, node2)
    return graph


def is_root_of_even_subtree(graph, parent, node):
    #dfs
    children_count = 0
    stack = [node]
    visited = set([parent, node])
    while stack:
        current_node = stack.pop()
        for next in graph[current_node] - visited:
            children_count += 1
            visited.add(next)
            stack.append(next)
    return children_count % 2 != 0 if children_count > 0 else False


def create_even_trees(graph):
    removed_edges_count = 0
    for node in graph.keys():
        next_node_set = graph[node].copy()
        for next in next_node_set:
            if is_root_of_even_subtree(graph, node, next):
                graph[node].remove(next)
                graph[next].remove(node)
                removed_edges_count += 1
    return removed_edges_count


def hackerrank():
    vertices_count, edges_count = [int(x) for x in raw_input().split()]
    graph = parse_graph(edges_count)
    print create_even_trees(graph)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
    # hackerrank()

# Try counting the children. 
# If the subtree has even number of nodes then the edge leading to this subtree can be removed. 
# Otherwise, you have to keep on searching until you find a suitable edge or the entire tree exhausted. 
# As it always can be decomposed into forests of even number of nodes, 
# you will always end up with an answer greater than 1.
