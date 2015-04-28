def look_and_say(n):
    if n == 0:
        return '1'
    return next_look_and_say_number(look_and_say(n - 1))

def next_look_and_say_number(n):
    previous_digit = n[0]
    occurrences = 1
    result = ''
    for i, digit in enumerate(n[1:]):
        if previous_digit == digit:
            occurrences += 1
        else:
            result += str(occurrences) + previous_digit
            occurrences = 1
            previous_digit = digit
    result += str(occurrences) + previous_digit
    return result

print look_and_say(5)
