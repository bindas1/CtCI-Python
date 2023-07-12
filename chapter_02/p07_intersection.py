from linked_list import LinkedList


def get_size(linked_list):
    head = linked_list.head
    size = 0
    while head:
        head = head.next
        size += 1
    return size


def my_intersection(ll1, ll2):
    size_ll1 = get_size(ll1)
    size_ll2 = get_size(ll2)
    if size_ll1 >= size_ll2:
        longer = ll1
        shorter = ll2
    else:
        longer = ll2
        shorter = ll1
        
    longer_runner = longer.head
    shorter_runner = shorter.head
    
    for _ in range(abs(size_ll1 - size_ll2)):
        longer_runner = longer_runner.next
    
    while longer_runner and shorter_runner:
        if longer_runner == shorter_runner:
            return True
        longer_runner = longer_runner.next
        shorter_runner = shorter_runner.next
    
    return False


def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail

    # should be 1
    assert intersection(a, b).value == 1
    assert my_intersection(a, b).value == 1
