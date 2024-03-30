import time
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_sign():
    n = random.choice([-1, 1])
    return n
    
num_trial = 1000
num_samples_list = [100, 1000, 10000, 100000, 1000000]
l1_data = {}
l2_data = {}

for num_samples in num_samples_list:
    pos_x, pos_y, pos_z = 0, 0, 0
    l1_dist = []
    l2_dist = []

    start_time = time.time()

    for i in range(num_trial):
        x, y, z = 0, 0, 0
        for i in range(num_samples):

            x1 = generate_random_sign()
            y1 = generate_random_sign()
            z1 = generate_random_sign()
            
            x += x1
            y += y1
            z += z1

        l2 = np.sqrt(x**2 + y**2 + z**2)
        l2_dist.append(l2)

        l1 = abs(x) + abs(y) + abs(z)
        l1_dist.append(l1)

    l1_data[num_samples] = (l1_dist, round(np.mean(l1_dist), 2), round(np.std(l1_dist), 2))
    l2_data[num_samples] = (l2_dist, round(np.mean(l2_dist), 2), round(np.std(l2_dist), 2))

    end_time = time.time()
    calculation_time = end_time - start_time

    print(f"Calculation time for num_samples = {num_samples}: {round(calculation_time, 4)} seconds")

fig, axs = plt.subplots(len(num_samples_list), 2, figsize=(10, 10))

for i, num_samples in enumerate(num_samples_list):
    l1_dist = l1_data[num_samples][0]
    l2_dist = l2_data[num_samples][0]
    max_dist = max(max(l1_dist), max(l2_dist))

    axs[i, 0].hist(l1_dist, bins = 100)
    axs[i, 0].set_title(f'L1 Distance, num_samples = {num_samples}\nAvg = {l1_data[num_samples][1]}, Std = {l1_data[num_samples][2]}')
    axs[i, 0].set_xlim([0, max_dist])
    axs[i, 0].set_ylabel('Probability density')

    axs[i, 1].hist(l2_dist, bins = 100)
    axs[i, 1].set_title(f'L2 Distance, num_samples = {num_samples}\nAvg = {l2_data[num_samples][1]}, Std = {l2_data[num_samples][2]}')
    axs[i, 1].set_xlim([0, max_dist])
    axs[i, 1].set_ylabel('Probability density')

plt.tight_layout()
plt.savefig(f"./graph/3D.png", dpi = 300)
plt.show()