import random
import multiprocessing
import os
import math

# User-supplied target number of rolls to perform
rolls = 10_000_000

# Get the number of available CPU cores
maxProcessCount = os.cpu_count()

def doRolls(count):
    maxOnes = 0
    tempOnes = 0
    for x in range(count):
        for x in range(231):
            if random.getrandbits(2) == 0:
                tempOnes += 1
        maxOnes = max(tempOnes, maxOnes)
        tempOnes = 0
    return maxOnes

def main():
    # Create a pool of processes
    with multiprocessing.Pool(processes=maxProcessCount) as pool:
        # Divide number of rolls by the number of processes and start each process
        results = pool.map(doRolls, [math.ceil(rolls / maxProcessCount)] * maxProcessCount)

    # Find the largest ones from the results returned by each process
    maxOnes = max(results)

    # Print results
    print("Highest Ones Roll:", maxOnes)
    print("Number of Roll Sessions: ", math.ceil(rolls / maxProcessCount) * maxProcessCount)

if __name__ == "__main__":
    main()