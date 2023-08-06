from matplotlib import pyplot as plt
from collections import Counter

def median(list):
    global v_median
    global sorted_v
    sorted_v = sorted(list)
    midpoint = len(list) // 2
    if len(list) % 2 == 1:
        #v_median = sum(v) // len(v)
        v_median = sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        v_median = (sorted_v[lo] + sorted_v[hi]) // 2
    return print("median is " + str(v_median))

def median_bar(list, xlabel="Set in function", ylabel="Set in function", title="Set in function"):
    global v_median
    global sorted_v
    sorted_v = sorted(list)
    midpoint = len(list) // 2
    if len(list) % 2 == 1:
        #v_median = sum(v) // len(v)
        v_median = sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        v_median = (sorted_v[lo] + sorted_v[hi]) // 2
    for x in range(len(list)):
        if list[x] == v_median:
            n_med_x = x
            break
    xs = range(len(list))
    xs2 = range(len(list))
    ys = [list[x] for x in xs]
    ys2 = v_median
    plt.bar(xs, ys)
    plt.bar(n_med_x,ys2,label="Median")
    plt.legend(loc="best")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def quantiels(list, percent):
    p_index = int(percent*len(list))
    return print(p_index)

def mode(list):
    counts = Counter(list)
    list_max_end = []
    list_max = list(counts.values())
    max_values = max(counts.values())
    for x in range(len(list_max)):
        if list_max[x] == max_values:
            list_max_end.append(x)
    return print(*list_max_end)