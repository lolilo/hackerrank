# Enter your code here. Read input from STDIN. Print output to STDOUT
original_time = raw_input()
# original_time = '06:40:03AM'
                
def is_twelve_hour(time):
    return time[:2] == '12'

def get_converted_hour(orignal_time):
    converted_hour = int(original_time[:2])
    isAM = original_time[-2] == 'A'

    if not isAM and not is_twelve_hour(orignal_time):
        converted_hour += 12
    elif isAM and is_twelve_hour(orignal_time):
        converted_hour = 0

    return '00' if converted_hour == 0 else str(converted_hour).zfill(2)

def get_converted_time(original_time):
    converted_hour = get_converted_hour(original_time)
    return converted_hour + original_time[2:-2]

print get_converted_time(original_time)
