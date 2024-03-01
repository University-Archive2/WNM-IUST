import sys


pause_time = int(sys.argv[1])
alaki_file = open(f"alaki_{pause_time}", "r")

count = 0
for line in alaki_file:
    if "salam" in line:
        count += 1


res_file = open(f"pdr_{pause_time}", "a")
res_file.write(f"{count}\n")

