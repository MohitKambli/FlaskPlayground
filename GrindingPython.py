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

    def __str__(self):
        ans = ''
        p = self.head
        while p:
            ans += f' {p.val} <->'
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

    def remove_front(self):
        node = self.head
        self.head = node.next
        node.next = None
        self.head.prev = None

    def remove_rear(self):
        node = self.tail
        self.tail = node.prev
        node.prev = None
        self.tail.next = None

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
ll.append(30)
ll.append(40)
ll.append(1)
ll.prepend(5)
ll.remove_front()
ll.remove_rear()
print(ll)
print(len(ll))
'''
