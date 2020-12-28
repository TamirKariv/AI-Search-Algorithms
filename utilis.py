from ways.tools import compute_distance
from ways.info import SPEED_RANGES


def H(node_one, node_two):
    dist = compute_distance(node_one.lat, node_one.lon, node_two.lat,
                            node_two.lon)
    return dist / 110


def link_cost(type, distance):
    speed = SPEED_RANGES[type][1]
    length = distance / 1000
    time = length / speed
    return time


def in_frontier(q, elm):
    for e in q.queue:
        if e[1] == elm:
            return True
    return False


def del_from_frontier(q, elm):
    for idx, e in enumerate(q.queue):
        if e[1] == elm:
            del q.queue[idx]
            break


def reconstruct_rout(parent_dict, end, start, map):
    rout = []
    end = end.index
    while end in parent_dict:
        rout.append(map[end])
        end = parent_dict[end]
    rout.append(start)
    rout.reverse()
    return rout


def calculate_time_of_rout(rout):
    end_node = rout[-1]
    total_time = 0
    for idx, node in enumerate(rout):
        if node == end_node:
            break
        for link in node.links:
            if link.target == rout[idx + 1].index:
                total_time += link_cost(link.highway_type, link.distance)
    return total_time


