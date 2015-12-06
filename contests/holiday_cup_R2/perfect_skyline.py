def detect_perfect(len_skyline, skyline):
    if len_skyline % 2 == 0:
        return 'Not perfect'
    for building_index in xrange(1, len_skyline / 2):
        previous_height = skyline[building_index - 1]
        if skyline[building_index] != skyline[-(building_index + 1)] or previous_height >= skyline[building_index]:
            return 'Not perfect'
    if skyline[len_skyline / 2] > skyline[len_skyline / 2 - 1] or len_skyline == 1:
        return 'Perfect'
    else:
        return 'Not perfect'

n = int(raw_input().strip())
H = map(int,raw_input().strip().split(' '))

print detect_perfect(n, H)
