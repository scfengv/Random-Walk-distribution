import time
import random
import numpy as np
import matplotlib.pyplot as plt
    
def generate_random_sign():
    n = random.choice([-1, 1])
    return n

num_trial, num_samples = 1000, 10000
pos_x = 0
dist = []

start_time = time.time()

for i in range(num_trial):
    x = 0
    for i in range(num_samples):

        x1 = generate_random_sign()

        if x1 == 1:
            pos_x += 1
        
        x += x1

    dist.append(x)

end_time = time.time()
calculation_time = end_time - start_time

max_dist = max(max(dist), abs(min(dist)))

print("========== Result ==========")
print(f"Positive percentage for x: {round((pos_x * 100 / (num_samples * num_trial)), 2)} %")
print("")
print(f"Calculation time: {round(calculation_time, 4)} seconds")
print("")
print(f"Min distance: {round(min(dist), 2)}")
print(f"Max distance: {round(max(dist), 2)}")
print(f"Average distance: {round(np.mean(dist), 2)}")
print(f"Standard deviation of distance: {round(np.std(dist), 2)}")
print("")


print("|  | Min distance | Max distance | Average distance | Standard Deviation |")
print("| - | - | - | - | - |")
print(f"| Distance | {round(min(dist), 2)} | {round(max(dist), 2)} | {round(np.mean(dist), 2)} | {round(np.std(dist), 2)} |")

plt.hist(dist, bins = 100)
plt.xlabel("Distance from the origin")
plt.ylabel("Probability density")
plt.xlim([-max_dist, max_dist])

plt.title(f"Probability density of 1D Random walk, trials = {num_trial}, steps = {num_samples}")

plt.savefig(f"./graph/1D_{num_trial}_{num_samples}.png", dpi = 300)
plt.show()