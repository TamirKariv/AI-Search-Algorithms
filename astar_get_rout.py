from queue import PriorityQueue
from utilis import in_frontier
from utilis import del_from_frontier
from utilis import H
from utilis import reconstruct_rout
from utilis import link_cost

def get_rout(start, end, map):
    nodes = map.junctions()
    start_node = nodes[start]
    end_node = nodes[end]
    frontier = PriorityQueue()
    frontier.put((H(start_node, end_node), start_node))
    closed_list = set()
    came_from = {}
    F = {}
    F[start] = H(start_node, end_node)
    while not frontier.empty():
        node_cost, node = frontier.get()
        # G = F-H
        node_cost = node_cost - H(node, end_node)
        if node == end_node:
            return reconstruct_rout(came_from, end_node, start_node, nodes)
        closed_list.add(node)
        for link in node.links:
            child_idx = link.target
            child = nodes[child_idx]
            #f = g + h
            child_f = link_cost(link.highway_type, link.distance) + node_cost + H(child, end_node)
            if child not in closed_list and not in_frontier(frontier, child):
                F[child.index] = child_f
                frontier.put((F[child.index], child))
                came_from[child.index] = node.index
            elif child_f < F[child.index]:
                F[child.index] = child_f
                del_from_frontier(frontier, child)
                frontier.put((F[child.index], child))
                came_from[child.index] = node.index
    return None
