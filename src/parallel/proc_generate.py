from multiprocessing import Process
from src.util import rsa
from src.util.benchmark import timing

key_pairs = []
round = 4


def generate_n_keys(num_key, nBits):
    with timing(f"{num_key} keys of {nBits} bits:", num_key):
        for _ in range(num_key):
            key_pairs.append(rsa.generate(nBits))


def launch_multi_proc_generate(num_keys, num_proc, nBits):
    #TODO: work on the key repartition for each proc 
    key_per_proc = num_keys//num_proc

    with timing(f"With {num_proc} processus for {num_keys} keys:", num_keys):
        procs = []
        for _ in range(num_proc):
            proc = Process(target=generate_n_keys, args=(key_per_proc, nBits))
            procs.append(proc)
            proc.start()
        
        for proc in procs:
            proc.join()