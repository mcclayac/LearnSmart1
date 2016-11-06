__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'

# !/usr/bin/python

from multiprocessing import Process, Queue


def display(queue):
    # put item into the queue.
    queue.put('X' * 1000000)


if __name__ == '__main__':
    # constructor for a FIFO queue.
    queueObj = Queue()

    # process objects represent activity that is run in a separate process.
    processObj = Process(target=display, args=(queueObj,))

    print("Before start: ", processObj, processObj.is_alive())

    # start the processâ€™s activity.
    processObj.start()

    print("After start: ", processObj, processObj.is_alive())

    # block until all items in the queue have been processed
    # processObj.join()                    # this deadlocks

    print("Before Queue get method: ", processObj, processObj.is_alive())
    # remove and return an item from the queue.
    print(" Queue get method :", queueObj.get())

    print("After Queue get method: ", processObj, processObj.is_alive())