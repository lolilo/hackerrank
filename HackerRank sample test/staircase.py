height = int(raw_input())

def draw_staircase(height):
    current_height = 1
    while current_height <= height:
        empty = ' ' * (height - current_height)
        stairs = '#' * current_height
        print empty + stairs
        current_height += 1

draw_staircase(6)
