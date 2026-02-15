import time
import matplotlib.pyplot as plt
import random
import os
os.makedirs("plots", exist_ok=True)
random.seed(42)


# =========================================================
# -------------------- TASK 1 ------------------------------
# =========================================================

def constant_time(n):
    return n * 2

def linear_time(n):
    total = 0
    for i in range(n):
        total += i
    return total

def quadratic_time(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total

def logarithmic_time(n):
    while n > 1:
        n = n // 2

sizes = [10, 100, 300, 500]

functions = {
    "O(1)": constant_time,
    "O(n)": linear_time,
    "O(n^2)": quadratic_time,
    "O(log n)": logarithmic_time
}

results = {key: [] for key in functions}

for size in sizes:
    for key in functions:
        start = time.time()
        functions[key](size)
        results[key].append(time.time() - start)

# 4 Separate Graphs
for key in results:
    plt.figure()
    plt.plot(sizes, results[key])
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time")
    plt.title(f"{key} Growth")
    plt.grid(True)
    plt.savefig(f"plots/task1_{key}.png")
    plt.show()


# =========================================================
# -------------------- TASK 2 ------------------------------
# =========================================================

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sizes = [100, 500, 1000, 3000]

linear_best, linear_avg, linear_worst = [], [], []
binary_best, binary_avg, binary_worst = [], [], []

for size in sizes:
    arr = sorted(random.sample(range(size*10), size))

    # Best Case
    target = arr[0]
    start = time.time()
    linear_search(arr, target)
    linear_best.append(time.time() - start)

    start = time.time()
    binary_search(arr, target)
    binary_best.append(time.time() - start)

    # Worst Case
    target = arr[-1]
    start = time.time()
    linear_search(arr, target)
    linear_worst.append(time.time() - start)

    start = time.time()
    binary_search(arr, target)
    binary_worst.append(time.time() - start)

    # Average Case
    target = arr[size // 2]
    start = time.time()
    linear_search(arr, target)
    linear_avg.append(time.time() - start)

    start = time.time()
    binary_search(arr, target)
    binary_avg.append(time.time() - start)

# Linear Search Graph
plt.figure()
plt.plot(sizes, linear_best, label="Best")
plt.plot(sizes, linear_avg, label="Average")
plt.plot(sizes, linear_worst, label="Worst")
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Linear Search Analysis")
plt.legend()
plt.grid(True)
plt.savefig("plots/task2_linear.png")
plt.show()

# Binary Search Graph
plt.figure()
plt.plot(sizes, binary_best, label="Best")
plt.plot(sizes, binary_avg, label="Average")
plt.plot(sizes, binary_worst, label="Worst")
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Binary Search Analysis")
plt.legend()
plt.grid(True)
plt.savefig("plots/task2_binary.png")
plt.show()


# =========================================================
# -------------------- TASK 3 ------------------------------
# =========================================================

print("\n----- TASK 3: Recursion Comparison -----")

fact_calls = 0
fib_calls = 0

def factorial(n):
    global fact_calls
    fact_calls += 1
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci_naive(n):
    global fib_calls
    fib_calls += 1
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_dp(n):
    dp = [0]*(n+1)
    if n > 0:
        dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

input_vals = [5, 10, 15, 20]

fact_call_list = []
fib_call_list = []
fib_dp_time = []

for n in input_vals:
    fact_calls = 0
    factorial(n)
    fact_call_list.append(fact_calls)

    fib_calls = 0
    start = time.time()
    fibonacci_naive(n)
    fib_call_list.append(fib_calls)

    start = time.time()
    fibonacci_dp(n)
    fib_dp_time.append(time.time() - start)

    print(f"\nInput: {n}")
    print(f"Factorial Calls: {fact_calls}")
    print(f"Fibonacci Naive Calls: {fib_calls}")

# Graph 1 - Fibonacci Naive Calls
plt.figure()
plt.plot(input_vals, fib_call_list)
plt.xlabel("Input")
plt.ylabel("Function Calls")
plt.title("Fibonacci Naive Call Growth")
plt.grid(True)
plt.savefig("plots/task3_fib_naive.png")
plt.show()

# Graph 2 - Factorial Calls
plt.figure()
plt.plot(input_vals, fact_call_list)
plt.xlabel("Input")
plt.ylabel("Function Calls")
plt.title("Factorial Call Growth")
plt.grid(True)
plt.savefig("plots/task3_factorial.png")
plt.show()

# Graph 3 - Fibonacci DP Time
plt.figure()
plt.plot(input_vals, fib_dp_time)
plt.xlabel("Input")
plt.ylabel("Execution Time")
plt.title("Fibonacci DP Time Growth")
plt.grid(True)
plt.savefig("plots/task3_fib_dp.png")
plt.show()


# =========================================================
# -------------------- TASK 4 ------------------------------
# =========================================================

print("\n----- TASK 4: Recurrence Validation -----")

rec1_calls = 0
rec2_calls = 0

def recurrence1(n):
    global rec1_calls
    rec1_calls += 1
    if n <= 1:
        return 1
    return recurrence1(n//2) + n

def recurrence2(n):
    global rec2_calls
    rec2_calls += 1
    if n <= 1:
        return 1
    return recurrence2(n//2) + recurrence2(n//2) + n

sizes_vals = [8, 16, 32, 64]

rec1_list = []
rec2_list = []

for n in sizes_vals:
    rec1_calls = 0
    rec2_calls = 0
    recurrence1(n)
    recurrence2(n)
    rec1_list.append(rec1_calls)
    rec2_list.append(rec2_calls)

    print(f"\nInput: {n}")
    print(f"T(n)=T(n/2)+n Calls: {rec1_calls}")
    print(f"T(n)=2T(n/2)+n Calls: {rec2_calls}")

# Graph 1
plt.figure()
plt.plot(sizes_vals, rec1_list)
plt.xlabel("Input")
plt.ylabel("Function Calls")
plt.title("T(n)=T(n/2)+n Call Growth")
plt.grid(True)
plt.savefig("plots/task4_rec1.png")
plt.show()

# Graph 2
plt.figure()
plt.plot(sizes_vals, rec2_list)
plt.xlabel("Input")
plt.ylabel("Function Calls")
plt.title("T(n)=2T(n/2)+n Call Growth")
plt.grid(True)
plt.savefig("plots/task4_rec2.png")
plt.show()
