import astar_get_rout
import ucs_get_rout
import idastar_get_rout
from ways.graph import load_map_from_csv


def get_ucs_rout(source, target):
    idx_rout =[]
    map = load_map_from_csv()
    rout = ucs_get_rout.get_rout(source, target, map)
    for node in rout:
        idx_rout.append(node.index)
    return idx_rout


def get_astar_rout(source, target):
    idx_rout = []
    map = load_map_from_csv()
    rout = astar_get_rout.get_rout(source, target, map)
    for node in rout:
        idx_rout.append(node.index)
    return idx_rout


def get_idastar_rout(source, target):
    idx_rout = []
    map = load_map_from_csv()
    rout = idastar_get_rout.get_rout(source, target, map)
    for node in rout:
        idx_rout.append(node.index)
    return idx_rout