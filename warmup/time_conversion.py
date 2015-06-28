# Enter your code here. Read input from STDIN. Print output to STDOUT
original_time = raw_input()
                
def is_twelve_hour(time):
    return time[:2] == '12'

def get_converted_hour(orignal_time):
    orignal_hour = int(original_time[:2])
    return str(orignal_hour + 12)

def get_converted_time(original_time):
    isAM = original_time[-2] == 'A'
    
    if isAM:
        if is_twelve_hour(original_time):
            return '00' + original_time[2:-2]
        return original_time[:-2]    

    # isPM
    if is_twelve_hour(original_time):
        return original_time[:-2]
    converted_hour = get_converted_hour(original_time)
    return converted_hour + original_time[2:-2]

print get_converted_time(original_time)
