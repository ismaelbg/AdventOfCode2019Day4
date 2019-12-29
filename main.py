def find_passwords(current_number, ending_number):
    possible_passwords = 0
    while current_number <= ending_number:
        string_number = str(current_number)
        there_is_double = False
        number_is_increasing = True
        i = 1
        while i < len(string_number) and number_is_increasing:
            current_digit = int(string_number[i])
            prev_digit = int(string_number[i-1])
            if current_digit == prev_digit:
                there_is_double = True
            if current_digit < prev_digit:
                number_is_increasing = False
            i = i + 1
        if (number_is_increasing and there_is_double):
            possible_passwords = possible_passwords + 1
        current_number = current_number + 1
    return possible_passwords


input = "236491 - 713787"
input = input.split("-")

current_number = int(input[0])
ending_number = int(input[1])

print("Result of part 1:", find_passwords(current_number,ending_number))