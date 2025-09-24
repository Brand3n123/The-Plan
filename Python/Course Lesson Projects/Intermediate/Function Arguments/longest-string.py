def longest_string(**strings):
    longest_string = ''
    for string in strings.values():
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

print(longest_string(string1 = "hello", string2 = "thomas", string3 =  "margaritas", string4 = "bob"))