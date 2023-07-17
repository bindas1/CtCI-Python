import time
import string
import random


class Animal:
    def __init__(self, name=''):
        self.name = name if name != '' else random.choice(string.ascii_letters)
        print("Hey my name is ", self.name)

class Dog(Animal):
    def __init__(self, name=''):
        super().__init__(name)
    
    def __str__(self):
        print("Hey my name is ", self.name)
        
class Cat(Animal):
    def __init__(self, name=''):
        super().__init__(name)
    
    def __str__(self):
        print("Hey my name is ", self.name)

import time

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0] if self.items != [] else None
    
class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
    
    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.enqueue((animal, time.time()))
        else:
            self.dogs.enqueue((animal, time.time()))
    
    def dequeueDog(self):
        return self.dogs.dequeue()[0]
    
    def dequeueCat(self):
        return self.cats.dequeue()[0]
    
    def dequeueAny(self):
        if self.dogs.peek() is None:
            return self.cats.dequeue()[0]
        elif self.cats.peek() is None:
            return self.dogs.dequeue()[0]
        if self.dogs.peek()[1] < self.cats.peek()[1]:
            return self.dogs.dequeue()[0]
        else:
            return self.cats.dequeue()[0]


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head
            self.head = self.head.next_node
            return head_to_pop

        return None

    def size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size


# Animal Definitions


class Animal:
    def __init__(self, name):
        self.time_admitted = time.time()
        self.name = name


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalShelter(LinkedList):
    def enqueue(self, animal):
        animal_node = Node(animal)
        self.insert(animal_node)

    def dequeue_any(self):
        return super().pop_head()

    def dequeue_cat(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Cat):
                previous_node.next_node = current_node.next_node
                return current_node.data
            previous_node = current_node
            current_node = current_node.next_node
        return None

    def dequeue_dog(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Dog):
                previous_node.next_node = current_node.next_node
                return current_node.data
            previous_node = current_node
            current_node = current_node.next_node
        return None


def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert animal_shelter.size() == 3
