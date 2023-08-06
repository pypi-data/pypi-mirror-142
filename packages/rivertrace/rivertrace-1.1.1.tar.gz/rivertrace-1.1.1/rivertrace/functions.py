from datetime import datetime
import numpy as np
import networkx as nx
from skimage.draw import line


def log(text, indent=0):
    text = str(text).split(r"\n")
    for t in text:
        if t != "":
            out = datetime.now().strftime("%H:%M:%S.%f") + (" " * 3 * (indent + 1)) + t
            print(out)


def shortest_path(matrix, start, end, jump, include_gaps=True):
    log("Calculating path from river skeleton with jump value {}".format(jump))
    pixels = np.where(matrix == 1)
    nodes = []
    edge_nodes = []
    edges = []
    edge_list = []
    G = nx.MultiGraph()
    for i in range(len(pixels[0])):
        if is_node(matrix, pixels[0][i], pixels[1][i]):
            nodes.append([pixels[0][i], pixels[1][i]])

    log("Found {} nodes, locating real edges.".format(len(nodes)), indent=1)
    for node in nodes:
        edges, edge_list = get_real_edges(matrix, node, edges, edge_list)

    log("Found {} real edges, locating jump edges.".format(len(edges)), indent=1)
    for node in nodes:
        edges, edge_list = get_jump_edges(matrix, node, edges, edge_list, jump=jump, include_gaps=include_gaps)

    log("Found {} total edges, calculating shortest path.".format(len(edges)), indent=1)
    for edge in edges:
        edge_nodes.append([int(e) for e in edge[0].split("_")])
        edge_nodes.append([int(e) for e in edge[1].split("_")])
        G.add_edge(edge[0], edge[1], weight=edge[2])

    start_node, end_node = get_start_end_nodes(edge_nodes, start, end)
    log("Identified start ({}) and end ({}) nodes".format(start_node, end_node), indent=1)

    path = nx.dijkstra_path(G, start_node, end_node)

    log("Exporting edges to path.", indent=1)
    full_path = []
    for i in range(1, len(path)):
        for edge in edges:
            if (path[i-1] == edge[0] or path[i] == edge[0]) and (path[i-1] == edge[1] or path[i] == edge[1]):
                p = edge[3]
                if len(p) > 0:
                    if "{}_{}".format(p[0][0], p[0][1]) != path[i-1]:
                        p.reverse()
                    while len(full_path) > 0 and len(p) > 0 and full_path[-1] == p[0]:
                        p.pop(0)
                    full_path = full_path + p
                break
    return full_path


def is_node(matrix, y, x):
    yl, xl = matrix.shape
    p_sum = np.sum(matrix[max(y-1, 0):min(yl, y+2), max(0, x-1):min(xl, x+2)])
    return matrix[y, x] == 1 and p_sum < 3 or p_sum > 3


def get_real_edges(matrix, node, edges, edge_list, max_iter=10000):
    ad = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    yl, xl = matrix.shape
    for i in range(len(ad)):
        count = 0
        path = [node]
        search = True
        y = node[0]+ad[i][0]
        x = node[1]+ad[i][1]
        if x < 0 or x > xl - 1 or y < 0 or y > yl - 1:
            continue
        if matrix[y, x]:
            prev = node
            curr = [y, x]
            path.append(curr)
            while search and count < max_iter:
                count += 1
                prev, curr, search = next_cell(matrix, prev, curr, yl, xl)
                path.append(curr)
                if count > max_iter-20:
                    log("WARNING: Count: {}, node: {}".format(count, curr), indent=2)
            if count >= max_iter:
                log("Iterations following path exceeded maximum allowed. Start node: {}".format(node), indent=2)
            else:
                start_end = ["{}_{}".format(node[0], node[1]), "{}_{}".format(curr[0], curr[1])]
                start_end.sort()
                while len(path) > 1 and path[-1] == path[-2]:
                    path.pop(-1)
                edge = [start_end[0], start_end[1], count, path]
                el = "_".join([start_end[0], start_end[1]])
                if el not in edge_list:
                    edge_list.append(el)
                    edges.append(edge)
    return edges, edge_list


def get_jump_edges(matrix, node, edges, edge_list, jump=10, jump_factor=1000, jump_power=3, include_gaps=True):
    yl, xl = matrix.shape
    y = node[0]
    x = node[1]
    for i in range(max(y - jump, 0), min(yl, y + 1 + jump)):
        for j in range(max(x - jump, 0), min(xl, x + 1 + jump)):
            if not (i == y and j == x) and is_node(matrix, i, j):
                count = (jump_factor * ((i-y)**2+(j-x)**2)**0.5) ** jump_power
                start_end = ["{}_{}".format(y, x), "{}_{}".format(i, j)]
                start_end.sort()
                if include_gaps:
                    path = [list(x) for x in list(np.transpose(np.array(line(y, x, i, j))))]
                else:
                    path = []
                edge = [start_end[0], start_end[1], count, path]
                el = "_".join([start_end[0], start_end[1]])
                if el not in edge_list:
                    edge_list.append(el)
                    edges.append(edge)
    return edges, edge_list


def get_start_end_nodes(nodes, start, end):
    nodes = np.asarray(nodes)
    dist_1 = np.sum((nodes - start) ** 2, axis=1)
    dist_2 = np.sum((nodes - end) ** 2, axis=1)
    node1 = nodes[np.argmin(dist_1)]
    node2 = nodes[np.argmin(dist_2)]
    start_node = "{}_{}".format(node1[0], node1[1])
    end_node = "{}_{}".format(node2[0], node2[1])
    return start_node, end_node


def next_cell(matrix, prev, curr, yl, xl):
    ad = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    pprev = prev
    y = curr[0]
    x = curr[1]
    if np.sum(matrix[max(y-1, 0):min(yl, y+2), max(0, x-1):min(xl, x+2)]) == 3:
        prev = curr
        for i in range(8):
            y_n = y + ad[i][0]
            x_n = x + ad[i][1]
            if x_n < 0 or x_n > xl - 1 or y_n < 0 or y_n > yl - 1:
                continue
            curr = [y_n, x_n]
            if matrix[y_n, x_n] and curr != prev and curr != pprev:
                break
        return prev, curr, True
    else:
        return prev, curr, False