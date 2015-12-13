class Board(object):
    def __init__(self):
        self.size = 10
        self.board = self.get_graph()

    def get_board(self):
        board = [[0] * self.size for i in xrange(self.size)]
        num = 1
        row_num = 0
        while num < self.size ** 2 + 1:
            row_index = 0
            while row_index < self.size:
                board[row_num][row_index] = num
                row_index += 1
                num += 1
            row_num += 1
        return board

    def get_graph(self):
        graph = {}
        num = 1
        while num < self.size ** 2:
            graph[num] = [num + 1]
            num += 1
        return graph

    def mark_ladder(self, ladder_starting_point, ladder_ending_point):
        self.board[ladder_starting_point].append(ladder_ending_point)

    def mark_snake(self, snake_starting_point, snake_ending_point):
        self.board[snake_starting_point].append(snake_ending_point)


# playing_board = Board()
# cases = int(raw_input())
# for case in xrange(cases):
#     num_ladders = int(raw_input())
#     for i in xrange(num_ladders):
#         ladder_starting_point, ladder_ending_point = [int(x) for x in raw_input().split()]
#         playing_board.mark_ladder(ladder_starting_point, ladder_ending_point)
#     num_snakes = int(raw_input())
#     for i in xrange(num_snakes):
#         snake_starting_point, snake_ending_point = [int(x) for x in raw_input().split()]
#         playing_board.mark_snake(snake_starting_point, snake_ending_point)
#     print playing_board.board


