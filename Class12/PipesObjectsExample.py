__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/5/16'
__revision__ = '$'
__revision_date__ = '$'


from multiprocessing import Process, Pipe


def displayPipes(pipeObj):
    # send an object to the other end of the connection which should be read using recv().
    pipeObj.send([42, None, 'hello'])

    # close the connection
    pipeObj.close()


#if __name__ == '__main__':

def pipesExample():
    print("\nExample program : Pipes\n")

    # returns a pair (conn1, conn2) of Connection objects representing the ends of a pipe.
    parent_conn, child_conn = Pipe()

    # Process objects represent activity that is run in a separate process.
    processObj = Process(target=displayPipes, args=(child_conn,))

    print("Before start: ", processObj, processObj.is_alive())
    # start the processâ€™s activity.
    processObj.start()

    # prints "[42, None, 'hello']"
    # return an object sent from the other end of the connection using send()
    print(" Pipe recv method :", parent_conn.recv())

    print("After start: ", processObj, processObj.is_alive())
    # block until all items in the queue have been processed
    processObj.join()


from multiprocessing import Pool


def Square(x):
    return x * x


def poolExample():
#if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:
        # evaluate "Square(10)" asynchronously
        result = pool.apply_async(Square, (10,))

        # prints "100" unless your computer is *very* slow
        print(result.get(timeout=1))

        # prints "[0, 1, 4,..., 81]"
        print(pool.map(Square, range(10)))

        it = pool.imap(Square, range(10))

        # prints "0"
        print(next(it))

        # prints "1"
        print(next(it))

        # prints "4" unless your computer is *very* slow
        print(it.next(timeout=1))

        import time

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))  # raises TimeoutError
