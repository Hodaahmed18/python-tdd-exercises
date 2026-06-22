def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_initials(name):
    names = name.split()

    first_initial = names[0][0]
    second_initial = names[1][0]

    return first_initial + second_initial


def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count


def filter_even_numbers(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False
