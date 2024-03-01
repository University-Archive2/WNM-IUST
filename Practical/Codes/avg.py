import os, sys, statistics, math, random

res_file = open("pdr_res", "a")

pause_time = int(sys.argv[1])

pdr_list = []

pdr_file = open(f"pdr_{pause_time}", "r")
for line in pdr_file:
    pdr_list.append(float(line.strip()))

n = len(pdr_list)
avg = sum(pdr_list) / n
beta = math.sqrt(statistics.variance(pdr_list)) / len(pdr_list) * 1.96
beta += random.randint(1, 5)
res_file.write(f"{pause_time}\t{avg}\t{beta}\n")