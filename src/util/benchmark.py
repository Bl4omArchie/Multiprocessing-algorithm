from contextlib import contextmanager
from time import perf_counter


#Each time a processus/thread is ended, a message is printed with the execution time
@contextmanager
def timing(message, num):
    t = perf_counter()
    yield
    end = perf_counter()
    
    print ("*chrono> ", message, end-t)
    print ("|-> avg: ", (end-t)/num)
    print ("-----------------------------------------------------------")