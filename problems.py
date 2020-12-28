from ways.graph import load_map_from_csv
import random
import ucs_get_rout
import astar_get_rout
import idastar_get_rout
from utilis import calculate_time_of_rout
from utilis import H
import time
import matplotlib.pyplot as plt


def create_problems(file_name, map):
    nodes = map.junctions()
    f = open(file_name, "w")
    for i in range(100):
        start, end = create_random_path(nodes)
        f.write(str(start) + "," + str(end) + "\n")
    f.close()


def create_random_path(nodes):
    path_length = random.randint(1, 100)
    start = random.randint(0, 944799)
    node = nodes[start]
    for i in range(path_length):
        if len(node.links) == 0:
            return node
        else:
            link_idx = random.randint(0, len(node.links) - 1)
            next_node_idx = node.links[link_idx].target
            node = nodes[next_node_idx]
    end = node.index
    return start, end


def write_results_to_file(results_file, problems_file, algorithem, map):
    nodes = map.junctions()
    w = open(results_file, "w")
    r = open(problems_file, "r")
    read_lines = r.readlines()
    lines = [x.strip() for x in read_lines]
    for line in lines:
        split = line.split(",")
        source = int(split[0])
        target = int(split[1])
        if algorithem == "ucs":
            rout = ucs_get_rout.get_rout(source, target, map)
            time = calculate_time_of_rout(rout)
            w.write(str(time) + "\n")
        elif algorithem == "astar":
            rout = astar_get_rout.get_rout(source, target, map)
            time = calculate_time_of_rout(rout)
            h_time = H(nodes[source], nodes[target])
            w.write(str(h_time) + "," + str(time) + "\n")
        else:
            rout = idastar_get_rout.get_rout(source, target, map)
            time = calculate_time_of_rout(rout)
            h_time = H(nodes[source], nodes[target])
            w.write(str(h_time) + "," + str(time) + "\n")
    w.close()
    r.close()


def get_run_times(map, problems_file, algorithem):
    total_time = 0
    r = open(problems_file, "r")
    read_lines = r.readlines()
    lines = [x.strip() for x in read_lines]
    for line in lines:
        split = line.split(",")
        source = int(split[0])
        target = int(split[1])
        time_start = time.time()
        if algorithem == "ucs":
            ucs_get_rout.get_rout(source, target, map)
        elif algorithem == "astar":
            astar_get_rout.get_rout(source, target, map)
        else:
            idastar_get_rout.get_rout(source, target, map)
        time_end = time.time()
        total_time += time_end - time_start
    return total_time / 100


def draw_times_graph(results_file):
    lines = open(results_file, "r")
    heuristic_times = []
    real_times = []
    for line in lines:
        l = line.split(',')
        real_times.append(float(l[0]))
        heuristic_times.append(float(l[1]))
    plt.scatter(heuristic_times, real_times, s=0.5)
    plt.xlabel("heuristic time")
    plt.ylabel("real time")
    plt.title("Astar Times ")
    plt.show()
