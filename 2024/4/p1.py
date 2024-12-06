import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


FILTER_H = 7
FILTER_W = 7
RADIUS = 3

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

    forward_filter = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, "X", "M", "A", "S"],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])

    backward_filter = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        ["S", "A", "M", "X", None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])
 
    above_filter = np.array([
        [None, None, None, "S", None, None, None],
        [None, None, None, "A", None, None, None],
        [None, None, None, "M", None, None, None],
        [None, None, None, "X", None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])

    below_filter = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, "X", None, None, None],
        [None, None, None, "M", None, None, None],
        [None, None, None, "A", None, None, None],
        [None, None, None, "S", None, None, None]
    ])

    diag_ne_filter = np.array([
        [None, None, None, None, None, None, "S"],
        [None, None, None, None, None, "A", None],
        [None, None, None, None, "M", None, None],
        [None, None, None, "X", None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])

    diag_se_filter = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, "X", None, None, None],
        [None, None, None, None, "M", None, None],
        [None, None, None, None, None, "A", None],
        [None, None, None, None, None, None, "S"]
    ])

    diag_sw_filter = np.array([
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, "X", None, None, None],
        [None, None, "M", None, None, None, None],
        [None, "A", None, None, None, None, None],
        ["S", None, None, None, None, None, None]
    ])

    diag_nw_filter = np.array([
        ["S", None, None, None, None, None, None],
        [None, "A", None, None, None, None, None],
        [None, None, "M", None, None, None, None],
        [None, None, None, "X", None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])

    all_filters = [
        forward_filter,
        backward_filter,
        above_filter,
        below_filter,
        diag_ne_filter,
        diag_se_filter,
        diag_sw_filter,
        diag_nw_filter
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
