numbers = [
    'zero',
    'one', 
    'two', 
    'three', 
    'four', 
    'five', 
    'six', 
    'seven', 
    'eight', 
    'nine', 
    'ten', 
    'eleven', 
    'twelve',
    'thirteen', 
    'fourteen', 
    'fifteen', 
    'sixteen', 
    'seventeen', 
    'eighteen', 
    'nineteen',
    'twenty']

def get_minutes(minutes):
    if minutes == 1:
        return numbers[minutes] + ' minute'
    if minutes == 15:
        return 'quarter'
    if minutes <= 20:
        return numbers[minutes] + ' minutes'
    return 'twenty ' + numbers[minutes - 20] + ' minutes'

def get_time_in_words(hour, minutes):
    if minutes == '00':
        return numbers[hour] + ' o\' clock'
    if int(minutes) < 30:
        return get_minutes(int(minutes)) + ' past ' + numbers[hour]
    if minutes == '30':
        return 'half past ' + numbers[hour]
    return get_minutes(60 - int(minutes)) + ' to ' + numbers[hour + 1]

hour = int(raw_input())
minutes = raw_input()

print get_time_in_words(hour, minutes)

print get_time_in_words(5, '01')

