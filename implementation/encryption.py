import math

def get_rows_and_columns(msg):
    len_msg = len(msg)

    sqrt_len_msg = math.sqrt(len_msg)
    min_len = int(math.floor(sqrt_len_msg))
    max_len = int(math.ceil(sqrt_len_msg))

    rows, columns = min_len, min_len
    while (rows * columns) < len_msg:
        if rows == columns:
            columns += 1
        else:
            rows += 1
    return rows, columns

# def create_grid(msg, rows, columns):
#     grid = []
#     row_index = 0
#     for char in msg:
#         if row_index < rows:

#     return grid

def get_every_nth_char(start_index, msg, n):
    curr_index = start_index
    len_msg = len(msg)
    new_word = ''
    while curr_index < len_msg:
        new_word += msg[curr_index]
        curr_index += n
    return new_word

def get_encrption(msg, rows, columns):
    encrption_string = ''
    for i in xrange(columns):
        start_index = i
        new_word = get_every_nth_char(start_index, msg, columns)
        encrption_string += new_word + ' '
    return encrption_string

def encrption(msg):
    rows, columns = get_rows_and_columns(msg)
    # grid = create_grid(msg, rows, columns)
    print get_encrption(msg, rows, columns)

# encrption('haveaniceday')
encrption('chillout')

# msg = raw_input()
# encrption(msg)
