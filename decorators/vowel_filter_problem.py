def vowel_filter(function):

    def wrapper():
        letters = function()
        vowels = ['a', 'e', 'i', 'o', 'u']
        filtered_letters = [l for l in letters if l in vowels]
        return filtered_letters
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
