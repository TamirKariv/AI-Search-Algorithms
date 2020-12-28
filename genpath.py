import random
import ucs_get_rout
import astar_get_rout
import idastar_get_rout
import problems
from utilis import calculate_time_of_rout
from utilis import calculate_time_of_rout
from utilis import H
from ways.draw import plot_path





def testpaths(map):
    juncs = map.junctions()
    #problems.create_problems("db/problems.csv")
    # problems.write_results_to_file("results/UCSRuns.txt", "db/problems.csv",
    #                                "ucs", map)
    # problems.write_results_to_file("results/AStarRuns.txt", "db/problems.csv",
    #                                "astar", map)
    # problems.write_results_to_file("results/IDAStarRuns.txt", "db/problems.csv",
    #                                "idstar", map)

    # ucs_time = problems.get_run_times(map, "db/problems.csv", "ucs")
    # print(ucs_time)
    # astar_time = problems.get_run_times(map, "db/problems.csv", "astar")
    # print(astar_time)
    # ida_time = problems.get_run_times(map, "db/problems.csv", "ida_time")
    # print(ida_time)
    #problems.draw_times_graph("results/AStarRuns.txt")












    with open("db/problems.csv") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for c in content:
        c.split(",")
        v = c.split(',')
        start = int(v[0])
        end = int(v[1])
        print(" ")
        print(str(start) + "," + str(end))
        path = astar_get_rout.get_rout(start, end, map)
        cost = calculate_time_of_rout(path)
        h_cost = H(juncs[start], juncs[end])
        print(cost)
        print(h_cost)
        if (cost < h_cost):
            print("problem")

        # pp = []
        # for p in path:
        #     pp.append(p.index)
        # cost = find_time(map.junctions(),pp)

        # path = ucs_rout.get_rout_with_map_dict(start, end, map)
        if path_is_illegal(path, map, end):
            print("Bye")
            break
        index_path = []
        for node in path:
            index_path.append(node.index)

        plot_path(juncs,index_path,)

        print(' '.join(str(j) for j in index_path))
        print(len(path))


def path_is_illegal(path, map, end):
    for i in range(len(path)):
        if path[i] == map[end]:
            return False
        found = False
        for link in path[i].links:
            if link.target == path[i + 1].index:
                found = True
                break
        if not found:
            return True
    return False
