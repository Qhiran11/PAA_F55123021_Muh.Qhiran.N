import random
import time
import matplotlib.pyplot as plt
import os


def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]


def is_unique(arr):
    return len(arr) == len(set(arr))


def measure_time(n, max_value, seed):

    arr = generate_array(n, max_value, seed)
    start_time = time.time()
    is_unique(arr)
    end_time = time.time()
    return end_time - start_time


stambuk = 21  
max_value = 250 - stambuk
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
seed = 42


worst_case_times = []
average_case_times = []

for n in n_values:

    worst_case_array = [1] * n
    start_time = time.time()
    is_unique(worst_case_array)
    end_time = time.time()
    worst_case_times.append(end_time - start_time)
    

    avg_time = measure_time(n, max_value, seed)
    average_case_times.append(avg_time)


os.makedirs("hasil", exist_ok=True)


with open("hasil/worst_avg.txt", "w") as f:
    f.write("n, Worst Case Time, Average Case Time\n")
    for i in range(len(n_values)):
        f.write(f"{n_values[i]}, {worst_case_times[i]:.6f}, {average_case_times[i]:.6f}\n")


plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label="Worst Case", marker='o')
plt.plot(n_values, average_case_times, label="Average Case", marker='s')
plt.title("Worst Case vs Average Case for Unique Check")
plt.xlabel("n (Array Size)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid()
plt.savefig("UAS/execution_time_plot.jpg")
plt.show()
