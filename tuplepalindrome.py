def is_palindrome(input_tuple):
    end_index = len(input_tuple) - 1
    start_index = 0

    while start_index < end_index:
        if input_tuple[start_index] != input_tuple[end_index]:
            return False

        start_index += 1
        end_index -= 1
    return True


numbers = (1,2,3,3,2,5)

if is_palindrome(numbers):
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome")