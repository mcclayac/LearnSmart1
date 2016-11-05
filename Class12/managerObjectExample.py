__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'

# A manager returned by Manager() will support types list, dict, Namespace,
# Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier,
# Queue, Value and Array.

from multiprocessing import Process, Manager


def display(dictionaryObj, listObj):
    dictionaryObj[1] = '1'
    dictionaryObj['2'] = 2
    dictionaryObj[0.25] = None
    listObj.reverse()
    print("Dictionary : ", dictionaryObj)
    print("List : ", listObj)


#if __name__ == '__main__':
def managerExample():
    with Manager() as manager:
        dictionaryObj = manager.dict()
        listObj = manager.list(range(10))

        # process objects represent activity that is run in a separate process.
        processObj = Process(target=display, args=(dictionaryObj, listObj))

        # start the processâ€™s activity.
        processObj.start()

        # block until all items in the queue have been processed
        processObj.join()