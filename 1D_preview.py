import time
import random
import matplotlib.pyplot as plt

def generate_random_sign():
    n = random.choice([-1, 1])
    return n
    
num_samples = 10000
result = [0]

x = 0

for i in range(num_samples):

    x1 = generate_random_sign()

    x += x1

    result.append(x)

zero = result.count(0)
max_d = max(max(result), abs(min(result)))

print("===== Result =====")
print(f"Final position for x: {x}")
print(f"How many times the dot comes back to the origin: {zero}")

plt.plot(result)
plt.axhline(y = 0, linestyle = '--')
plt.ylim(-max_d, max_d)
plt.title("1D Random walk preview")
plt.ylabel("Position")
plt.xlabel("Random walk steps")
plt.savefig(f"./graph/1D_Preview.png", dpi = 300)
plt.show()