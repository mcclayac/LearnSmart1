__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'

from multiprocessing import Process, Lock


def displayLock(lock, num):
    # acquire a lock, blocking or non-blocking
    lock.acquire()

    print('display :', num)

    # Release a lock. This can be called from any thread, not only the thread
    # which has acquired the lock.
    lock.release()


#if __name__ == '__main__':
def lockExample():
    # create a shared threading.Lock object and return a proxy for it.
    lock = Lock()

    for num in range(10):
        # process objects represent activity that is run in a separate process.
        # start the processâ€™s activity.
        Process(target=displayLock, args=(lock, num)).start()



