import sys
from utilis import H
from utilis import reconstruct_rout
from utilis import link_cost


sys.setrecursionlimit(1500)
from ways.tools import compute_distance
import ways.info


def get_rout(start, end, map):
    nodes = map.junctions()
    start_node = nodes[start]
    end_node = nodes[end]
    parent = {}
    current_limit = H(start_node, end_node)
    rout = []
    rout.append(start_node)
    cost = 0
    while current_limit != end_node:
        current_limit = search_rout(rout, cost, current_limit, parent, nodes, end_node)
    return reconstruct_rout(parent, end_node, start_node, nodes)



def search_rout(rout, current_cost, f_limit, parent, nodes, end):
    current_node = rout[-1]
    current_f = current_cost + H(current_node, end)
    if current_f > f_limit:
        return current_f
    if current_node == end:
        return current_node
    new_limit = 999999999999999
    for link in current_node.links:
        child = nodes[link.target]
        if child not in rout:
            parent[child.index] = current_node.index
            rout.append(child)
            cost = current_cost + link_cost(link.highway_type, link.distance)
            current_limit = search_rout(rout, cost, f_limit, parent, nodes, end)
            if current_limit == end:
                return current_limit
            if current_limit < new_limit:
                new_limit = current_limit
            rout.pop()
    return new_limit
