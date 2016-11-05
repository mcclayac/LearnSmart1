__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'

# Data can be stored in a shared memory map using Value or Array

from multiprocessing import Process, Value, Array


def display(num, array):
    num.value = 3.1415927
    for i in range(len(array)):
        array[i] = -array[i]


#if __name__ == '__main__':
def sharedMemoryExample():
    num = Value('d', 0.0)
    array = Array('i', range(10))

    # process objects represent activity that is run in a separate process.
    processObj = Process(target=display, args=(num, array))

    # start the processâ€™s activity.
    processObj.start()

    # block until all items in the queue have been processed
    processObj.join()

    print("number : ", num.value)
    print("array : ", array[:])

