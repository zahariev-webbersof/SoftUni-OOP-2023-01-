def reverse_text(text):
    for char in reversed(text):
        yield char


for char in reverse_text("step"):
    print(char, end='')
