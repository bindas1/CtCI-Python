from chapter_02.linked_list import LinkedList


def delete_middle(linked_list: LinkedList):
    # check if len(list) < 3
    if linked_list.head.next.next != None:
        runner = linked_list.head
        back = linked_list.head

        while runner and runner.next:
            runner = runner.next.next
            back = back.next

            if runner == None or runner.next == None:
                back.value = back.next.value
                back.next = back.next.next


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)
