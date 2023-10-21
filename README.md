# Finding prime factors using multiprocessing

From the book: Advanced python and scientic programmation by Jerzy Karczmarczuk, I'm learning about multithreading and multiprocessing. My goals here are to learn the basics for making parallel algorithm and to have a better understanding of what is effiency. What can improve an algorithm ? Did parallezing algorithms worth it and if yes how ?

I have implemented three parallel algorithms:
- prime factors
- RSA key pairs generator with multiprocessing
- RSA key pairs generator with multithreading

I'm doing test to see which way is the best to make those tasks faster. For instance one of my main ideas was to make the whole process of a key pairs generator in parallel so I can generate the highest amount of keys. I'm trying to figure out how it can be done.


## Benchmark

**Disclaimer:** Evaluating the performance for a parallel algorithm is harder than the single processus function. I'm still working on the benchmark so I can measure in a correct way the effiency of my algorithms and also make a meaningful comparison between the multi-proc and single-proc algorithm.  

### Context manager

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

The measurement is very accurate (seconds): 
```
*chrono>  Facteurs multi 2: 4.227859886999795
```

### Results
This is a sample of test from the multiprocessing key pairs generator. For each processus I'm generating N keys, I print the execution time (in seconds) for the whole processus and a average time for one key.    
**100 keys for 5 processus:**
```
*chrono>  20 keys of 2048 bits: 120.85321527899998
|-> avg:  6.042660763949999
-----------------------------------------------------------
*chrono>  20 keys of 2048 bits: 124.392143111
|-> avg:  6.219607155549999
-----------------------------------------------------------
*chrono>  20 keys of 2048 bits: 128.158622556
|-> avg:  6.4079311278
-----------------------------------------------------------
*chrono>  20 keys of 2048 bits: 139.41532958200003
|-> avg:  6.970766479100002
-----------------------------------------------------------
*chrono>  20 keys of 2048 bits: 154.503436157
|-> avg:  7.725171807850001
-----------------------------------------------------------
*chrono>  With 5 processus: 154.60126702000002
|-> avg:  30.920253404000004
-----------------------------------------------------------
```

**100 keys for 10 processus:**
```
*chrono>  10 keys of 2048 bits: 80.65746558900003
|-> avg:  8.065746558900003
-----------------------------------------------------------
*chrono>  10 keys of 2048 bits: 84.483848502
|-> avg:  8.4483848502
-----------------------------------------------------------
*chrono>  10 keys of 2048 bits: 90.38790660200004
|-> avg:  9.038790660200004

...

*chrono>  10 keys of 2048 bits: 97.66862106099995
|-> avg:  9.766862106099996
-----------------------------------------------------------
*chrono>  10 keys of 2048 bits: 103.83959000900006
|-> avg:  10.383959000900006
-----------------------------------------------------------
*chrono>  10 keys of 2048 bits: 107.33971728200004
|-> avg:  10.733971728200004
-----------------------------------------------------------
*chrono>  With 10 processus: 107.50551436899991
|-> avg:  10.750551436899991
-----------------------------------------------------------
```

**200 keys for 15 processus:**
```
*chrono>  13 keys of 2048 bits: 179.01978532400017
|-> avg:  13.770752717230781
-----------------------------------------------------------
*chrono>  13 keys of 2048 bits: 180.04305490700017
|-> avg:  13.849465762076935
-----------------------------------------------------------
*chrono>  13 keys of 2048 bits: 191.885950481
|-> avg:  14.760457729307692
-----------------------------------------------------------

...

*chrono>  13 keys of 2048 bits: 226.32043813200016
|-> avg:  17.40926447169232
-----------------------------------------------------------
*chrono>  13 keys of 2048 bits: 231.43199777299992
|-> avg:  17.80246136715384
-----------------------------------------------------------
*chrono>  13 keys of 2048 bits: 234.04581142000006
|-> avg:  18.00352395538462
-----------------------------------------------------------
*chrono>  13 keys of 2048 bits: 235.15784594299998
|-> avg:  18.08906507253846
-----------------------------------------------------------
*chrono>  13 keys of 2048 bits: 243.8047373689999
|-> avg:  18.754210566846147
-----------------------------------------------------------
*chrono>  With 15 processus: 244.05981024599987
|-> avg:  16.27065401639999
-----------------------------------------------------------
```

# Sources:
[Python avancé et programmation scientifique - Jerzy Karczmarczuk](https://hal.science/hal-02474793)
[Algorithms for Modern Hardware by Sergey Slotin](https://en.algorithmica.org/hpc)
[Python documentation for concurrent.futures module](https://docs.python.org/3/library/concurrent.futures.html)
[Python documentation for multiprocessing module](https://docs.python.org/3/library/multiprocessing.html)