# Optimized Graveler Submission

## Description
This repository contains my submission for the challenge presented in the [You'll NEVER Escape Pikasprey's Evil Soft Lock ](https://www.youtube.com/watch?v=M8C8dHQE2Ro) youtube video. The goal is to enhance the performance of the [Graveler script](https://github.com/arhourigan/graveler) used to simulate the video's scenario.


## Approach
### Memory Optimization
The original script tracked values for all four possible outcomes of each dice roll. By tracking only the result of "one," this optimized version saves both time and memory space.

### Improved random number generation
I switched from using random.choice() to random.getrandbits(2) for the improved speed and due to no longer tracking the other three possibilities on the dice role. Meaning there was now only one choice, resulting in all ones when using random.choice().

### Multi-threading
The original script was single-threaded, processing dice rolls sequentially. By implementing multi-threading, the script now divides rolls into multiple parallel sequences, improving efficiency.

To address Python's Global Interpreter Lock (GIL) limitation, which restricts execution to a single thread per process, the script utilizes the multiprocessing library. This approach creates multiple processes, each with its own GIL, enabling true multi-threading.

## Results
These optimizations resulted in a 99.7% reduction in the time required to complete 1,000,000 rolls. The original script took 11 minutes and 20 seconds, whereas the optimized version completes the task in just 9 seconds.

There is a small difference in the number of rolls between the two scripts. This is a result of floating point precision errors when splitting the quantity of rolls between the processes and rounding the resulting float up to the nearest int.

Due to my script dynamically changing the number of threads based on the number present on the CPU, these run times will change based on the thread count of the CPU. With this script taking longer on CPUs with lower core counts and running faster on those with higher core count.

The script's runtime varies based on the CPU's thread count. This means that CPUs with fewer threads will experience longer run times, while those with more cores will benefit from faster execution.

### My Script
```
gravelerSubmission$ time python3 gravelerSubmission.py
Highest Ones Roll: 95
Number of Roll Sessions:  10000008

real    0m9.035s
user    3m26.601s
sys     0m0.177s
```

### Original Script
```
gravelerSubmission$ time python3 gravelerOriginal.py
Highest Ones Roll: 95
Number of Roll Sessions:  10000000

real    11m20.271s
user    11m20.136s
sys     0m0.005s
```
