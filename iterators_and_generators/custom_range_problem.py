class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current_number = self.start
            self.start += 1
            return current_number
        else:
            raise StopIteration

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
