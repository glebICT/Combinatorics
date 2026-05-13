import operator
import time
a = list(range(1, 10001))
b = list(range(1, 10001))
num_iterations = 5
mapt = []
loopt = []
# Measure the performance of the map function
for _ in range(num_iterations):
    t1 = time.time()
    result = list(map(operator.mul, a, b))
    t2 = time.time()
    mapt.append(t2 - t1)
# Measure the performance of the for loop
for _ in range(num_iterations):
    t1 = time.time()
    result = [a[i] * b[i] for i in range(len(a))]
    t2 = time.time()
    loopt.append(t2 - t1)
# Calculate average times
avg_mapt = sum(mapt) / num_iterations
avg_loopt = sum(loopt) / num_iterations
print(f"Average time of map: {avg_mapt:.6f} seconds")
print(f"Average time of for loop: {avg_loopt:.6f} seconds")
