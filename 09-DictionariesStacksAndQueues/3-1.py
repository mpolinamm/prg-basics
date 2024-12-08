import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

numbers = queue.LifoQueue()

numbers.put(2)
numbers.put(3)
numbers.put(7)
numbers.put(4)
numbers.put(1)
numbers.put(9)
numbers.put(8)

last = numbers.get()
second_last = numbers.get()
sum_last_two = last + second_last
print("Sum of the last two numbers:", sum_last_two)

sum_remaining = 0
while not numbers.empty():
    sum_remaining += numbers.get()

print("Sum of the remaining stack elements:", sum_remaining)
