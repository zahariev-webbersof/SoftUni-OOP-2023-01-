class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data) - 1, -1, -1)]) + "]"