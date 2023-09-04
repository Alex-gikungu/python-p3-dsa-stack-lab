class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full. Cannot push item.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty. Cannot pop item.")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise ValueError("Stack is empty. Cannot peek.")

    def size(self):
        return len(self.items)

    def empty(self):
        return self.isEmpty()

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.items.index(target)
        else:
            return -1
