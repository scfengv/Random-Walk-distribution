import time
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_sign():
    n = random.choice([-1, 1])
    return n
    
num_trial = 1000
num_samples_list = [100, 1000, 10000, 100000, 1000000]
dist = {}

for num_samples in num_samples_list:
    pos_x = 0
    d = []

    start_time = time.time()

    for i in range(num_trial):
        x, y = 0, 0
        for i in range(num_samples):

            x1 = generate_random_sign()

            if x1 == 1:
                pos_x += 1
            
            x += x1

        d.append(x)

    dist[num_samples] = (d, round(np.mean(d), 2), round(np.std(d), 2))

    end_time = time.time()
    calculation_time = end_time - start_time

    print(f"Calculation time for num_samples = {num_samples}: {round(calculation_time, 4)} seconds")

fig, axs = plt.subplots(3, 2, figsize = (10, 10))

for i, num_samples in enumerate(num_samples_list):

    row = np.log10(num_samples)

    if row % 2 == 0:
        r = 0
        c = int(row / 2 - 1)
    else:
        r = 1
        c = int(np.floor(row / 2 - 1))

    d = dist[num_samples][0]
    max_dist = max(d)

    axs[c, r].hist(d, bins = 100)
    axs[c, r].set_title(f'Distance, num_samples = {num_samples}\nAvg = {dist[num_samples][1]}, Std = {dist[num_samples][2]}')
    axs[c, r].set_xlim([-max_dist, max_dist])
    axs[c, r].set_ylabel('Probability density')


plt.tight_layout()
plt.savefig(f"./graph/1D.png", dpi = 300)
plt.show()