__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'

# !/usr/bin/python

print("\nExample program : Coroutines and Microthreading\n")


def first():
    for n in range(5):
        print("First Method : %d" % n)
        yield


def second():
    for n in range(10):
        print("Second Method : %d" % n)
        yield


def third():
    for n in range(7):
        print("Third Method : %d" % n)
        yield


# Create and populate a task queue
from collections import deque

taskqueue = deque()
taskqueue.append(first())  # Add some tasks (generators)
taskqueue.append(second())
taskqueue.append(third())

# Run all of the tasks
while taskqueue:
    # Get the next task
    task = taskqueue.pop()
    try:
        # Run it to the next yield and enqueue
        next(task)
        taskqueue.appendleft(task)
    except StopIteration:
        # Task is done
        pass


