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

I'm using this decorator to measure the execution time of a code block. This is the process: 
- the function perf_counter() record the time before the program start
- I use the yield instruction to let the program continue
- I'm printing the time ellapsed since the program has started and it give me the total time of execution

The measurement is very accurate:
```
*chrono>  Facteurs multi 2: 4.227859886999795
```

## Multiprocessing module

in progress...


# Sources:
[Python avancé et programmation scientifique - Jerzy Karczmarczuk](https://hal.science/hal-02474793)