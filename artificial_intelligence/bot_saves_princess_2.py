#!/bin/python

def find_m_and_p(n, grid):
	m_position, p_position = 0, 0
	for row in xrange(n):
		for column in xrange(n):
			if grid[row][column] == 'm':
				m_position = (row, column)
			elif grid[row][column] == 'p':
				p_position = (row, column)
			if m_position and p_position:
				return m_position, p_position


def get_next_move(m_position, p_position):
	row_difference = m_position[0] - p_position[0]
	column_difference = m_position[1] - p_position[1]
	if row_difference < 0:
		vertical_shift = 'DOWN'
	else:
		vertical_shift = 'UP'
	if column_difference < 0:
		horizontal_shift = 'RIGHT'
	else:
		horizontal_shift = 'LEFT'

	if row_difference != 0:
		return vertical_shift
	if column_difference != 0:
		return horizontal_shift


def nextMove(n,r,c,grid):
	m_position, p_position = find_m_and_p(n, grid)
	return get_next_move(m_position, p_position)


n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
