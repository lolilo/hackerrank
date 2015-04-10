number_of_files = int(raw_input())
file_contents= []

files_that_pass_query1 = 0
files_that_pass_query2 = 0
files_that_pass_query3 = 0

def create_dict(num_array):
    dict = {}
    for num in num_array:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    return dict

for file in xrange(number_of_files): 
    file_description = [ int(x) for x in raw_input().split() ]
    file_content = file_description[1:]
    file_content = create_dict(file_content)
    file_contents.append(file_content)

def query_all(file, array):
    if len(file) < len(array):
        return 0
    for element in array:
        if (element in file) and (file[element] > 0):
            file[element] -= 1
        else:
            return 0
    return 1

def query_any(file, array):
    array = set(array)
    for element in array:
        if element in file:
            return 1
    return 0

def query_some(file, array):
    if query_any(file, array) and (query_all(file, array) == 0):
        return 1
    return 0 

def query_file(file, type_of_query, array):
    global files_that_pass_query1
    global files_that_pass_query2
    global files_that_pass_query3
    if type_of_query == 1:
        files_that_pass_query1 += query_all(file, array)
    if type_of_query == 2:
        files_that_pass_query2 += query_any(file, array)
    if type_of_query == 3:
        files_that_pass_query3 += query_some(file, array)

number_of_queries = int(raw_input())

for query in xrange(number_of_queries):
    query_description = [ int(x) for x in raw_input().split() ]
    type_of_query = query_description[0]
    elements_of_array = query_description[2:]

    for file in file_contents:
        file_copy = file.copy()
        query_file(file_copy, type_of_query, elements_of_array)

print files_that_pass_query1
print files_that_pass_query2
print files_that_pass_query3
