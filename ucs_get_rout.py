from queue import PriorityQueue
from utilis import in_frontier
from utilis import del_from_frontier
from utilis import link_cost
from utilis import reconstruct_rout


def get_rout(start, end, map):
    nodes = map.junctions()
    start_node = nodes[start]
    end_node = nodes[end]
    frontier = PriorityQueue()
    frontier.put((0, start_node))
    closed_list = set()
    parent = {}
    F = {}
    F[start] = 0
    while not frontier.empty():
        node_cost, node = frontier.get()
        if node == end_node:
            return reconstruct_rout(parent, end_node, start_node, nodes)
        closed_list.add(node)
        for link in node.links:
            child_idx = link.target
            child = nodes[child_idx]
            child_f = link_cost(link.highway_type, link.distance) + node_cost
            if child not in closed_list and not in_frontier(frontier, child):
                F[child.index] = child_f
                frontier.put((F[child.index], child))
                parent[child.index] = node.index
            elif child_f < F[child.index]:
                F[child.index] = child_f
                del_from_frontier(frontier, child)
                frontier.put((F[child.index], child))
                parent[child.index] = node.index
    return None
