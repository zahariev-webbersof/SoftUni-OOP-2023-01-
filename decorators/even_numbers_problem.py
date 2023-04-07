def even_numbers(function):

    def wrapper(numbers):
        numbers_list = function(numbers)
        even_numbers_list = [num for num in numbers_list if num % 2 == 0]
        return even_numbers_list
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
