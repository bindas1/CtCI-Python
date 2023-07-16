# 3.5 Sort Stacks
import unittest

from chapter_03.stack import Stack


def sort_stack(stack):
    """Returns sorted stack"""
    temp_stack = Stack()
    
    while not stack.is_empty():
        elem = stack.pop()
        if temp_stack.is_empty():
            temp_stack.push(elem)
            print("Adding elem to empty stack", elem)
        else:
            while not temp_stack.is_empty():
                if temp_stack.peek() >= elem:
                    temp_stack.push(elem)
                    print("Adding elem to full stack", elem)
                    break
                else:
                    print("Moving to the original stack", elem)
                    stack.push(temp_stack.pop())
            if temp_stack.is_empty():
                print("Adding elem to the beginning of stack", elem)
                temp_stack.push(elem)
            
    return temp_stack


def sort_stack2(stack):
    """Returns sorted stack"""
    temp_stack = Stack()
    
    while not stack.is_empty():
        elem = stack.pop()
        while not temp_stack.is_empty() and not temp_stack.peek() > elem:
            stack.push(temp_stack.pop())
        temp_stack.push(elem)
    return temp_stack


class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def push(self, item):
        if self.is_empty() or item < self.peek():
            super().push(item)
        else:
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())
            super().push(item)
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())


class Tests(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        assert len(queue) == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert len(queue) == 2

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert len(queue) == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4
