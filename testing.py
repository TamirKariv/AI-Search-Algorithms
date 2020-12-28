import problems
from ways.graph import load_map_from_csv
from problems import create_problems
from problems import write_results_to_file
from problems import get_run_times
from problems import draw_times_graph


def main():
    map = load_map_from_csv()
    create_problems("db/problems.csv",map)
    write_results_to_file("results/UCSRuns.txt", "db/problems.csv",
                                   "ucs", map)
    write_results_to_file("results/AStarRuns.txt", "db/problems.csv",
                                   "astar", map)
    write_results_to_file("results/IDAStarRuns.txt", "db/problems.csv",
                                   "idstar", map)
    ucs_runtime = get_run_times(map, "db/problems.csv", "ucs")
    astar_runtime = get_run_times(map, "db/problems.csv", "astar")
    ida_star_runtime = get_run_times(map, "db/problems.csv", "idastar")
    print(ucs_runtime)
    print(astar_runtime)
    print(ida_star_runtime)
    draw_times_graph("results/AStarRuns.txt")


if __name__ == '__main__':
    main()
