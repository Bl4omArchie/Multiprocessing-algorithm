from time import perf_counter
from contextlib import contextmanager

from random import randint
import multiprocessing as mp
from multiprocessing import Process

NbProc = 2

@contextmanager
def timing(message):
    t = perf_counter()
    yield
    print ("*chrono> ", message, perf_counter()-t)

def prime_factors(n):
    primeFact = []
    d = 2

    while d*d <= n:
        while not (n%d):
            primeFact.append(d)
            n //= d
        d+=1
    if n>1:
        primeFact.append(n)
    return primeFact


def exe_proc():
    for _ in range(30000//NbProc):
        r = randint(20000, 1000000000)
        pf = prime_factors(r)
        #print (f"Facteurs de r: {pf}")

def multi_proc_simulation():
    with timing(f"Facteurs multi {NbProc}:"):
        procs = []

        for i in range(NbProc):
            proc = Process(target=exe_proc, args=())
            procs.append(proc)
            proc.start()
        
        for proc in procs:
            proc.join()

def single_proc_simulation():
    with timing(f"Facteurs multi {NbProc}:"):
        for _ in range(NbProc):
            exe_proc()

if __name__ == "__main__":
    #multi processus 
    mp.set_start_method('spawn')
    multi_proc_simulation()

    #single processus
    single_proc_simulation()