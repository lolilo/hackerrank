#!/bin/python
# https://www.hackerrank.com/challenges/saveprincess


def displayPathtoPrincess(n, grid):
	m_position, p_position = find_m_and_p(n, grid)
	print_moves(m_position, p_position)


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


def print_moves(m_position, p_position):
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

	row_difference = abs(row_difference)
	column_difference = abs(column_difference)
	while row_difference > 0:
		print vertical_shift
		row_difference -= 1
	while column_difference > 0:
		print horizontal_shift
		column_difference -= 1


m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)
