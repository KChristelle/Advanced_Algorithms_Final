import collections
import heapq
import sys
from typing import List


def shortestReach(graph, source, destination):
    # INITIALIZE large val
    val = sys.maxsize
    # create dictionary of nodes
    nodes = {
        '1': {'cost': val, 'pred': []},
        '2': {'cost': val, 'pred': []},
        '3': {'cost': val, 'pred': []},
        '4': {'cost': val, 'pred': []},
    }