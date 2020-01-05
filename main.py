def find_passwords_part1(current_number, ending_number):
    possible_passwords = []
    number_of_possible_passwords = 0
    while current_number <= ending_number:
        string_number = str(current_number)

        if len(string_number) < 2:
            raise Exception('Numbers must be formed by more than 1 digit')

        there_is_double = False
        number_decreasing = False
        i = 0
        while i < (len(string_number) - 1) and not number_decreasing:
            current_digit = int(string_number[i])
            next_digit = int(string_number[i+1])

            if current_digit == next_digit:
                there_is_double = True
            if current_digit > next_digit:
                number_decreasing = True

            i = i + 1
        if not number_decreasing and there_is_double:
            number_of_possible_passwords = number_of_possible_passwords + 1
            possible_passwords.append(current_number)
        current_number = current_number + 1
    return number_of_possible_passwords, possible_passwords


def find_passwords_part2(possible_passwords):
    number_of_possible_passwords = 0
    for current_number in possible_passwords:
        string_number = str(current_number)
        i = 0
        possible_password = False
        while i < (len(string_number) - 1):
            digit = string_number[i]
            i = i + 1
            next_digit = string_number[i]
            counter = 0
            while digit == next_digit:
                counter = counter + 1
                if i < (len(string_number) - 1):
                    i = i + 1
                    next_digit = string_number[i]
                else:
                    break
            if counter == 1:
                possible_password = True
        if possible_password:
            number_of_possible_passwords = number_of_possible_passwords + 1
    return number_of_possible_passwords


input = "236491-713787"
input = input.split("-")

current_number = int(input[0])
ending_number = int(input[1])

number_of_passwords_part1, list_possible_passwords = find_passwords_part1(current_number, ending_number)
print("Result of part 1:", number_of_passwords_part1)
print("Result of part 2:", find_passwords_part2(list_possible_passwords))