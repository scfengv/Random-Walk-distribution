import time
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_sign():
    n = random.choice([-1, 1])
    return n

num_trial, num_samples = 1000, 10000
result = [(0, 0)]
dist = [0]
x, y, pos_x, pos_y = 0, 0, 0, 0
quad_1, quad_2, quad_3, quad_4 = 0, 0, 0, 0

for i in range(num_samples):

    x1 = generate_random_sign()
    y1 = generate_random_sign()

    x += x1
    y += y1

    if x > 0:
        if y > 0:
            quad_1 += 1
        else:
            quad_4 += 1

    elif x < 0:
        if y > 0:
            quad_2 += 1
        else:
            quad_3 += 1
    
    result.append((x, y))
    
    d = np.sqrt(x**2 + y**2)
    dist.append(d)

x_values = [point[0] for point in result]
y_values = [point[1] for point in result]

width_max = max(max(x_values), max(y_values), abs(min(x_values)), abs(min(y_values)))

print("===== Result =====")
print(f"Final position: {result[-1]}")

print(f"Quadrant 1: {round(quad_1 * 100 / num_samples, 2)} %")
print(f"Quadrant 2: {round(quad_2 * 100 / num_samples, 2)} %")
print(f"Quadrant 3: {round(quad_3 * 100 / num_samples, 2)} %")
print(f"Quadrant 4: {round(quad_4 * 100 / num_samples, 2)} %")


fig, axs = plt.subplots(2, 1)

axs[0].plot(x_values, y_values, marker = 'o', markersize = 3, linestyle = '-')
axs[0].plot(0, 0, marker = 'o', markersize = 3, color = 'green')
axs[0].plot(result[-1][0], result[-1][1], marker = 'o', markersize = 3, color = 'red')
axs[0].set_xlim([-width_max, width_max])
axs[0].set_ylim([-width_max, width_max])
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].set_title("2D probability distribution")
axs[0].grid(True)

axs[1].plot(dist)
axs[1].set_xlabel("Random Walk Steps")
axs[1].set_ylabel("Distance")
axs[1].set_title("Distance from the origin")

plt.tight_layout() 
plt.savefig(f"./graph/2D_Preview.png", dpi = 300)
plt.show()