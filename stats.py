'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple
from collections import Counter
from ways import load_map_from_csv


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    max_branching = max(len(junction.links) for junction in roads.junctions())
    min_branching = min((len(junction.links) for junction in roads.junctions()))
    avg_branching = 0
    for junction in roads.junctions():
        avg_branching += len(junction.links)
    avg_branching /= len(roads.junctions())
    max_distance = -1
    min_distance = 1000000000000
    avg_distance = 0
    link_type_histogram = []
    for node in roads.junctions():
        for link in node.links:
            if link.distance > max_distance:
                max_distance = link.distance
            if link.distance < min_distance:
                min_distance = link.distance
            avg_distance += link.distance
            link_type_histogram.append(link.highway_type)
    avg_distance /= len(list(roads.iterlinks()))
    link_type_histogram = Counter(link_type_histogram)
    return {
        'Number of junctions': len(roads.junctions()),
        'Number of links': len(list(roads.iterlinks())),
        'Outgoing branching factor': Stat(max=max_branching, min=min_branching, avg=avg_branching),
        'Link distance': Stat(max=max_distance, min=min_distance, avg=avg_distance),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': link_type_histogram,  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
