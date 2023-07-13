from linked_list import LinkedList


def has_loop(head, hash_map):
    if not head:
        return False, _
    else:
        if head in hash_map:
            return True, head
        else:
            hash_map[head] = None
            return has_loop(head.next, hash_map)


def my_loop_detection(ll):
    loop_exists, head = has_loop(ll.head, {})
    if not loop_exists:
        return None
    else:
        return head


def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected
        assert my_loop_detection(ll) == expected
