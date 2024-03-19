import time
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_sign():
    n = random.choice([-1, 1])
    return n
    
num_trial, num_samples = 1000, 1000
pos_x, pos_y = 0, 0
l1_dist = []
l2_dist = []

start_time = time.time()

for i in range(num_trial):
    x, y = 0, 0
    for i in range(num_samples):

        x1 = generate_random_sign()
        y1 = generate_random_sign()

        if x1 == 1:
            pos_x += 1
    
        if y1 == 1:
            pos_y += 1
        
        x += x1
        y += y1

    l2 = np.sqrt(x**2 + y**2)
    l2_dist.append(l2)

    l1 = abs(x) + abs(y)
    l1_dist.append(l1)

end_time = time.time()
calculation_time = end_time - start_time

max_dist = max(max(l1_dist), max(l2_dist))

print("========== Result ==========")
print(f"Positive percentage for x: {round((pos_x * 100 / (num_samples * num_trial)), 4)} %")
print("")
print(f"Positive percentage for y: {round((pos_y * 100 / (num_samples * num_trial)), 4)} %")
print("")
print(f"Calculation time: {round(calculation_time, 4)} seconds")
print("")
print(f"Min L1 distance: {round(min(l1_dist), 2)}")
print(f"Max L1 distance: {round(max(l1_dist), 2)}")
print(f"Average L1 distance: {round(np.mean(l1_dist), 2)}")
print(f"Standard deviation of L1 distance: {round(np.std(l1_dist), 2)}")
print("")
print(f"Min L2 distance: {round(min(l2_dist), 2)}")
print(f"Max L2 distance: {round(max(l2_dist), 2)}")
print(f"Average L2 distance: {round(np.mean(l2_dist), 2)}")
print(f"Standard deviation of L2 distance: {round(np.std(l2_dist), 2)}")
print("")


print("|  | Min distance | Max distance | Average distance | Standard Deviation |")
print("| - | - | - | - | - |")
print(f"| L1 | {round(min(l1_dist), 2)} | {round(max(l1_dist), 2)} | {round(np.mean(l1_dist), 2)} | {round(np.std(l1_dist), 2)} |")
print(f"| L2 | {round(min(l2_dist), 2)} | {round(max(l2_dist), 2)} | {round(np.mean(l2_dist), 2)} | {round(np.std(l2_dist), 2)} |")

fig = plt.figure()

fig.add_subplot(211)
plt.hist(l1_dist, bins = 100)
plt.xlabel("L1 Distance from the origin")
plt.ylabel("Probability density")
plt.xlim([0, max_dist])

fig.add_subplot(212)
plt.hist(l2_dist, bins = 100)
plt.xlabel("L2 Distance from the origin")
plt.ylabel("Probability density")
plt.xlim([0, max_dist])

plt.title(f"Probability density of 2D Random walk, trials = {num_trial}, steps = {num_samples}")
plt.tight_layout()
plt.savefig(f"./graph/2D_{num_trial}_{num_samples}.png", dpi = 300)
plt.show()