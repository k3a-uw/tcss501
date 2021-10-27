class Queue:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def enqueue(self, data):
        n = Queue.QueueNode(data)
        if self.top is None:  # EMPTY
            self.top = n
            self.bottom = n
        else:
            self.bottom.prev = n
            n.next = self.bottom
            self.bottom = n
        self.size += 1

    def dequeue(self):
        ret = self.top

        if self.size == 1:
            self.top = None
            self.bottom = None
        elif self.size > 1:
            self.top = self.top.prev
            self.top.next = None

        if self.size >= 1:
            self.size -= 1
            return ret.data


class Stack:
    class StackNode:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        n = Stack.StackNode(data)
        if self.is_empty():
            self.top = n
        else:
            n.next = self.top
            self.top = n

        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            r = self.top
            self.top = self.top.next

        self.size -= 1
        return r.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data


class StackQueue:
    def __init__(self):
        self.inbound = Stack()
        self.outbound = Stack()

    def enqueue(self, data):
        self.inbound.push(data)
        self.size += 1

    def dequeue(self):
        if self.outbound.is_empty():
            while not self.inbound.is_empty():
                self.outbound.push(self.inbound.pop())

        if self.outbound.is_empty():
            return None
        else:
            self.size -= 1
            return self.outbound.pop()


def check_brackets(n):
    s = Stack()
    for c in n:
        if c in ('{', '[', '('):
            s.push(c)
        if c in ('}', ']', ')'):
            l = s.pop()
            if l == '{' and c == '}':
                continue
            elif l == '[' and c == ']':
                continue
            elif l == '(' and c == ')':
                continue
            else:
                return False

    return s.is_empty()




if __name__ == "__main__":
    print("Demonstration of Stacks vs Queues")

    my_stack = Stack()
    my_queue = Queue()

    words_to_add = ['Four', 'Score', 'and Seven', 'Years Ago']

    for word in words_to_add:
        print(f"Adding {word}")
        my_stack.push(word)
        my_queue.enqueue(word)


    print("\n\nShowing Stack...")
    while not my_stack.is_empty():
        v = my_stack.pop()
        print(f"Element: {v}")

    print("\n\nDequeing...")
    while not my_queue.size == 0:
        x = my_queue.dequeue()
        print(f"Element: {x}")


    my_stack.push("Hello")
    my_stack.push("World")
