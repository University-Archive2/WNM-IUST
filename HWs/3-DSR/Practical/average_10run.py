import sys, statistics, math


def calc_beta(data_list):
    n = len(data_list)
    return statistics.stdev(data_list) / math.sqrt(n) * 1.96


def main(nodes, input_path):
    pdr_list = []
    latency_list = []

    with open(input_path, "r") as input_file:
        for line in input_file:
            pdr, latency = line.split()
            pdr_list.append(float(pdr))
            latency_list.append(float(latency))

    with open("results_average", "a") as output_file:
        output_file.write(f"{nodes} {statistics.mean(pdr_list)} {calc_beta(pdr_list)} {statistics.mean(latency_list)} {calc_beta(latency_list)}\n")


if __name__ == "__main__":
    nodes = int(sys.argv[1])
    input_path = sys.argv[2]
    main(nodes, input_path)

