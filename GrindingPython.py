# OOP
'''
class Person:
    def __init__(self, name:str, age:int, is_alive:bool) -> None:
        self.__name = name
        self.__age = age
        self.__is_alive = is_alive

    def get_name(self) -> str:
        return self.__name
    def set_name(self, name:str):
        self.__name = name
    def get_age(self) -> int:
        return self.__age
    def set_age(self, age:int):
        self.__age = age
    def get_is_alive(self) -> bool:
        return self.__is_alive
    def set_is_alive(self, is_alive:bool):
        self.__is_alive = is_alive

    def __str__(self) -> str:
        return f'(Person Name: {self.get_name()}, Person Age: {self.get_age()}, Person Alive: {self.get_is_alive()})'

    @staticmethod
    def check(x: "Person", y: "Person") -> bool:
        return x.__is_alive == y.__is_alive

    @classmethod
    def helper(cls, name:str, age:int, is_alive:bool) -> "Person":
        return cls(name=name, age=age, is_alive=is_alive)

    def __del__(self) -> None:
        print('Object Deleted')

p1 = Person(name = 'Mohit', age = 26, is_alive = True)
p2 = Person(name = 'Mitesh', age = 27, is_alive = True)
p3 = Person(name = 'Parag', age = 26, is_alive = True)
p4 = Person(name = 'Ameya', age = 25, is_alive = True)
p5 = Person.helper(name = 'Prasad', age = 28, is_alive = True)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
'''


# Inheritance
'''
class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return f'Person Name: {self.name}, Person Age: {self.age}, Person Height: {self.height}'

class Worker(Person):
    def __init__(self, name: str, age: int, height: float, salary: float):
        super().__init__(name, age, height)
        self.salary = salary

    def calculate_yearly_salary(self):
        return self.salary * 12

    def __str__(self) -> str:
        temp_text = super().__str__()
        text = f'{temp_text}, Person Salary: {self.salary}'
        return text

worker = Worker(name = 'Mohit', age = 26, height = 5.5, salary = 4000)
print(worker)
'''


# Decorators
'''
import time
def calculate_execution_time(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        function(*args, **kwargs)
        after = time.time()
        print(f'Time taken : {after - before}')
    return wrapper

@calculate_execution_time
def sort_numbers_1(arr: list[int]) -> None:
    arr.sort()

@calculate_execution_time
def sort_numbers_2(arr: list[int]) -> None:
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

nums: list[int] = [5,1,7,4,9,3,2]
sort_numbers_1(nums)
sort_numbers_2(nums)
'''


# Operator Overloading
'''
class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __add__(self, v) -> "Vector":
        return Vector(self.x + v.x, self.y + v.y)
    def __sub__(self, v) -> "Vector":
        return Vector(self.x - v.x, self.y - v.y)
    def __str__(self) -> str:
        return f'Vector : ({self.x},{self.y})'

v1 = Vector(10, 20)
v2 = Vector(50, 60)
print(v1 + v2)
print(v1 - v2)
'''


# Multithreading
'''
import threading
def print_one():
    for i in range(100):
        print('One')
def print_two():
    for i in range(100):
        print('Two')

t1 = threading.Thread(target=print_one)
t2 = threading.Thread(target=print_two)
t1.start()
t2.start()
t1.join()
t2.join()
'''


# Queues
'''
import queue
q1 = queue.Queue()
q1.put('Hello World')
q1.put( 10.5)
q1.put(True)
while not q1.empty():
    print(q1.get())
q2 = queue.LifoQueue()
q2.put('Hello World')
q2.put(10.5)
q2.put(True)
while not q2.empty():
    print(q2.get())
q3 = queue.PriorityQueue()
q3.put((2, 'Hello World'))
q3.put((5, 10.5))
q3.put((1, True))
while not q3.empty():
    print(q3.get())
'''


# Recursion
'''
def factorial_1(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial_1(n-1)

def factorial_2(n: int) -> int:
    ans: int = 1
    for i in range(1, n+1):
        ans *= i
    return ans
print(factorial_1(5))
print(factorial_2(5))

def fibo_1(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo_1(n-1) + fibo_1(n-2)

def fibo_2(n: int) -> int:
    first, second = 0, 1
    if n == 1:
        return first
    if n == 2:
        return second
    for i in range(3, n+1):
        first, second = second, first + second
    return second


print(fibo_1(5))
print(fibo_2(5))
'''


# Logging
'''
import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG)
logging.warning('You have got 20 mails in your inbox!')
logging.critical('All components have failed!')

logger = logging.getLogger('My Logger')
logger.info('Best logger was just created')
logger.critical('Your YT channel was deleted')
logger.log(logging.ERROR, 'Error occurred!')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('log_file.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug('This is a Debug message')
logger.info('This is an Info message')
'''


