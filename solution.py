class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


def is_balanced(sequence):
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            if stack.peek() != matching[char]:
                return False
            stack.pop()
        # остальные символы игнорируем

    return stack.is_empty()


def main():
    user_input = input("Введите строку со скобками: ")
    if is_balanced(user_input):
        print("Balanced")          # <-- ИЗМЕНЕНО (было "Сбалансированно")
    else:
        print("Unbalanced")        # <-- ИЗМЕНЕНО (было "Несбалансированно")


if __name__ == "__main__":
    main()