# Finding prime factors using multiprocessing

From the book: Advanced python and scientic programmation by Jerzy Karczmarczuk, I implemented an algorithm that find prime factors of a given number. The goal is to paralalized the process so we can run the algorithm several times at once.


## Context Manager

```py
@contextmanager
def timing(message):
    t = perf_counter()
    yield
    print ("*chrono> ", message, perf_counter()-t)
```

I'm using this decorator to measure the execution time of a code block. The process is the following: 
- the function perf_counter() record the time before the program start
- I use the yield instruction to let the program continue
- I'm printing the time ellapsed since the program has started and it give me the total time of execution

The measurement is very accurate:
```
*chrono>  Facteurs multi 2: 4.227859886999795
```

## Generate
The generate.py is a test for generating RSA key pairs with multiprocessing. If I want N keys, I divide the numbers of keys by the number of processus which give the numbers of key that one processus will be generating. This is sample of the first tests:
For 5 processus:
```
*chrono>  Generating 20 keys of 2048 bits: 101.70569087499996
*chrono>  Generating 20 keys of 2048 bits: 105.44192267799997
*chrono>  Generating 20 keys of 2048 bits: 116.323315047
*chrono>  Generating 20 keys of 2048 bits: 128.22645591999998
*chrono>  Generating 20 keys of 2048 bits: 133.698310181
*chrono>  For 5 processus: 133.77674500900002
```
For 10 processus:
```
*chrono>  Generating 10 keys of 2048 bits: 76.45657361400004
*chrono>  Generating 10 keys of 2048 bits: 88.58233852800004
*chrono>  Generating 10 keys of 2048 bits: 96.63851762500008
*chrono>  Generating 10 keys of 2048 bits: 101.14048556400007
*chrono>  Generating 10 keys of 2048 bits: 104.37396468500003
*chrono>  Generating 10 keys of 2048 bits: 106.74245541000005
*chrono>  Generating 10 keys of 2048 bits: 109.62159420400008
*chrono>  Generating 10 keys of 2048 bits: 116.56856248600002
*chrono>  Generating 10 keys of 2048 bits: 116.620228193
*chrono>  Generating 10 keys of 2048 bits: 122.46367952699995
*chrono>  With 10 processus: 122.63489865200006
```

For the moment it is too early for conclusion, the generation process is unstable and the result aren't really what I expected. 


# Sources:
[Python avancé et programmation scientifique - Jerzy Karczmarczuk](https://hal.science/hal-02474793)