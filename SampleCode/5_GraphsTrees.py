from collections import deque


class BinarySearchTree:
    class GraphNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __str__(self):
            return f"Data:{self.data}"

    def __init__(self):
        self.root_node = None

    def is_empty(self):
        return self.root_node is None

    def insert(self, data):
        n = BinarySearchTree.GraphNode(data)
        if self.is_empty():
            self.root_node = n
        else:
            curr = self.root_node
            parent = None
            while True:
                parent = curr
                if n.data < curr.data:
                    curr = curr.left
                    if not curr:
                        parent.left = n
                        return
                else:
                    curr = curr.right
                    if not curr:
                        parent.right = n
                        return

    def search(self, data):
        curr = self.root_node

        while True:
            if not curr:
                return None
            elif curr.data == data:
                return data
            elif curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

    def get_height(self):
        return self.__get_height__(self.root_node)

    def __get_height__(self, node):
        if node is None:
            return 0
        else:
            l = self.__get_height__(node.left)
            r = self.__get_height__(node.right)

            return max(l, r)+1

    def is_balanced(self):
        if self.root_node is None:
            return True
        lh = self.__get_height__(self.root_node.left)
        rh = self.__get_height__(self.root_node.right)
        return abs(lh - rh) < 2

    def get_node_with_parent(self, data):
        parent = None
        curr = self.root_node
        while curr:
            if curr.data == data:
                return parent, curr
            elif curr.data > data:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        return parent, curr

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if node is None:
            return False

        children = 0
        if node.left and node.right:
            children = 2
        elif node.left or node.right:
            children = 1

        if children == 0:
            if parent:
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root_node = None
        elif children == 1:
            next_n = None
            if node.left:
                next_n = node.left
            else:
                next_n = node.right

            if parent:
                if parent.left is node:
                    parent.left = next_n
                else:
                    parent.right = next_n
            else:
                self.root_node = next_n
        else:  # TWO CHILDREN
            left_parent = node
            leftmost_node = node.right
            while leftmost_node.left:
                left_parent = leftmost_node
                leftmost_node = leftmost_node.left

            node.data = leftmost_node.data

            if left_parent.left == leftmost_node:
                left_parent.left = leftmost_node.right
            else:
                left_parent.right = leftmost_node.right

    def in_order_recursive(self, node):
        curr = node
        if curr is None:
            return None
        self.in_order_recursive(curr.left)
        print(node.data)
        self.in_order_recursive(curr.right)

    def in_order_recursive_iter(self, node):
        curr = node
        if curr is None:
            return None
        yield from self.in_order_recursive_iter(curr.left)
        yield node.data
        yield from self.in_order_recursive_iter(curr.right)

    def in_order_stack(self):
        curr = self.root_node
        s = []
        while True:
            if curr is not None:  # WE'VE REACHED THE END OF THE LEFT SUBTREE
                s.append(curr)
                curr = curr.left
            elif len(s) > 0:
                curr = s.pop()
                print(curr.data)
                curr = curr.right
            else:
                break

    def in_order_stack_iter(self):
        curr = self.root_node
        s = []
        while True:
            if curr is not None:  # WE'VE REACHED THE END OF THE LEFT SUBTREE
                s.append(curr)
                curr = curr.left
            elif len(s) > 0:
                curr = s.pop()
                yield curr.data
                curr = curr.right
            else:
                break

    def pre_order_recursive(self, node):
        curr = node
        if curr is None:
            return None
        print(node.data)
        self.in_order_recursive(curr.left)
        self.in_order_recursive(curr.right)

    def post_order_recursive(self, node):
        curr = node
        if curr is None:
            return None
        self.in_order_recursive(curr.left)
        self.in_order_recursive(curr.right)
        print(node.data)

    def post_order_recursive_iter(self, node):
        curr = node
        if curr is None:
            return None
        yield from self.in_order_recursive_iter(curr.left)
        yield from self.in_order_recursive_iter(curr.right)
        yield node.data

    def breadth_first_search_traversal(self):
        queue = deque()
        queue.append(self.root_node)

        while len(queue) > 0:
            node = queue.popleft()
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()

    insert = [7, 5, 10, 8, 15, 17, 12, 11, 13, 11.5]

    for e in insert:
        bst.insert(e)

    bst.remove(10)

    print("STARTING IN ORDER TRAVERSAL...")
    for data in bst.in_order_recursive_iter(bst.root_node):
        print(f"Do something with {data}")

    print("STARTING POST ORDER TRAVERSAL...")
    for data in bst.post_order_recursive_iter(bst.root_node):
        print(f"Do something with {data}")