# Inheritance
'''
class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

    @staticmethod
    def help_parents() -> str:
        return 'Help Parents'

class Developer(Employee):
    def __init__(self, name, age, salary, programming_languages) -> None:
        super().__init__(name, age, salary)
        self.programming_languages = programming_languages

    def __str__(self) -> str:
        return f'{super().__str__()}, Programming Languages: {", ".join(self.programming_languages)}'

    def practise_coding(self) -> str:
        ans: str = 'Working on: '
        ans = ans + ', '.join(self.programming_languages)
        return ans

dev_1 = Developer('Mohit', 27, 80000, ['Python', 'Java', 'JavaScript'])
print(dev_1)
print(dev_1.help_parents())
print(dev_1.practise_coding())
'''


# Requests
'''
import requests
url = 'https://api.agify.io?name=meelad'
headers = {
    'User-Agent': 'Test-1.0',
    'Accept': 'application/json'
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data)
except Exception as e:
    print('Exception: ', e)
'''


# DataClass
'''
from dataclasses import dataclass

@dataclass()
class Person:
    name: str
    age: int
    salary: float
    is_married: bool

p1 = Person('Mohit', 26, 80000.00, False)
print(p1)
'''


# Falcon
'''
import falcon
from waitress import serve

class MyApp:
    def on_get(self, req, resp):
        resp.text = 'Hello World'
        resp.status = falcon.HTTP_OK

api = falcon.App()
api.add_route('/', MyApp())

if __name__ == '__main__':
    print(f'Server running on port 8001')
    serve(api, host='127.0.0.1', port=8001)
'''










'''
# Doubly LinkedList
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time Complexity: O(n)
    def __str__(self):
        ans = ''
        p = self.head
        while p:
            ans += f'<-> {p.val} <->'
            p = p.next
        return ans

    # Time Complexity: O(n)
    def append(self, val: int):
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(val)
        else:
            node = Node(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # Time Complexity: O(1)
    def prepend(self, val):
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(val)
        else:
            node = Node(val)
            self.head.prev = node
            node.next = self.head
            self.head = node

    # Time Complexity: O(1)
    def remove_front(self):
        if not self.head and not self.tail:
            return AssertionError
        if self.head and self.tail and self.head is self.tail and self.head.val == self.tail.val:
            val = self.head.val
            self.head = None
            self.tail = None
            return val

        node = self.head
        self.head = node.next
        node.next = None
        self.head.prev = None
        return node.val

    # Time Complexity: O(1)
    def remove_rear(self):
        if not self.head and not self.tail:
            return AssertionError
        if self.head and self.tail and self.head is self.tail and self.head.val == self.tail.val:
            val = self.head.val
            self.head = None
            self.tail = None
            return val

        node = self.tail
        self.tail = node.prev
        node.prev = None
        self.tail.next = None

    # Time Complexity: O(n)
    def __len__(self) -> int:
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.next
        return count

ll = ListNode()
ll.append(10)
ll.append(20)
ll.remove_front()
ll.remove_rear()
ll.append(30)
ll.append(40)
ll.append(1)
ll.prepend(5)
ll.remove_front()
ll.remove_rear()
print(ll)
print(len(ll))








import pytest

from linked_list import ListNode, Node

@pytest.fixture
def ll():
    return ListNode()

def test_append(ll):
    ll.append(10)
    ll.append(20)
    assert ll.__len__() == 2

def test_prepend(ll):
    ll.prepend(10)
    ll.prepend(20)
    assert ll.__len__() == 2

def test_remove_front(ll):
    val = ll.remove_front()
    assert val is AssertionError

def test_remove_rear(ll):
    ll.append(10)
    val = ll.remove_rear()
    assert val == 10

def test__len__(ll):
    ll.append(10)
    assert ll.__len__() == 1

'''






'''
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val: int) -> None:
        self.s1.append(val)

    def dequeue(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        value: int = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return value

    def queue_front(self):
        if self.queue_size() == 0:
            return IndexError
        while self.s1:
            self.s2.append(self.s1.pop())
        value: int = self.s2[len(self.s2)-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return value

    def queue_rear(self):
        if self.s1:
            return self.s1[len(self.s1)-1]
        return IndexError

    def queue_size(self) -> int:
        return len(self.s1)

    def __str__(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        ans = ''
        while self.s2:
            value: int = self.s2.pop()
            ans += str(value) + '->'
            self.s1.append(value)
        return ans

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print(f'Dequeue: {q.dequeue()}')
print(f'Queue Front: {q.queue_front()}')
print(f'Dequeue: {q.dequeue()}')
print(f'Queue Front: {q.queue_front()}')
print(q)
'''




'''
import pytest

from queue import Queue

@pytest.fixture()
def q():
    return Queue()

def test_enqueue(q):
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.queue_size() == 3

def test_queue_rear(q):
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.queue_rear() == 30

def test_dequeue(q):
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 10 and q.queue_size() == 2

def test_queue_front(q):
    assert q.queue_front() == IndexError and q.queue_size() == 0
'''










