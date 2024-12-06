import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


FILTER_H = 3
FILTER_W = 3
RADIUS = 1

def match_window(window, filter):
    match = True
    for i in range(FILTER_H):
        for j in range(FILTER_W):
            if filter[i, j]:
                if filter[i, j] != window[i, j]:
                    match = False
                    break
        if not match:
            break
    return match

def get_window(arr, x, y):
    box_size = RADIUS
    x_min = max(x - box_size, 0)
    x_max = min(x + box_size + 1, arr.shape[0]) 
    y_min = max(y - box_size, 0)
    y_max = min(y + box_size + 1, arr.shape[1])
    box = arr[x_min:x_max, y_min:y_max]
    return box

with open("input.txt", 'r') as f:

    rows = []

    for line in f:

        rows.append(list(line))

    graph = np.pad(np.array(rows), RADIUS, mode='constant', constant_values=0)

    all_filters = [
        np.array([
            ["S", None, "M"],
            [None, "A", None],
            ["S", None, "M"]
        ]),
        np.array([
            ["M", None, "M"],
            [None, "A", None],
            ["S", None, "S"]
        ]),
        np.array([
            ["M", None, "S"],
            [None, "A", None],
            ["M", None, "S"]
        ]),
        np.array([
            ["S", None, "S"],
            [None, "A", None],
            ["M", None, "M"]
        ])
    ]

    match_count = 0
    for x in range(RADIUS, graph.shape[0] - RADIUS):
        for y in range(RADIUS, graph.shape[1] - RADIUS):
            try:
                for filter in all_filters:
                    if match_window(get_window(graph, x, y), filter):
                        match_count += 1
            except Exception as e:
                print(f"ERROR: Failed to process point ({x}, {y})\nError: {e}")

    print(match_count)
