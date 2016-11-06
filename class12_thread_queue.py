__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'

# !/usr/bin/python

print("\nExample program : Queues with Threads\n")
from queue import Queue
import threading


class sampleThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        # to invoke the base class constructor
        threading.Thread.__init__(self, *args, **kwargs)
        # constructor for a FIFO queue.
        self.input_queue = Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    def run(self):
        while True:
            item = self.input_queue.get()
            if item is None:
                break

            # Process the item
            print(item)
            self.input_queue.task_done()

        # Done. Indicate that sentinel was received and return
        self.input_queue.task_done()
        return


# Example use
obj = sampleThread()
# start the threadâ€™s activity.
obj.start()

obj.send("hello")  # Send items to the class (via queue)
obj.send("world")
obj.close()