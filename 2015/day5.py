def contains_n_vowels(string, n=3):
    num_vowels = 0
    for c in string:
        if c in "aeiouAEIOU":
            num_vowels += 1
    return num_vowels >= n

def contains_repeated_letters(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False

def free_of_forbidden_strings(string, bad_strings):
    for bad_string in bad_strings:
        if bad_string in string:
            return False
    return True

def contains_repeated_letter_pairs(string):
    letter_pairs = []
    for i in range(len(string) - 1):
        letter_pairs.append(string[i] + string[i + 1])
    if len(letter_pairs) == len(set(letter_pairs)):
        return False
    else:
        return True

def contains_sandwich(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False

def is_nice(string):
    if not contains_repeated_letter_pairs(string):
        return False
    if not contains_sandwich(string):
        return False
    return True

if __name__ == '__main__':
    f = open('in5', 'r')

    nice_lines = 0
    for line in f:
        if is_nice(line):
            nice_lines += 1

    print "Nice lines:", nice_lines
