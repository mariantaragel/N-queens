import sys
import math

if len(sys.argv) != 2:
    print("Error", file=sys.stderr)
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Error", file=sys.stderr)
    exit(1)

list = []

def count_clauses(n):
    clauses = (2 * n) * (math.comb(n, 2) + 1)
    sum = 0
    for i in range(n - 1, 1, -1):
        sum += math.comb(i, 2)
    clauses += 4 * sum + 2 * math.comb(n, 2)
    return clauses

clauses = count_clauses(n)

print("p cnf " + str(n * n) + " " + str(clauses))

for k in range(1, n + 1):
    for i in range((k - 1) * n + 1, k * n + 1):
        list.append(i)
        print(i, end=" ")
    print("0")
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            print("-" + str(list[i]) + " -" + str(list[j]) + " 0")
    list = []

for k in range(1, n + 1):
    for i in range(k, n * (n - 1) + k + 1, n):
        list.append(i)
        print(i, end=" ")
    print("0")
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            print("-" + str(list[i]) + " -" + str(list[j]) + " 0")
    list = []

if n > 1:
    for k in range(1, n + 1):
        for i in range(k, n * (n - k + 1) + 1, n + 1):
            list.append(i)
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                print("-" + str(list[i]) + " -" + str(list[j]) + " 0")
        list = []

    for k in range(n + 1, n * (n - 1) + 2, n):
        for i in range(k, n * n + 1, n + 1):
            list.append(i)
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                print("-" + str(list[i]) + " -" + str(list[j]) + " 0")
        list = []

    for k in range(n, 0, -1):
        for i in range(k, n * (k - 1) + 2, n - 1):
            list.append(i)
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                print("-" + str(list[i]) + " -" + str(list[j]) + " 0")
        list = []

    for k in range(2 * n, n * n + 1, n):
        for i in range(k, n * n + 1, n - 1):
            list.append(i)
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                print("-" + str(list[i]) + " -" + str(list[j]) + " 0")
        list = []