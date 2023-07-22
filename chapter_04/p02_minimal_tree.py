class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.val}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()


def create_bst(array):
    match len(array):
        case 0:
            return None
        case 1:
            return Node(array[0])
        case _:
            mid = len(array) // 2
            root_node = Node(array[mid])
            root_node.left = create_bst(array[:mid])
            root_node.right = create_bst(array[mid+1:])
            return root_node


def array_to_binary_tree(array, start, end):
    if start > end:
        return None
    mid = (
        start + end
    ) // 2  # This must be floor division, otherwise you get a slice error
    # TypeError: list indices must be integers or slices, not float
    root = Node(array[mid])
    root.left = array_to_binary_tree(array, start, mid - 1)
    root.right = array_to_binary_tree(array, mid + 1, end)
    return root


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    print(array_to_binary_tree(test_array, 0, len(test_array) - 1))
