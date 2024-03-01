import os


def main(run_count):
    for nodes in [10, 20, 30, 40, 50]:
        for _ in range(run_count):
            os.system(f"printf {nodes} | ./simulation >> results_10run_{nodes}")

        os.system(f"python3 average_10run.py {nodes} results_10run_{nodes}")

        os.system("gnuplot -p rate.gp")
        os.system("gnuplot -p latency.gp")


if __name__ == "__main__":
    main(10)
