from src.parallel.prime_factors import launch_multi_proc_prime_factors
from src.parallel.proc_generate import launch_multi_proc_generate
from src.parallel.thread_generate import launch_multi_thread_generate

from src.util.rsa import generate
import multiprocessing as mp



if __name__ == "__main__":
    num_keys = 100
    num_proc = 10
    num_thread = 10
    nBits = 2048

    #multi processus 
    mp.set_start_method('spawn')
    launch_multi_proc_generate(num_keys, num_proc, nBits)

    #multi thread
    #launch_multi_thread_generate(num_keys, num_thread, nBits)

    #single processus
    #generate(nBits)