import os, random

for pause_t in range(0, 1000, 100):
    last = None

    # alaki_file = open(f"alaki_{pause_t}", "w")
    # salam_count = random.randint(10, 50)
    # for i in range(100):
    #     if salam_count > 0:
    #         alaki_file.write(f"salam {i + random.randint(0, 10)}\n")
    #         salam_count -= 1
    #     alaki_file.write(f"bye {i + random.randint(0, 10)}\n")
    # alaki_file.close()


    # for run in range(100):
    #     os.system(f"python3 analyse.py {pause_t}")

    # os.system(f"python3 avg.py {pause_t}")

os.system("gnuplot -p gp")